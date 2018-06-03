import unittest
from selenium import webdriver
import os
import os.path
import time
import HTMLTestRunner

class SearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_driver_path =os.path.join("C:\Anaconda","chromedriver.exe")
        cls.driver = webdriver.Chrome(chrome_driver_path)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://www.baidu.com/")

    def test_search_by_category(self):
        elem = self.driver.find_element_by_xpath("//*[@id='kw']")
        elem.send_keys("今日热点")
        elem = self.driver.find_element_by_xpath("//*[@id='su']")
        elem.click()
        self.assertEqual("百度一下",elem.get_attribute("value"))

        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
