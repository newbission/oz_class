from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup as bs
import requests

import time
import random
from datetime import datetime, timedelta


from pprint import pprint

import hashlib

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
# yesterday = today - timedelta(days=1)
_yesterday = _today
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
    try:
      return item.find_element(By.CSS_SELECTOR, ".article_item.as_type_main img").get_attribute("src").split("?")[0]
    except:
      return None

  opinions = []
  for item in items:
    timestamp = item.find_element(By.CLASS_NAME, "timestamp").text.replace(".", "")
    timestamp_diff = _compare_timestamp(timestamp, _scrap_day)
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
        "category": None,
      }
      opinions.append(temp)
      break
    elif timestamp_diff == 1:
      continue
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

  for category in _categories:
    opinions = opinion_dict[category]
    for opinion in opinions:
      req = requests.get(opinion["naver_url"], headers=header_user)
      html = req.text
      soup = bs(html, "html.parser")

      opinion_header = soup.select_one('.media_end_head.go_trans')

      # upload_time = soup.select_one("span[data-date-time]")["data-date-time"]
      upload_time = get_element_attribute(opinion_header, "span[data-date-time]", "data-date-time")
      update_time = get_element_attribute(opinion_header, "span[data-modify-date-time]", "data-modify-date-time")
      original_url = get_element_attribute(opinion_header, ".media_end_head_origin_link", "href")
      summary = get_opinion_summary(soup.select(".shn_text"), opinion["title"])
      try:
        journalist = get_element(opinion_header, ".media_end_head_journalist_name").text.split(" ")[0]
      except:
        journalist = None


      # print(opinion["title"], original_url, journalist)
      
      opinion["upload_time"] = upload_time
      opinion["update_time"] = update_time
      opinion["original_url"] = original_url
      opinion["summary"] = summary
      opinion["journalist"] = journalist
      opinion["category"] = category
      
  
  

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
  pprint(opinion_dict)

# scrap()