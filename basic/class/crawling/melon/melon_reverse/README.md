# 🍈 Melon 월간 역주행곡 🔺
> BeautifulSoup을 사용해 [***장르종합***, ***국내종합***, ***해외종합***]차트의 월간 역주행곡(최소 10위 이상 상승)을 추출

### ⚠️ 주요 코드 
```python
def get_reverse_songs(url):
    ...

reverse_charts = [None] * 3
user_choice = 0

while(user_choice != 999):
    ...

  if not reverse_charts[user_choice]:
    print(f'\n⚙︎ {part[user_choice]} 데이터 가져오는 중 ⚙︎\n')
    reverse_charts[user_choice] = get_reverse_songs(url_list[user_choice])

    ...
```
> **`get_reverse_songs`**:  `url`을 통해 급상승 곡 리스트를 가져오는 함수
>
> 
> 앱 시작 시 모든 데이터를 추출하면 데이터 로딩 시간도 생기고 사용자가 궁금하지 않은 차트의 데이터를 가져오는 등의 낭비가 발생하기 때문에 사용자가 원하는 차트 선택 시 최초 한 번 해당 차트의 데이터를 추출하도록 설정

### ▶️ 실행 결과
<p align="center"><img width="50%" height="300px" alt="실행결과" src="https://github.com/newbission/oz_class/assets/155050120/c316bb14-314a-43a1-b087-0355fe2cdbde"></p>