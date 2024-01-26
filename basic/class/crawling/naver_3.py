import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query="
# search_url = input("검색어를 입력해주세요 : ")
search_url = '손흥민'

url = base_url + search_url
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

titles = soup.select(".keyword_box_wrap.type_color")
for i in titles:
  name = i.select_one(".name.elss")
  category = i.select_one(".etc_area")
  title = i.select_one('.title_area')
  print(f"블로그 작성자는 : {name.text}")
  print(f"분야 : {category.text}")
  print(f"제목 : {title.text}")
  print()