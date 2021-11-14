'''Tema 9 - pct 1 -https://duckduckgo.com/'''

'''Pct 1
1. Open https://duckduckgo.com/
2. check the duck duck image is displayed on page (poza  cu rata mare)
3. Write "python" in search field
4. Click on search button
 take first title  (exemplu Start Programming With Python - Start Learning Today )
 daca title contine in primul title ("python") - printeaza titlul
 faceti clear la fieldul de search
 scrieti "dog" in fieldul de search
 press enter'''

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('C:\\Users\\Larisa\\PycharmProjects\\Automation_IT_Factory_Curs\\chromedriver.exe')
import time

driver.get('https://duckduckgo.com/')
search_logo = driver.find_element(By.ID,'logo_homepage_link')
time.sleep(2.0)
search_field = driver.find_element(By.ID,'search_form_input_homepage')
time.sleep(2.0)
search_field.send_keys('python')
time.sleep(2.0)
search_find = driver.find_element(By.ID,'search_button_homepage')
search_find.click()
time.sleep(2.0)
'''search_result = driver.find_element(By.CSS_SELECTOR,'a.result__a.js-result-title-link')
search_result.find_elements_by_link_text()'''

search_field = driver.find_element(By.ID,'search_form_input')
search_field.clear()
time.sleep(2.0)
search_field.send_keys('dog')
time.sleep(2.0)
search_field = driver.find_element(By.ID,'search_button')
search_field.click()

time.sleep(3.0)
driver.close()