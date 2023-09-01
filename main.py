from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

COOKIES_FILE = "data/cookies.txt"

driver = webdriver.Chrome(executable_path="drivers/chromedriver_mac_arm64/chromedriver")

driver.get("https://www.olx.ua")

driver.get("https://www.olx.ua")
with open(COOKIES_FILE, "r") as file:
    cookies = eval(file.read())
    for cookie in cookies:
        driver.add_cookie(cookie)

time.sleep(2)

driver.get("https://www.olx.ua/obyavlenie/sample-ad-ID12345")

message_field = driver.find_element(By.NAME, "message[message]")
message_field.send_keys("Доброго Дня")
message_field.send_keys(Keys.ENTER)

driver.quit()
