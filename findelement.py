from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://phptravels.com/demo/"
# driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path=r"C:\Peproneh Autmation tools\Selenium\chromedriver_win32\chromedriver.exe")
page = driver.get(url)
element_id = driver.find_element_by_id("SiteNavContainer")
element_class = driver.find_element_by_class_name("marketing-nav--skin-light marketing-nav marketing-nav--primary")
#element_xPath = driver.find_element_by_xpath()
#element_cssSelector = driver.find_element_by_css_selector()