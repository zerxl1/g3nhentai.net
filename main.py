import time
import requests
import os
import random
from time import sleep


hentai = 'https://nhentai.net/g/'
number = '1234567890'
number2 = '123'

#webhook here
webhooklink = ''

print(' ')
for i in range(9999):
    message = 'มาเเจกของคุบ ' + hentai + random.choice(number2) + random.choice(number) + random.choice(number) + random.choice(number) + random.choice(number) + random.choice(number) + '/'
    _data = requests.post(webhooklink, json={'content': message}, headers={'Content-Type': 'application/json'})
    if _data.status_code == 204:
        print(f'[+] send nhentai.net {message}')
    if _data.status_code == 429:
        print(f"[-] rate limited in 10 (s)")
        time.sleep(10)
