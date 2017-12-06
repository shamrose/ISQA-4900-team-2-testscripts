import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class KDuong_Updating_Item_Cart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_assignment3(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://group2e-learning.herokuapp.com/")
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[1]/ul/li/a").click()
        time.sleep(5)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(5)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        driver.get("https://group2e-learning.herokuapp.com/course/")
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[1]/ul/li[3]/a").click()                     #click on Shopping Cart
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[1]/ul/li[2]/a").click()             #click on Advance Django
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/a[2]").click()                     #click on Advance Django again
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div/form/input[3]").click()              #click on Add to Cart
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[3]/p[2]/a[1]").click()                         #click Browse Other Courses
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[1]/ul/li[3]/a").click()             #click on Advance Python
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/a[2]").click()              #click on Advance Python again
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div/form/input[3]").click()              #Click Add to Cart
        time.sleep(5)
        elem = driver.find_element_by_id("id_quantity")                                                 #Change quantity of Advance Django to 2
        elem.send_keys("2")
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[1]/td[3]/form/input[2]").click()  #Click on Saving the Item

        elem = driver.find_element_by_xpath("/html/body/div[3]/p[2]/a[1]").click()                      #Browse other courses
        time.sleep(10)

        assert "Add another item then Update another Item and Browse Again"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()