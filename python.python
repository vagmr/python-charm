import struct
import base64
import requests
import random

headers = {
    't': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjQxNjU2NzIsIm5iZiI6MTY2MzkwODEwOSwiaWF0IjoxNjYzOTA2MzA5LCJqdGkiOiJDTTpjYXRfbWF0Y2g6bHQxMjM0NTYiLCJ1aWQiOjEyMjk0NjY1OCwidmVyIjoiMSIsImV4dCI6IjM2MzMzMjY0MzI2NTY1MzYzNTY2MzkzMDYzNjQzMjY1NjM2MzYyMzEzMjYyMzI2MSIsImNvZGUiOiJjYWNiMGI4MmE4MzMxZjE2NmRmZDZiYWMwZGFmMmFjNyIsImVuZCI6MTY2NDE2NTY3MjkyMn0.IpPw0J69Xk9aqXkTspOQKvqCYaAQOB5KBSeyi4xVxdo',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF',
    'Referer': 'https://servicewechat.com/wx141bfb9b73c970a9/23/page-frame.html'

}
url = 'https://cat-match.easygame2021.com/sheep/v1/game/personal_info?'
r = requests.get(url, headers=headers)
print(r.json())
url = 'https://cat-match.easygame2021.com/sheep/v1/game/map_info_ex?matchType=3'
r = requests.get(url, headers=headers)
print(r.json())
map_md5 = r.json()['data']['map_md5'][1]
url = f'https://cat-match-static.easygame2021.com/maps/{map_md5}.txt'  # 由于每天获取的地图不一样，需要计算地图大小
r = requests.get(url)
print(r.json())
levelData = r.json()['levelData']
p = []
for h in range(len(sum(levelData.values(), []))):  # 生成操作序列
    p.append({'chessIndex': 127 if h > 127 else h, 'timeTag': 127 if h > 127 else h})
GAME_DAILY = 3
GAME_TOPIC = 4
data = struct.pack('BB', 8, GAME_DAILY)
for i in p:
    c, t = i.values()
    data += struct.pack('BBBBBB', 34, 4, 8, c, 16, t)
MatchPlayInfo = base64.b64encode(data)
print(MatchPlayInfo)
print(MatchPlayInfo.decode('utf-8'))
cost_time = random.randint(1, 3600)
url = 'https://cat-match.easygame2021.com/sheep/v1/game/game_over_ex?'
r = requests.post(url, headers=headers,
                  json={'rank_score': 1, 'rank_state': 1, 'rank_time': cost_time, 'rank_role': 1, 'skin': 34,
                        'MatchPlayInfo': MatchPlayInfo.decode('utf-8')})

url = 'https://cat-match.easygame2021.com/sheep/v1/game/update_user_skin?skin=27'
r = requests.get(url, headers=headers)
print(r.json())
url = 'https://cat-match.easygame2021.com/sheep/v1/game/personal_info?'
r = requests.get(url, headers=headers)
print(r.json())
