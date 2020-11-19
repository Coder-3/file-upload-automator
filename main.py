from selenium import webdriver
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import hidden
import filenames
import time
import os

PATH = "/Users/cedricquenette/code/hbk/file-upload-automator/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://duluxpowders.com.au/login/?redirect_to=https://duluxpowders.com.au/#sign_in")

username = driver.find_element_by_id("input_24_2")
username.clear()
username.send_keys(hidden.username)

password = driver.find_element_by_id("input_24_3")
password.clear()
password.send_keys(hidden.password)

driver.find_element_by_id("gform_submit_button_24").click()

time.sleep(2)

driver.get("https://duluxpowders.com.au/wp-admin/edit.php?post_type=product")

postSearch = driver.find_element_by_id("post-search-input")
postSearch.clear()
postSearch.send_keys('Duralloy RapidCure')

driver.find_element_by_id("search-submit").click()

productNames = driver.find_elements_by_class_name("row-title")
productNames[1].click()

currentProduct = driver.find_element_by_id("title").get_attribute("value")
matchedProduct = process.extractOne(currentProduct, filenames.filenamesArray)

print(currentProduct)
print(matchedProduct[0])

driver.find_elements_by_class_name("acf-button")[1].click()

driver.find_element_by_id("media-search-input").send_keys(matchedProduct[0])

time.sleep(2)

driver.find_element_by_class_name("thumbnail").click()

driver.find_element_by_class_name("media-button-select").click()

# driver.quit()