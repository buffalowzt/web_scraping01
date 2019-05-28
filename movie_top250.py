import requests
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36', 'Host': 'movie.douban.com'}
r = requests.get('http://movie.douban.com/', headers=headers)
print('Response_code:', r.status_code)
for i in range(0,10):
    link = 'https://movie.douban.com/top250?start=' + str(i * 25)
    r = requests.get(link, headers=headers, timeout=10)
    print(r.text)



import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36', 'Host': 'movie.douban.com'}
r = requests.get('http://movie.douban.com/', headers=headers)
print('Response_code:', r.status_code)
movie_list = []
for i in range(0,10):
    link = 'https://movie.douban.com/top250?start=' + str(i * 25)
    r = requests.get(link, headers=headers, timeout=10)
    soup = BeautifulSoup(r.text,"lxml")
    div_list = soup.find_all('div', class_= 'hd')
    for each in div_list:
        movie = each.a.span.text.strip()
        movie_list.append(movie)
print(movie_list)
