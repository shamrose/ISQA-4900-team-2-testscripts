import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Coupon(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_assignment3(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://group2e-learning.herokuapp.com/")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[1]/ul/li/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        time.sleep(2)
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        driver.get("https://group2e-learning.herokuapp.com/course/")
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[1]/ul/li[3]/a").click()                     #click on Shopping Cart
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[1]/ul/li[2]/a").click()              #click on a Subject
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/a[2]").click()            #click on Subject Again
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div/form/input[3]").click()                  #Click on add to cart
        time.sleep(5)
        elem = driver.find_element_by_id("id_code")
        elem.send_keys("study123")
        elem = driver.find_element_by_xpath("/html/body/div[3]/form/input[2]").click()
        time.sleep(10)



        assert "Add item to shopping cart then browse again"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()