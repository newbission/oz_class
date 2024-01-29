import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
search_url = '손흥민'

url = base_url + search_url
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, 'html.parser')

title = soup.select('.title_link')
name = soup.select('.user_info .name')

for i in zip(title, name):
  print(i[0].a['href'], type(i[0]['href']))
  (t, n) = i
  print(i[0].text, i[0]['href'])
  print(i[1].text, i[1]['href'])
  print()
  print()