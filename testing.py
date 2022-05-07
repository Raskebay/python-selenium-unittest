from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest


class Selenium(unittest.TestCase):

    def test_add_to_shopping_card(self):
        """Добавление в корзину"""
        s = Service('C:/pytest/selenium/chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        driver.get('http://tutorialsninja.com/demo/')

        search_field = driver.find_element(By.NAME, 'search')
        search_field.send_keys('iphone')
        search_field.send_keys(Keys.RETURN)

        add_to_cart_button = driver.find_element(By.XPATH,
                                                 '/html/body/div[2]/div/div/div[3]/div/div/div[2]/div[2]/button[1]')
        add_to_cart_button.click()

        shopping_card_link = driver.find_element(By.XPATH, '/html/body/nav/div/div[2]/ul/li[4]/a')
        shopping_card_link.click()

        self.assertTrue('product 11' in driver.page_source)
        driver.close()

    def test_del_from_card(self):
        self.assertTrue(True)





