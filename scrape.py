
#import
import time

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from parsel import selector
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('/Users/max/desktop/chromedriver')

#navigate to LinkedIn
#driver.get('https://www.linkedin.com/school/ucsantabarbara/people/')
#driver.get('https://www.linkedin.com')
#Login to LinkedIn
"""
username = driver.find_element_by_class_name('login-email')
username.send_keys('m_medearis@ucsb.edu')
time.sleep(0.5)
password = driver.find_element_by_class_name('login-password')
password.send_keys('LSVPgDUeEgzuh4D') 
time.sleep(0.5)
log_in_button = driver.find_element_by_id('login-submit')
log_in_button.click()
time.sleep(5)
"""
#Navigate to Google

driver.get('https://www.google.com/')
time.sleep(5)
search_bar = driver.find_element_by_name('q')
search_bar.send_keys('site:linkedin.com/in/ AND "UC Santa Barbara" AND "Founder"')
search_bar.send_keys(Keys.RETURN)
time.sleep(5)

#Find LinkedIn URLS
x = 0
while x < 2:
    linkedin_urls = []
    linkedin_urls += driver.find_elements_by_class_name('iUh30 bc rpCHfe')
    linkedin_urls = [url.text for url in linkedin_urls]
    driver.find_element_by_link_text("Next").click()
    #driver.find_element_by_xpath("//*[contains(local-name(), 'span') and contains(text(), 'Next')]").click()
    for linkedin_url in linkedin_urls:
        print(linkedin_url)
    time.sleep(5)
    x = x + 1

   
print(linkedin_urls)


#iterate thru and scrape
"""print("\n")
for linkedin_url in linkedin_urls:
    print(linkedin_url.text)"""
    





















driver.quit()