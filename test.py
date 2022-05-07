from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('C:/pytest/selenium/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('http://tutorialsninja.com/demo/')

search_field = driver.find_element(By.NAME, 'search')
search_field.send_keys('iphone')
search_field.send_keys(Keys.RETURN)

add_to_cart_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[2]/div[2]/button[1]')
add_to_cart_button.click()

shopping_card_link = driver.find_element(By.XPATH, '/html/body/nav/div/div[2]/ul/li[4]/a')
shopping_card_link.click()

assert 'product 11' in driver.page_source
driver.close()

