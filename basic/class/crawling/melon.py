import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, 'html.parser')

# lst50 = soup.select('.lst50')
# lst100 = soup.select('.lst100')
# top100 = lst50 + lst100
# print(len(lst50), len(lst100), len(top100))

list_all = soup.find_all(class_=['lst50, lst100']) # << 한번에 찾아서 리스트로 만들어줌

song = soup.select('.rank01 > span > a')
artist = soup.select('.rank02 > span')
album = soup.select('.rank03 > a')
for rank, i in enumerate(zip(song, artist, album), 1):
  print(f'{rank} {i[0].text} - {i[1].text} ({i[2].text})')