import requests
from bs4 import BeautifulSoup

url = 'https://www.jobplanet.co.kr/job_postings/search?_rs_act=index&_rs_con=search&_rs_element=see_more_job_postings_bottom&query=%EA%B0%9C%EB%B0%9C%EC%9E%90'
default_url = 'https://www.jobplanet.co.kr'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

item = soup.select(".posting_name")
item_list = []
for href_list in item:
    href = href_list.get('href')
    href = href.replace("#", "")
    item_list.append(href)
    
test_url = default_url + item_list[0]
print(test_url)