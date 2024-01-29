import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
search_url = '홍삼'

url = base_url + search_url
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, 'html.parser')

area = soup.select('.view_wrap')
filteredArea = [i for i in area if not i.select_one('.link_ad')]

for i in filteredArea:
  title = i.select_one('.title_link._cross_trigger')
  name = i.select_one('.user_info .name')
  print(f'title: {title.text}')
  print(f'user: {name.text}')
  print(f'link: {title['href']}')
  print()