import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Elearning(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_assignment3(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://group2e-learning.herokuapp.com/")                                                           #Get the Group 2 E-learning URL
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div[2]/h3[1]/a").click()                                 #Select the button for subject to enroll
        time.sleep(2)                                             #Get the URL of the subject
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/a").click()                                          #Click the Register to Enroll button
        time.sleep(2)
        driver.get("https://group2e-learning.herokuapp.com/students/register/")                                         #Get the URL for Student to Register
        user = "shaun"                                                                                                    #Provide the User ID
        pwd = "sam@123"                                                                                                 #Provide the Password
        elem = driver.find_element_by_id("id_username")                                                                 #Find the Username field
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password1")                                                                #Find the Password field
        elem.send_keys(pwd)
        time.sleep(2)
        elem = driver.find_element_by_id("id_password2")                                                                #Find the confirm password field
        elem.send_keys(pwd)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/form/p[4]/input").click()                            #Click the Create Account button
        #elem.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.get("https://group2e-learning.herokuapp.com/students/courses/")                                          #Dashboard page
        time.sleep(2)
        driver.get("https://group2e-learning.herokuapp.com/")                                                           #Go to the Welcome page
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div[2]/h3[1]/a").click()                                 #Click the test subject button                                             #See the Overview of the course
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/form/input[3]").click()                              #Click the Enroll Now button
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div[1]/ul/li/a").click()                                 #Click on the modules to view the course
        time.sleep(5)
        assert "Enrolled in Course"
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
