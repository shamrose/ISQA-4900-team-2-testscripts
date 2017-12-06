import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class KDuong_Payment(unittest.TestCase):
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
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[1]/ul/li[3]/a").click()                     #click on Shopping Cart
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[1]/ul/li[2]/a").click()              #click on a Subject
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/a[2]").click()            #click on Subject Again
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div/form/input[3]").click()                  #Click on add to cart
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[3]/p[2]/a[2]").click()                     #Check Out
        time.sleep(2)
        elem = driver.find_element_by_id("id_first_name")
        elem.send_keys("George")
        elem = driver.find_element_by_id("id_last_name")
        elem.send_keys("Royce")
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("szm.makandar@gmail.com")
        elem = driver.find_element_by_id("id_address")
        elem.send_keys("123 Pacific Street")
        elem = driver.find_element_by_id("id_postal_code")
        elem.send_keys("68156")
        elem = driver.find_element_by_id("id_city")
        elem.send_keys("Omaha")

        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[3]/form/p[7]/input").click()            #Click on Place Order
        time.sleep(2)
        driver.get("https://group2e-learning.herokuapp.com/payment/process/")                               #Paypal
        time.sleep(2)



        assert "Add item to shopping cart then browse again"
        '''
        driver.find_element_by_xpath("//*[@id="content"]/form/input[12]").click()
        driver.get("https://www.sandbox.paypal.com/webapps/hermes?token=6AG62038W60798225&useraction=commit&mfid=1512351756149_c0506f0c9646a#/checkout/login")
        elem = driver.find_element_by_id("email.hasHelp.validate.validateEmpty")
        sleep.time(2)
        elem.send_keys("elearningsteam2-buyer@gmail.com")
        elem = driver.find_element_by_id("password.hasHelp.validateEmpty.pin-password")
        sleep.time(2)
        elem.send_keys("elearning@2017")
        elem = driver.find_element_by_xpath("//*[@id="btnLogin"]").click()
        sleep.time(2)
        elem = driver.find_element_by_xpath("//*[@id="confirmButtonTop"]").click()
        sleep.time(2)
        elem = driver.find_element_by_xpath("//*[@id="merchantReturnBtn"]").click()
        sleep.time(2)
        driver.get("https://group2e-learning.herokuapp.com/")
        '''



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()