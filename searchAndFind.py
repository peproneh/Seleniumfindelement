from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

f = open("resourses/SAF_Locators.txt", "r")
resources = f.readlines()
resourcesMAP = {}
for line in resources:
    delimiter_index = line.find(':')
    key = line[:delimiter_index].strip()
    value = line[delimiter_index + 1:-1].strip()
    resourcesMAP[key] = value

url = resourcesMAP['url']
driver = webdriver.Chrome('resourses/chromedriver.exe')
# opens page
driver.get(url)
search_box_id = resourcesMAP['search_box_id']
searchBox = driver.find_element_by_id(search_box_id)

searchText = resourcesMAP['search']
while '  ' in searchText:
    #if there are two spaces, replace with one
    searchText = searchText.replace("  ", " ")

searchBox.send_keys(searchText)
searchBox.send_keys(Keys.ENTER)

result_list = driver.find_elements(By.CLASS_NAME, resourcesMAP['result_list_class'])
for span in result_list:

    try:
        assert searchText.upper() in span.text.upper(), "There is an extra result"
    except AssertionError as e:
        print(e)

f.close()
driver.quit()
