from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs

import requests as req
import time
import random
from datetime import datetime, timedelta


import pprint

options = Options()

user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
options.add_argument(f'user-agent={user}')
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=options)

basic_url = 'https://news.naver.com/opinion/series?whole=Y&sid='
categories = ["NORMAL", "POLITICS", "ECONOMY", "SOCIETY", "LIFE", "WORLD", "IT"]

# 어제 날짜 정보 가져오기
today = datetime.now()
yesterday = today - timedelta(days=1)
scrap_day = f"{yesterday.year}{str(yesterday.month).zfill(2)}{str(yesterday.day).zfill(2)}"

compare_timestamp = lambda a, b : int(a) - int(b)


def scrap_opinion(url):
  driver.get(url)
  time.sleep(random.uniform(1, 4))
  while True:
    items = driver.find_elements(By.CSS_SELECTOR, "li.opinion_serialization_item")
    last_timestamp = items[-1].find_element(By.CLASS_NAME, "timestamp").text.replace(".", "")
    if compare_timestamp(last_timestamp, scrap_day) < 0:
      break
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(random.uniform(1, 3))

  opinions = []
  for item in items:
    timestamp = item.find_element(By.CLASS_NAME, "timestamp").text.replace(".", "")
    timestamp_diff = compare_timestamp(timestamp, scrap_day)
    # print(timestamp, scrap_day, timestamp_diff)
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
      }
      opinions.append(temp)
    elif timestamp_diff == 1:
      continue
    else:
      break
  return opinions

opinion_dict = {}
for category in categories:
  opinions = scrap_opinion(basic_url + category)
  opinion_dict[category] = opinions
driver.quit()
pprint.pprint(opinion_dict["IT"])
