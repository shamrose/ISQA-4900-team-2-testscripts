import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class blog_Elearning(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    #Edit Course Information as Instructor
    def test_edit_course(self):
        user = "cuijing"
        pwd = "jian7688"
        driver = self.driver
        driver.maximize_window ()
        driver.get ("http://group2e-learning.herokuapp.com/admin/")
        elem = driver.find_element_by_id ("id_username")
        elem.send_keys (user)
        time.sleep(4)
        elem = driver.find_element_by_id ("id_password")
        elem.send_keys (pwd)
        time.sleep(4)
        elem.send_keys (Keys.RETURN)
        assert "My courses"
        time.sleep (4)
        driver.get ("http://group2e-learning.herokuapp.com/course/7/edit/")
        select = Select (driver.find_element_by_name ('subject'))
        select.select_by_visible_text ('Introduction to Django')
        time.sleep(4)
        elem = driver.find_element_by_id ("id_title")
        elem.clear()
        elem.send_keys ('What is Python')
        time.sleep (4)
        elem = driver.find_element_by_id ("id_slug")
        elem.clear()
        elem.send_keys ('Python_3')
        time.sleep (4)
        elem = driver.find_element_by_id ("id_overview")
        elem.clear()
        elem.send_keys ('this is the introduction of django')
        time.sleep (4)
        driver.find_element_by_xpath ('//*[@id="content"]/div/form/p[5]/input').click()

    #Create Account as Student
    def test_register(self):
        driver=self.driver
        driver.maximize_window ()
        driver.get ("http://group2e-learning.herokuapp.com/students/register/")
        time.sleep (4)
        elem = driver.find_element_by_id ("id_username")
        elem.send_keys("student8")
        time.sleep(4)
        elem = driver.find_element_by_id("id_password1")
        elem.send_keys ('student1234')
        elem = driver.find_element_by_id ("id_password2")
        elem.send_keys ('student1234')
        time.sleep (4)
        driver.find_element_by_xpath ('//*[@id="content"]/div/form/p[4]/input').click()
        assert "Sign up"

    def tearDown(self):
        self.driver.close ()

if __name__ == "__main__":
   unittest.main()