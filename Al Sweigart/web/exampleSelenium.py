from selenium import webdriver


browser = webdriver.Firefox(executable_path=r'C:\gecko\geckodriver.exe')
type(browser)
browser.get('http://inventwithpython.com')
