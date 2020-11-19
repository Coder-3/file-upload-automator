from selenium import webdriver
import credentials

PATH = "/Users/cedricquenette/code/hbk/file-upload-automator/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://duluxpowders.com.au/login/?redirect_to=https://duluxpowders.com.au/#sign_in")