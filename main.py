from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import hidden
import filenames
import time
import os

PATH = "/Users/cedricquenette/code/hbk/file-upload-automator/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://duluxpowders.com.au/login/?redirect_to=https://duluxpowders.com.au/#sign_in")

def login():
    username = driver.find_element_by_id("input_24_2")
    username.clear()
    username.send_keys(hidden.username)

    password = driver.find_element_by_id("input_24_3")
    password.clear()
    password.send_keys(hidden.password)
    
    driver.find_element_by_id("gform_submit_button_24").click()

def search_products(pageNumber):
    driver.get("https://duluxpowders.com.au/wp-admin/edit.php?orderby=title&order=asc&s=precious&post_status=all&post_type=product&m=0&layout=5e617bd96816a&action=-1&paged=" + str(pageNumber) + "&action2=-1")

    # postSearch = driver.find_element_by_id("post-search-input")
    # postSearch.clear()
    # postSearch.send_keys(product_line)

    # driver.find_element_by_id("search-submit").click()

def select_product(productNumber):
    productNames = driver.find_elements_by_class_name("row-title")
    productNames[productNumber].click()

def match_product():
    currentProduct = driver.find_element_by_id("title").get_attribute("value")
    matchedProduct = process.extractOne(currentProduct, filenames.filenamesArray)

    return matchedProduct

def upload_file():
    matchedProduct = match_product()

    try:
        driver.find_elements_by_class_name("acf-button")[1].click()
    except:
        return
    driver.find_element_by_id("media-search-input").send_keys(matchedProduct[0])

    time.sleep(2)

    driver.find_element_by_class_name("thumbnail").click()
    driver.find_element_by_class_name("media-button-select").click()

def update():
    driver.implicitly_wait(10)
    element = driver.find_element_by_class_name("is-active")

    if(element):
        time.sleep(5)
        return

def steps(pageNumber, productNumber):
    search_products(pageNumber)
    select_product(productNumber)
    productNumber += 1
    try:
        upload_file()
    except:
        time.sleep(10)
        return
    time.sleep(10)

login()

time.sleep(2)

for i in range(9, 20):
    steps(2, i)

# driver.quit()