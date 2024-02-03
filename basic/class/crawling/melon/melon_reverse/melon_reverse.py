import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

url_list = [
  'https://www.melon.com/chart/month/index.htm?classCd=GN0000',
  'https://www.melon.com/chart/month/index.htm?classCd=DM0000',
  'https://www.melon.com/chart/month/index.htm?classCd=AB0000',
]

def get_reverse_songs(url):
  # url을 통해 soup 가져오기
  req = requests.get(url, headers=header_user)
  html = req.text
  soup = BeautifulSoup(html, 'html.parser')
  chart = soup.select('tbody tr')
  
  filtered_chart = []
  for item in chart:
    # 순위가 상승한 곡인지 판별
    # 급상승 기준: 최소 10위 상승
    up = item.select_one('.up')
    if up == None or int(up.text) < 10 : continue
    
    # 곡 정보 가져오기
    rank = item.select_one('.rank').text.strip()
    title = item.select_one('.rank01 a').text.strip()
    artist = item.select_one('.rank02 span').text.strip()

    new_item = {
      'rank': rank,
      'title': title,
      'artist': artist,
      'up': up.text
    }
    filtered_chart.append(new_item)
  return filtered_chart

reverse_charts = [None] * 3
user_choice = 0
can_choice = [1, 2, 3, 999]
part = ['장르종합', '국내종합', '해외종합']
while(user_choice != 999):
  print('월간 역주행 곡')
  print('[1] 장르종합 | [2] 국내종합 | [3] 해외종합 | [999] 종료')
  user_choice = int(input('원하시는 차트를 선택해주세요 > '))

  # 유저 선택이 맞는지 확인
  if not user_choice in can_choice:
    print('\n\n!! 정확한 메뉴만 눌러주세요 !!\n\n')
    continue
  
  # 999면 종료
  if user_choice == 999: break
  
  # 사용하기 편하도록 유저 선택에서 1빼기
  user_choice -= 1

  # 유저가 선택한 차트의 데이터가 없으면 가져오기
  if not reverse_charts[user_choice]:
    print(f'\n⚙︎ {part[user_choice]} 데이터 가져오는 중 ⚙︎\n')
    reverse_charts[user_choice] = get_reverse_songs(url_list[user_choice])

  # 유저 선택에 따라 
  print(f'\n\n[[{part[user_choice]}]]')
  for item in reverse_charts[user_choice]:
    print(f'🔺{item['up']} [{item['rank']}] {item['title']} - {item['artist']}')
  print()