import requests
import json

answers = [
19,
'busan',
'ssafycial',
'protocol',
'json',
'singleton',
'cookie',
'redis',
'mvvm',
'pandas',
'bluetooth',
'fittymon',
'memoization',
'ioc',
'docker',
'dfs',
'bloom',
'a',
'quick',
'kubernetes'
]

def req(nextUrl, i):
    headers = {'Content-Type': 'application/json; chearset=utf-8'}
    URL = 'http://13.125.222.176/quiz/{}'.format(nextUrl)
    data = {
        'nickname': '서울 4반 유희진',
        'yourAnswer': answers[i]
    }
    response = requests.post(URL, data=json.dumps(data), headers=headers)
    print(response.json())

    return response.json()
next = 'alpha'

i = 0
while next != '수고하셨습니다.':
    response = req(next, i)
    if response['code'] == 200:
        next = response['nextUrl']
        i += 1


