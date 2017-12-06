import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class assignment3Search (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_add_new_investment(self):
        driver = self.driver
        driver.maximize_window ()
        driver.get ("http://group2e-learning.herokuapp.com/admin/login")
        elem = driver.find_element_by_id ("id_username")
        elem.send_keys ('cuijing')
        time.sleep (3)
        elem = driver.find_element_by_id ("id_password")
        elem.send_keys ('jian7688')
        time.sleep (3)
        elem.send_keys (Keys.RETURN)
        assert "Log in | Django site admin"
        time.sleep (3)

        # Test how to create a new course as a instructor
        driver.get ("http://group2e-learning.herokuapp.com/course/create/")
        self.assertIn ("Create a new course", driver.title)
        elem = driver.find_element_by_id ("id_subject")
        elem.send_keys ('Advanced Python')
        time.sleep (2)
        elem = driver.find_element_by_id ("id_title")
        elem.send_keys ('Test Python Class ')
        time.sleep (2)
        elem = driver.find_element_by_id ("id_slug")
        elem.send_keys ('python_3')
        time.sleep (2)
        elem = driver.find_element_by_id ("id_overview")
        elem.send_keys ('This course will introduce how to install Python on Windows 10 and on Mac.')
        time.sleep (2)
        driver.find_element_by_xpath ("html/body/div[2]/div/form/p[5]/input").click ()
        time.sleep (2)

        # Test how to how to edit course modules as the same instructor
        driver.get ("http://group2e-learning.herokuapp.com/course/mine/")
        self.assertIn ("My courses", driver.title)
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/p/a[3]").click()
        time.sleep(5)
        elem = driver.find_element_by_id ("id_modules-0-title")
        elem.send_keys ('How to work with lists and tuples')
        time.sleep (5)
        elem = driver.find_element_by_id ("id_modules-0-description")
        elem.send_keys ('Describe how an item in a list is accessed.')
        time.sleep (5)
        driver.find_element_by_xpath ("/html/body/div[2]/div/form/input[22]").click ()

        time.sleep (5)

    def tearDown(self):
        self.driver.close ()


if __name__ == "__main__":
    unittest.main ()
