
from selenium import webdriver
import unittest

class NewVistorTest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Chrome()
        self.browser.get('http://localhost:8000')
    def tearDown(self):
        self.browser.quit()

    def test_1(self):
        self.assertIn("Django",self.browser.title)

if __name__=='__main__':
    unittest.main()