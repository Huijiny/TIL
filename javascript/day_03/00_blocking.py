from time import sleep
import requests

# 1. sleep
def sleep_3_seconds():
    sleep(3)
    print('잘잤다.')
print('goodnight')
sleep_3_seconds()
print('go')

# 2. requests

response = requests.get( 'https://jsonplaceholder.typicode.com/todos/1/')
todo = response.json()