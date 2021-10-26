# 웹크롤링 - 다음뉴스

import requests

from bs4 import BeautifulSoup

# requests - 웹사이트 코드 복사 GET
# BeutifulSoup4 - requests get 해온 코드에서 필요한 정보만 find해서 가져오기

url = 'https://news.v.daum.net/v/20211021152915953'
result = requests.get(url)
# print(result.text)

doc = BeautifulSoup(result.text, 'html.parser')
# title = doc.select('h3.tit_view') # list type 지우기
# title2 = doc.select('h3.tit_view')[0] 지우기
title = doc.select('h3.tit_view')[0].get_text()
contents = doc.select('section p')
contents.pop(-1) # 기자 정보 삭제, remove와의 차이 숙지!(시험)



content = '' # 본문 총합, 0초기화
for info in contents:
    content += info.get_text()

print('#############################')
print('# 뉴스 제목: {}'.format(title))
print('#############################')
print('# 뉴스 본문: {}'.format(content))