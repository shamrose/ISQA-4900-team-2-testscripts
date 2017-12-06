import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Royalon(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ForgotPassword(self):
        driver = self.driver
        driver.get("http://group2e-learning.herokuapp.com/")
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[1]/ul/li/a").click()
        time.sleep(5)
        id_username = "nikki_2"
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(id_username)
        id_password = "Strawberryjam44"
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(id_password)
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/p[3]/input").click()
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/p[1]/a").click()
        time.sleep(5)
        id_email = "nochuba@yahoo.com"
        elem = driver.find_element_by_id("id_email")
        elem.send_keys(id_email)
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[2]/form/p[2]/input").click()
        time.sleep(10)


if __name__ == "__main__":
    unittest.main()