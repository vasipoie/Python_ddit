from selenium import webdriver  # 셀레니움을 활성화
from selenium.webdriver import ActionChains  # 액션체인 활성화
import time

dr = webdriver.Chrome()  # 크롬 드라이버를 실행하는 명령어를 dr로 지정
dr.get('https://topis.seoul.go.kr/map/openBusMap.do')  # 드라이버를 통해 url의 웹 페이지를 오픈
time.sleep(2)

act = ActionChains(dr)  # 드라이버에 동작을 실행시키는 명령어를 act로 지정

### 예시 ###
element1 = dr.find_element_by_css_selector('#mapContainer > div.aside > div > div.searchresult > ul > li:nth-child(2) > a')
act.click(element1).perform()  # element1  클릭 동작을 수행

content = dr.find_elements_by_xpath('//*[@id="my_tbody"]')
for cont in content:
    print(cont.text)
