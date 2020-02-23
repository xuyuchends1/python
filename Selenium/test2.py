import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
    def test_search_in_python_org(self):
        driver = webdriver.Firefox()
        driver.get("https://www.baidu.com/")
        assert "百度一下，你就知道" in driver.title
        elem = driver.find_element_by_name("wd")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        driver.close()

    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()
