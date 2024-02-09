from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import requests as req
import time

options = Options()

user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
options.add_argument(f'user-agent={user}')
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=options)

url = 'http://kream.co.kr'
driver.get(url)

time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.btn_search').click()

time.sleep(.5)
search_bar = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
search_bar.click()
search_bar.send_keys('슈프림\n')
# '\n'대신에 Keys.ENTER도 가능하다

# 스크롤 밑으로 내리기
html = None
for item in range(5):
  driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
  time.sleep(1)

# 썸네일 이미지 다운로드
def download_img(url, save_path):
  response = req.get(url)
  if response.status_code == 200:
    with open(save_path, 'wb') as file:
      file.write(response.content)
      print('downaload complete')
  else:
    print('download fail')


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

driver.quit()

items = soup.select('.item_inner')
brand = soup.select_one('.product_info_brand.brand')
num = 1
for item in items:
  product_name_ko = item.select_one('.translated_name')
  if not '후드' in product_name_ko.text:
    continue

  print(num)
  #브랜드명
  print(f'Brand:{brand.text}')
  #제품명
  product_name_en = item.select_one('.product_info_product_name .name')
  print(f'Product: {product_name_en.text}')
  #가격
  price = item.select_one('.amount')
  print(f'Price: {price.text}')

  #썸네일 다운로드
  thumbnail_url = item.select_one('img[data-v-44ba780a]')['src']
  save_path = f'./thumbnails/{brand.text.strip()}-{product_name_en.text}.png'
  download_img(thumbnail_url, save_path)
  print()
  num += 1