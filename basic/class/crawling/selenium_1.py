from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = 'https://www.naver.com'
driver = webdriver.Chrome()
driver.get(url)

title = driver.title
print(title)

element = driver.find_element(by='id', value='query')
element.send_keys('손흥민\n')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

query = soup.select_one('#query')
print(query)
time.sleep(100000000)