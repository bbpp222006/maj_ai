# maj_ai
基于开源代码实现的麻将ai

算法基于https://github.com/erreurt/MahjongAI 
这里只是做了个封装(并没有进行测试)  
介绍一下输入json格式

```
in_dic = {
    'init_info': {  #此为场地初始化
        'round_number': 1,
        'honba_sticks': 0,
        'reach_sticks': 0,
        'bonus_tile_indicator': [30, 31],
        'dealer': 1, #逆时针0123,场自风自动计算
        'scores': [1000, 1000, 1000, 1000],
    },
    '0': {  #0号位的各种状态
        'tiles': [1, 1,1,   5, 5,   17, 17,     ],  #手牌, 0123为1万, 依次延后, 一共136种(可以像这里一样重复输入)
        'discards': [4],  #当前位置的牌河
        'reach': False  #是否立直
    },
    'melds': [  #场上的各种明牌
        {
            'type': 'pon',  # 'chi','pon','kan'
            'tiles': [13, 14, 15], #涉及到的牌
            'called_tile': 13,  #哪张是别家的
            'from_whom': 1,  #从哪家
            'by_whom': 0,  #被哪家
        },
        {
            'type': 'chi',  #同上
            'tiles': [20, 21, 22],
            'called_tile': 20,
            'from_whom': 1,
            'by_whom': 0,
        },
    ],
    'todo':{  #发送json时的状态
        'new_tile':7,  #涉及到的新牌(比如摸的牌,别家打出的牌等等)
        'chi':False,  #当前状态可以吃
        'pon':False, #当前状态可以碰
        'minkan':False,#当前状态可以杠(明杠)
        'ankan':False,#当前状态可以杠(暗杠)
        'reach':True#当前状态可以立直
    }

```
