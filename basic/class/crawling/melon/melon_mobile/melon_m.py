from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as keys
from bs4 import BeautifulSoup
import time

options = Options()

# 유저 정보 넣기 (모바일버전))
user = "mozilla/5.0 (iphone; cpu iphone os 15_0 like mac os x) applewebkit/605.1.15 (khtml, like gecko) crios/94.0.4606.52 mobile/15e148 safari/604.1"
options.add_argument(f'user-agent={user}')

# 모바일 처럼 보이게 화면 크기 조정
# options.add_argument('window-size=412,950')

# 자동 종료 해제 옵션
options.add_experimental_option('detach', True)

# 상단 - 조작되고 있다는 메시지를 지우는 옵션
options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=options)

url = 'https://m2.melon.com/index.htm'
driver.get(url)
time.sleep(1)

if driver.current_url != url :
  driver.get(url)
  time.sleep(0.5)

driver.find_element(by.LINK_TEXT, '닫기').click()
time.sleep(.2)
driver.find_element(by.LINK_TEXT, '멜론차트').click()
time.sleep(1)
driver.find_element(by.CSS_SELECTOR, '.swiper_slide.main_chart #moreBtn').click()
time.sleep(.5)

html = driver.page_source
driver.quit()
soup = BeautifulSoup(html, 'html.parser')
chart = soup.select('#_chartList .list_item')

def extractNumber(str):
  return ''.join([x for x in list(str) if x.isdigit()])

album_base_url = 'https://m2.melon.com/album/music.htm?albumId='
song_base_url = 'https://m2.melon.com/song/lyrics.htm?songId='
for item in chart:
  rank = item.select_one('.ranking_num').text.strip()
  title = item.select_one('.title').text.strip()
  artist = item.select_one('.name').text.strip()
  album_id = extractNumber(item.select_one('.thumb a')['href'])
  album_url = album_base_url+album_id
  song_id = extractNumber(item.select_one('.content a')['href'])
  song_url = song_base_url+song_id
  thumbnail_url = item.select_one('.img')['style']
  print(f'[{rank}] {title} - {artist}')

