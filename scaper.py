import requests
import pandas as pd
from bs4 import BeautifulSoup
URL = "https://www.careerguide.com/career-options"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
#print(soup.prettify())
final=[]
jobs=soup.find_all('ul',attrs = {'class':'c-content-list-1 c-theme c-separator-dot'})

for j in range(len(jobs)):
    job=[jobs[j].find_all('li')[i].a['title'] for i in range(len(jobs[j].find_all('li')))]
    final+=job
print(final)

j=final[182]

URL = "https://www.linkedin.in/jobs/search/?keywords={j}"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

import re
def xtract(l):
    x=[]
    for i in l:
        t=re.sub(r"[\n\t]*", "", (i.a.text))
        x.append(t.strip())
    return x
    
job_titles=[re.sub(r"[\n\t]*", "", (x.text)).strip() for x in(soup.find_all('h3',{'class':'base-search-card__title'}))]
companies=xtract(soup.find_all('h4',{'class':'base-search-card__subtitle'}))
locations=[re.sub(r"[\n\t]*", "", (x.text)).strip() for x in (soup.find_all('span',{'class':'job-search-card__location'}))]

res=pd.DataFrame()
res['job_titles']=job_titles
res['companies']=companies
res['locations']=locations

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
PATH='C:\Program Files (x86)\chromedriver.exe'
c=companies[0]
driver=webdriver.Chrome(PATH)
URL = "https://www.linkedin.in/company/microsoft/"
driver.get(URL)
sleep(4)
about=driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div/section[1]/div/p').text
size = driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div/section[1]/div/dl/div[3]/dd').text
hq = driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div/section[1]/div/dl/div[4]/dd').text
print(about)
print(size)
print(hq)
