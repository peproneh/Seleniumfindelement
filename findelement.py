from selenium import webdriver

f = open("locators.txt", "r", encoding=('utf-8'))
url = f.readline()[9:]
driver = webdriver.Chrome('C:\Peproneh Autmation tools\Selenium\chromedriver_win32\chromedriver.exe')
driver.get(url)

id_selector = str(f.readline())[9:-1]
id_elm = driver.find_element_by_id(id_selector)
assert id_elm.get_attribute("name") == "continue", "Id_elm name fail"
print("id_elm name:   " + id_elm.get_attribute("name"))

name_selector = str(f.readline())[9:-1]
name_elm = driver.find_element_by_name(name_selector)
assert name_elm.get_attribute("name") == "username", "name_elm name fail"
print("name_elm name: " + name_elm.get_attribute("name"))

css_selector = str(f.readline())[9:-1]
css_elm = driver.find_element_by_css_selector(css_selector)
assert css_elm.text == "Site content goes here.", "scc_elm text fail"
print("css_elm text:  " + css_elm.text)

xPath_selector = str(f.readline())[9:]
xPath_elm = driver.find_element_by_xpath(xPath_selector)
assert xPath_elm.get_attribute("id") == "loginForm", "xPath_elm ID fail"
print("xPath_elm ID:  " + xPath_elm.get_attribute("id"))

f.close()
driver.quit()
