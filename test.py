import requests
import json
url = "http://127.0.0.1:9528/TestServer"
#119.28.87.35:9528
#127.0.0.1:9528
in_dic = {
    'init_info': {
        'round_number': 1,
        'honba_sticks': 0,
        'reach_sticks': 0,
        'bonus_tile_indicator': [30, 31],
        'dealer': 1, #逆时针0123,场自风自动计算
        'scores': [1000, 1000, 1000, 1000],
    },
    '0': {
        'tiles': [1, 1,1,   5, 5,   17, 17,     ],
        'discards': [4],
        'reach': False
    },
    'melds': [
        {
            'type': 'chi',
            'tiles': [13, 14, 15],
            'called_tile': 13,
            'from_whom': 1,
            'by_whom': 0,
        },
        {
            'type': 'chi',
            'tiles': [20, 21, 22],
            'called_tile': 20,
            'from_whom': 1,
            'by_whom': 0,
        },
    ],
    'todo':{
        'new_tile':7,
        'chi':False,
        'pon':False,
        'minkan':False,
        'ankan':False,
        'reach':True
    }
}
headers = {
    'Content-Type': "text/plain",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "d5639969-8fbd-4531-9ad5-9a1bbe99089a,0c1fee63-a3e2-4a81-89ea-8b8861a0aa61",
    'Host': "192.168.1.108:8080",
    'accept-encoding': "gzip, deflate",
    'content-length': "12",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, json=in_dic, headers=headers)
a =  json.loads(response.text)

print(a)