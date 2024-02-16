from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup as bs
import requests

import time
import random
from datetime import datetime, timedelta

import hashlib
import os

_options = Options()

_user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
_options.add_argument(f'user-agent={_user_agent}')
_options.add_experimental_option('detach', True)
_options.add_experimental_option('excludeSwitches', ['enable-automation'])
_driver = webdriver.Chrome(options=_options)

_basic_url = 'https://news.naver.com/opinion/series?whole=Y&sid='
_categories = ["NORMAL", "POLITICS", "ECONOMY", "SOCIETY", "LIFE", "WORLD", "IT"]

# 어제 날짜 정보 가져오기
_today = datetime.now()
_yesterday = _today - timedelta(days=1)
# _yesterday = _today
_scrap_day = f"{_yesterday.year}{str(_yesterday.month).zfill(2)}{str(_yesterday.day).zfill(2)}"

_compare_timestamp = lambda a, b : int(a) - int(b)

def _scrap_opinion(url):
  _driver.get(url)
  time.sleep(random.uniform(1, 4))
  while True:
    items = _driver.find_elements(By.CSS_SELECTOR, "li.opinion_serialization_item")
    last_timestamp = items[-1].find_element(By.CLASS_NAME, "timestamp").text.replace(".", "")
    if _compare_timestamp(last_timestamp, _scrap_day) < 0:
      break
    _driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(random.uniform(1, 3))

  def get_thumbnail_link(item):
    # 썸네일이 없는 경우가 있어서 try문으로 실행
    try:
      return item.find_element(By.CSS_SELECTOR, ".article_item.as_type_main img").get_attribute("src").split("?")[0]
    except:
      return None

  opinions = []
  for item in items:
    # 기사가 작성된 날짜와 스크랩 할 날짜 비교
    timestamp = item.find_element(By.CLASS_NAME, "timestamp").text.replace(".", "")
    timestamp_diff = _compare_timestamp(timestamp, _scrap_day)
    # 날짜가 같으면 추출
    if timestamp_diff == 0:
      temp = {
        "title": item.find_element(By.CLASS_NAME, "article_text").text,
        "press": item.find_element(By.CLASS_NAME, "press_name").text,
        "journalist": None,
        "upload_time": None,
        "update_time":None,
        "naver_url": item.find_element(By.CSS_SELECTOR, ".article_list .link").get_attribute('href'),
        "original_url": None,
        "summary": None,
        "header": item.find_element(By.CLASS_NAME, "header_name").text,
        "thumbnail_url": get_thumbnail_link(item),
        "thumbnail_file_name": None,
        "category": None,
      }
      opinions.append(temp)
    # 스크랩 날짜보다 크면 건너뛰기
    elif timestamp_diff > 0:
      continue
    # 스크랩 날짜보다 작으면 더이상 비교할 필요가 없으므로 종료
    else:
      break
  return opinions

def scrap_detail(opinion_dict):
  #url을 bs4로 가져오기
  header_user = {"User-Agent": _user_agent}

  def get_element(element, selector):
    try:
      return element.select_one(selector)
    except:
      return None
  
  def get_element_attribute(element, selector, attribute):
    try:
      return element.select_one(selector)[attribute]
    except:
      return None

  def get_opinion_summary(elements, title):
    for element in elements:
      e_title = element.select_one(".shn_headline_text").text
      if e_title == title:
        return element.select_one(".shn_summary").text
    return None
  
  # os의 위치를 thumbnail_path로 변경
  # --> 프로그램이 db/save_data.py 에서 실행이 되므로 
  current_file = os.path.realpath(__file__)
  os.chdir(os.path.dirname(current_file) + "/thumbnails")
  # 현재 폴더 경로 변수에 저장
  current_path = os.getcwd()

  # 이미지파일을 날짜별로 정리하기 위해서 스크랩날짜 폴더 생성
  if not os.path.exists(str(_scrap_day)):
    os.mkdir(str(_scrap_day))

  def download_img(url, title):
    if url == None:
      return None
    
    try:
      response = requests.get(url)
      # 파일명을 압축후 8자리만 추출
      hash_code = hashlib.md5(title.encode()).hexdigest()[:8]
      # 파일명이 겹치지 않게 저장하는 시간대와 함께 저장
      file_name = f"{int(time.time())}_{hash_code}"
      # 파일 저장경로
      save_path = f"{current_path}/{_scrap_day}/{file_name}.png"
      with open(save_path, 'wb') as file:
        file.write(response.content)
        print('downaload complete')
    except:
      print('download fail')
      file_name = None
    
    return file_name

  for category in _categories:
    opinions = opinion_dict[category]
    for opinion in opinions:
      req = requests.get(opinion["naver_url"], headers=header_user)
      html = req.text
      soup = bs(html, "html.parser")

      opinion_header = soup.select_one('.media_end_head.go_trans')

      upload_time = get_element_attribute(opinion_header, "span[data-date-time]", "data-date-time")
      update_time = get_element_attribute(opinion_header, "span[data-modify-date-time]", "data-modify-date-time")
      original_url = get_element_attribute(opinion_header, ".media_end_head_origin_link", "href")
      summary = get_opinion_summary(soup.select(".shn_text"), opinion["title"])
      thumbnail_file_name = download_img(opinion["thumbnail_url"], opinion["title"])
      try:
        journalist = get_element(opinion_header, ".media_end_head_journalist_name").text.split(" ")[0]
      except:
        journalist = None

      opinion["upload_time"] = upload_time
      opinion["update_time"] = update_time
      opinion["original_url"] = original_url
      opinion["summary"] = summary
      opinion["journalist"] = journalist
      opinion["category"] = category
      opinion["thumbnail_file_name"] = thumbnail_file_name

def scrap():
  opinion_dict = {}
  for category in _categories:
    opinions = _scrap_opinion(_basic_url + category)
    opinion_dict[category] = opinions
  # 셀레니움 역할은 끝났으므로 driver 종료
  _driver.quit()

  # bs4를 활용해 기사 정보 스크랩
  scrap_detail(opinion_dict)

  return opinion_dict
