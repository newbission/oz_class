from selenium import webdriver
from bs4 import BeautifulSoup
import time

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
search_url = '홍삼'
url = base_url + search_url

driver = webdriver.Chrome()
driver.get(url)


# 스크롤 코드
# driver.execute_script('window.scrollTo(0, 4000)')
# time.sleep(1)

for i in range(5):
  driver.execute_script(f'window.scrollTo(0, document.body.scrollHeight)')
  time.sleep(.5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

area = soup.select('.view_wrap')
filtered_area = [item for item in area if not item.select_one('.link_ad')]
for num, item in enumerate(filtered_area, 1):
  title = item.select_one('.title_link._cross_trigger')
  name = item.select_one('.user_info > a')
  print(num)
  print(f'title: {title.text}')
  print(f'name : {name.text}')
  print(f'link: {title['href']}')
  print()

time.sleep(5)