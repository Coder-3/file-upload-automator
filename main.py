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

def search_products(product_line):
    driver.get("https://duluxpowders.com.au/wp-admin/edit.php?post_type=product")

    postSearch = driver.find_element_by_id("post-search-input")
    postSearch.clear()
    postSearch.send_keys(product_line)

    driver.find_element_by_id("search-submit").click()

def select_product(product_number):
    productNames = driver.find_elements_by_class_name("row-title")
    productNames[product_number].click()

def match_product():
    currentProduct = driver.find_element_by_id("title").get_attribute("value")
    matchedProduct = process.extractOne(currentProduct, filenames.filenamesArray)

    return matchedProduct

def upload_file():
    matchedProduct = match_product()[0]

    driver.find_elements_by_class_name("acf-button")[1].click()
    driver.find_element_by_id("media-search-input").send_keys(matchedProduct)

    time.sleep(2)

    driver.find_element_by_class_name("thumbnail").click()
    driver.find_element_by_class_name("media-button-select").click()

def update():
    driver.implicitly_wait(10)
    element = driver.find_element_by_class_name("is-active")

    if(element):
        time.sleep(4)
        return

def main():
    # pageNumber = 0
    # productNumber = 0
    login()
    time.sleep(2)
    for i in range(20):
        search_products("duralloy")
        select_product(i)
        try:
            upload_file()
        except:
            continue
        update()


main()
# driver.quit()