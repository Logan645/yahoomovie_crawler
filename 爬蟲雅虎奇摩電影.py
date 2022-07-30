import requests
from bs4 import BeautifulSoup
url="https://movies.yahoo.com.tw/movie_thisweek.html"
response=requests.get(url) #取得網頁內容
# print(response.text) 得到網頁html原始碼
soup=BeautifulSoup(response.text, 'html.parser') #建立beautifulsoap物件
info_items= soup.find_all('div','release_info')
# print(info_items) 得到一個list
# for item in info_items:
#     name=item.find('div','release_movie_name').a.text.strip()
#     english_Name = item.find('div', 'en').a.text.strip()
#     release_date= item.find('div','release_movie_time').text.split('：')[-1].strip()
#     expectation=item.find('div','leveltext').span.text.strip()
#     print('{}{}；上映日：{}；期待度：{}'.format(name,english_Name,release_date,expectation))

import csv
with open("本週新片.csv",'w',encoding='utf-8') as file:
    csv_writer=csv.writer(file)
    csv_writer.writerow(['電影片名','電影英文名','上映時間','網友期待度'])
    for item in info_items:
        name=item.find('div','release_movie_name').a.text.strip()
        english_Name = item.find('div', 'en').a.text.strip()
        release_date= item.find('div','release_movie_time').text.split('：')[-1].strip()
        expectation=item.find('div','leveltext').span.text.strip()
        csv_writer.writerow([name, english_Name, release_date, expectation])




