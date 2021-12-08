from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(6)


driver.get("http://192.168.1.1")

if driver.title == "Privacy error":
    print(driver.title)
    btn = driver.find_element_by_id("details-button")
    btn.click()
    driver.find_element_by_id("proceed-link").click()

username = driver.find_element_by_id("index_username")
username.send_keys("admin")

pw = driver.find_element_by_id("password")
pw.send_keys("2333185a")

loginbtn = driver.find_element_by_id("loginbtn")
loginbtn.click()
time.sleep(2)


driver.get("https://192.168.1.1/html/advance.html#device_mngt")


reboot = driver.find_element_by_id("rebootId").click()
sure = driver.find_element_by_id("dev_mngt_modal_id_ok").click()

time.sleep(2)
driver.quit()
