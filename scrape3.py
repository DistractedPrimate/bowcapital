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
titles = []
descriptions = []
page = 0
while page < 29:

    soup = BeautifulSoup(driver.page_source,'lxml')
    result_div = soup.find_all('div', attrs={'class': 'g'})


    for r in result_div:
        # Checks if each element is present, else, raise exception
        try:
            link = r.find('a', href=True)
            title = None
            title = r.find('h3')

            if isinstance(title,Tag):
                title = title.get_text()

            description = None
            description = r.find('span', attrs={'class': 'st'})

            if isinstance(description, Tag):
                description = description.get_text()

            # Check to make sure everything is present before appending
            if link != '' and title != '' and description != '':
                links.append(link['href'])
                titles.append(title)
                descriptions.append(description)
        # Next loop if one element is not present
        except Exception as e:
            print(e)
            continue
    driver.find_element_by_link_text("Next").click()
    time.sleep(3)
    page = page +1

with open("linkedinlinks.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows([[link] for link in links])

#print(titles)
print(type(links))
print(links)
#print(descriptions)