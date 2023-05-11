import time
import requests
from urllib.parse import urlencode

# Telegram

# @NamasteHacker


Email=input('Enter Your Email : ')
Password=input('Enter Your PassWord : ')

headers = {
    'Host': 'www.facebook.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Connection': 'close',
}

response = requests.get('https://www.facebook.com/', headers=headers)
fr=response.cookies['fr']
sb=response.cookies['sb']
_datr=response.text.split('"_js_datr","')[1].split('"')[0]
_token=response.text.split('privacy_mutation_token=')[1].split('"')[0]
_jago=response.text.split('"jazoest" value="')[1].split('"')[0]
_lsd=response.text.split('name="lsd" value="')[1].split('"')[0]


cookies = {
    'fr': fr,
    'sb': sb,
    '_js_datr': _datr,
    'wd': '717x730',
    'dpr': '1.25',
}

data = urlencode({
    'jazoest': _jago,
    'lsd': _lsd,
    'email': Email,
    'login_source': 'comet_headerless_login',
    'next': '',
    'encpass': f'#PWD_BROWSER:0:{round(time.time())}:{Password}',
})


headers = {
    'Host': 'www.facebook.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://www.facebook.com/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': str(len(data)),
    'Origin': 'https://www.facebook.com',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
}

response = requests.post(f'https://www.facebook.com/login/?privacy_mutation_token={_token}', cookies=cookies, headers=headers, data=data)

if 'The email address you entered isn&#039;t connected to an account' in response.text:
    print('The email address you entered is not connected to an account')
elif 'The email address or mobile number you entered isn&#039;t connected to an account' in response.text:
    print('The email address or mobile number you entered is not connected to an account')

elif 'The password that you&#039;ve entered is incorrect.' in response.text:
    print("The password that you've entered is incorrect")
elif 'Choose a way to confirm that it&#039;s you' in response.text:
    print('Two Factor Code Sended.....')
elif 'should_show_close_friend_badge":false' in response.text:
    print('Login Success ')
else:
    print(response.content) # If They Showing Html Code Copy And Paste On Html Viewer Website And Check What Response Show You .


