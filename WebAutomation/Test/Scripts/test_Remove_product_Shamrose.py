import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Remove_product_Shamrose(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_assignment3(self):
        user = "instructor"                                                                                             #Provide the Username
        pwd = "instructor1a"                                                                                            #Provide the Password
        driver = self.driver
        driver.maximize_window()
        driver.get("https://group2e-learning.herokuapp.com/")                                                           #Get the Heroku URL
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[1]/ul/li/a").click()                                        #Click on the Sign In Button
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")                                                                 #Get the username field
        elem.send_keys(user)
        time.sleep(5)
        elem = driver.find_element_by_id("id_password")                                                                 #Get the password field
        elem.send_keys(pwd)
        time.sleep(5)
        elem.send_keys(Keys.RETURN)
        driver.get("https://group2e-learning.herokuapp.com/course/")                                                    #Go to the course URL
        elem = driver.find_element_by_xpath("/html/body/div[1]/ul/li[3]/a").click()                                     #click on Shopping Cart
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[4]/a[2]").click()                             #click on Advance Django
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div/form/input[3]").click()                              #click on Add to Cart
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[3]/p[2]/a[1]").click()                                         #click Browse Other Courses
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[5]/a[2]").click()                             #click on Advance Python
        time.sleep(10)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div/form/input[3]").click()                              #Click on Add to Cart
        time.sleep(10)
        elem = driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[2]/td[4]/a").click()                      #Remove Advance Django
        time.sleep(20)

        assert "Remove An Item"


        time.sleep(20)

        assert "Remove Item"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()