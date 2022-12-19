'''
  * 웹 크롤링
    - 웹 페이지에 있는 데이터를 요청하여 가져오는 방법 활용
    - request, bas4 라이브러리 활용
        - beautifulsoup4(bs4)
            - HTML source에서 tag별 계층 구조 parse
              tree 형태로 변환해주는 라이브러리이다.
            - 손 쉽게 HTML source에서 원하는 정보를 추출할 수 있다.
                - find(), find_all() 함수를 이용하면 원하는 tag 속성에 맞는
                  모든 정보를 가져올 수 있다.
    - 날짜 추출
      - td 태그 중 원하는 정보만을 따로 가져와야 한다.
      - 날짜 태그 규칙 찾아서 td 태그들 중에 날짜를 가져옴


    - 해당 페이지의 page source를 직접 가져옴
    - 웹 페이지 우클릭 "페이지(프레임) 소스 보기"로 같은 HTML 소스를 볼 수 있다.
    - 마우스 우클릭을 하면 "검사" 기능 활용
'''


page_no = 1
page_url =f"https://finance.naver.com/sise/sise_index_day.naver?code=KPI200&page={page_no}"
#print(page_url)

import requests
source = requests.get(page_url).text

import bs4
source = bs4.BeautifulSoup(source)


dates = source.find_all("td", class_ = "date")
#print(result)
#print(dates)
#print()
#print(dates[0])
#print(dates[0].text)


# 날짜 크롤링
date_list = []
for date in dates:
  date_list.append(date.text)

#print(date_list)


print()
# 체결가 크롤링(추출)

dates_pirce = source.find_all("td", class_ = "number_1")
#print(dates_pirce)
#print(dates_pirce[::4])
price_list = []
for price in dates_pirce:
  price_list.append(price.text)
    
print(price_list[::4])

'''
  체결가 변동량(천주) 거래량(천주) 거래대금(백만)들도 같은 태그(number_1)를 공유하고 있는 것을
  4개씩 증가하는 것을 알 수 있다.
  4의 배수로 건너뛰면서 추출하면 바로 체결가만 가져올 수 있다.
'''
price = source.find_all("td", class_ = "number_1")
price1_list = []
for price in dates_pirce[::4]:
  price1_list.append(price.text)

print(price1_list)

#print(len(date_list))
#print(len(price1_list))


result = source.find_all("td", class_="pgRR")[0]
#print(result)

last_url = source.find_all("td", class_="pgRR")[0].find_all("a")[0]["href"]
#print(last_url)

result = last_url.split('&page=')
#print(result)

last_page = last_url.split('&page=')[-1]
#print(last_page)

last_page = int(last_url.split('&page=')[-1])
print(last_page)