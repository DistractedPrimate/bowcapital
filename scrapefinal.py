from selenium import webdriver
from bs4 import BeautifulSoup
import time
from bs4.element import Tag
from selenium.webdriver.common.keys import Keys
import csv
import os

os.chdir("/Users/max/desktop")

driver = webdriver.Chrome('/Users/max/desktop/chromedriver')
google_query = 'site:linkedin.com/in/ AND "UC Santa Barbara" AND "Founder"'
driver.get('https://www.google.com/')
time.sleep(5)
search_bar = driver.find_element_by_name('q')
search_bar.send_keys(google_query)
search_bar.send_keys(Keys.RETURN)
time.sleep(3)

links = []
page = 0
while page < 2:

    soup = BeautifulSoup(driver.page_source,'lxml')
    result_div = soup.find_all('div', attrs={'class': 'g'})


    for r in result_div:
        # Checks for link
        try:
            link = r.find('a', href=True)
            

            # Check to for link then appends
            if link != '':
                links.append(link['href'])
                
        # Next loop if one element is not present
        except Exception as exception:
            print(exception)
            continue
    driver.find_element_by_link_text("Next").click()
    time.sleep(3)
    page = page +1

with open("linkedinlinks.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows([[link] for link in links])


print(type(links))
print(links)

driver.quit()
