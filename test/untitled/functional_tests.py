from selenium import webdriver

driver=webdriver.Chrome()
driver.get('http//localhost:8000')
#driver.get('https://www.baidu.com')
assert 'Django' in driver.title