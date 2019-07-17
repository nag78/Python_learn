

from selenium import webdriver


browser = webdriver.Firefox(executable_path=r'C:\gecko\geckodriver.exe')
type(browser)
browser.get('http://inventwithpython.com')

# Поиск объекта на странице
try:
    elem = browser.find_element_by_class_name('card-img-top')
    print('Найден элемент <%s> с данным именем класса!' % (elem.tag_name))
except:
    print('Не удалось найти элемент с данным именем класса.')
# Имитация клика мыши
linkElem = browser.find_element_by_link_text('Read for Free')
type(linkElem)
linkElem.click()

# Заполнение полей
browser.get('http://gmail.com')
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys = ('fake_email@gmail.com')
emailElem.submit()
passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('123456')
passwordElem.submit()
