import requests
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36', 'Host': 'movie.douban.com'}
r = requests.get('http://movie.douban.com/', headers=headers)
print('Response_code:', r.status_code)
for i in range(0,10):
    link = 'https://movie.douban.com/top250?start=' + str(i * 25)
    r = requests.get(link, headers=headers, timeout=10)
    print(r.text)
