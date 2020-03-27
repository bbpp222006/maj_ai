# -*- coding: utf-8 -*-
import importlib
from client.mahjong_table import GameTable
from client.mahjong_meld import Meld


class AI:
    def __init__(self,in_dic):
        self.in_dic = in_dic
        ai_module = importlib.import_module("test_agent.jianyang_ai")
        waiting_prediction_class = getattr(ai_module, "EnsembleCLF")
        ensemble_clfs = waiting_prediction_class()
        ai_class = getattr(ai_module, "MLAI")
        ai_obj = ai_class(ensemble_clfs)
        opponent_class = getattr(ai_module, "OppPlayer")
        self.game_table = GameTable(ai_obj, opponent_class, None)
        self.init_state()

    def _meld_sort(self,meld_dic):
        meld_sorted = Meld()
        meld_sorted.by_whom = meld_dic['by_whom']
        meld_sorted.from_whom = meld_dic['from_whom']
        meld_sorted.type = meld_dic['type']
        meld_sorted.tiles = meld_dic['tiles']
        meld_sorted.called_tile = meld_dic['called_tile']
        return meld_sorted

    def init_state(self):
        # 重置现场
        self.game_table.init_round(
            self.in_dic['init_info']['round_number'],
            self.in_dic['init_info']['honba_sticks'],
            self.in_dic['init_info']['reach_sticks'],
            self.in_dic['init_info']['bonus_tile_indicator'],
            self.in_dic['init_info']['dealer'],
            self.in_dic['init_info']['scores']
        )
        #重置手牌
        self.game_table.bot.init_hand(self.in_dic['0']['tiles'])

        #重置牌河
        for i in range(4):
            if str(i) in self.in_dic:
                for disc in self.in_dic[str(i)]['discards']:
                    self.game_table.discard_tile(i, disc)
        #重置吃碰杠
        if 'melds' in self.in_dic:
            for meld in self.in_dic['melds']:
                meld_sorted = self._meld_sort(meld)
                self.game_table.call_meld(meld_sorted.by_whom, meld_sorted)

    def next_step(self):
        return_dic = {
        'chi':False,
        'pon':False,
        'kan':False,  #包含了明暗枪杠
        'involved_tiles':[],
        'discard_tile':None,
        'reach':False
        }
        if self.in_dic['todo']['chi'] or self.in_dic['todo']['pon'] :
            meld, tile_to_discard = self.game_table.bot.try_to_call_meld(self.in_dic['todo']['new_tile'] , True)
            if meld:
                return_dic[meld.type] = True
                return_dic['involved_tiles'] = meld.tiles
                return_dic['discard_tile'] = tile_to_discard
        if self.in_dic['todo']['minkan']: #包含明枪杠
            Kan_type,tile = self.game_table.bot.should_call_kan(self.in_dic['todo']['new_tile'],True)
            return_dic['kan'] = True
            return_dic['involved_tiles'] = tile


        self.game_table.bot.draw_tile(self.in_dic['todo']['new_tile'])
        if self.in_dic['todo']['reach']:
            can_call_reach, to_discard_136 = self.game_table.bot.can_call_reach()
            return_dic['reach'] = can_call_reach
            return_dic['discard_tile'] = to_discard_136
        if self.in_dic['todo']['ankan']:
            Kan_type, tile = self.game_table.bot.should_call_kan(self.in_dic['todo']['new_tile'], False)
            return_dic['kan'] = True
            return_dic['involved_tiles'] = tile

        discard_tile_136 = self.game_table.bot.to_discard_tile()
        return_dic['discard_tile'] = discard_tile_136

        return return_dic


