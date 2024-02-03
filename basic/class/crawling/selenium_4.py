from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

# 유저 정보 넣기
user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
options.add_argument(f'user-agent={user}')

# 자동 종료 해제 옵션
options.add_experimental_option('detach', True)

# 화면 크기 설정
# options.add_argument('--start-maximized')
# options.add_argument('--start-fullscreen)
# options.add_argument('window-size=200, 500')

# 브라우저 화면이 나오지 않게 하기
# options.add_argument('--headless')

# 상단 - 조작되고 있다는 메시지를 지우는 옵션
options.add_experimental_option('excludeSwitches', ['enable-automation'])

# 음소거 옵션
options.add_argument('--mute-audio')

# 시크릿 모드
options.add_argument('incognito')

driver = webdriver.Chrome(options=options)

url = 'http://naver.com'
driver.get(url)
print(len(driver.page_source))