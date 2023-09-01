import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestOlx(unittest.TestCase):

    def test_driver_load(self):
        driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
        self.assertIsNotNone(driver)
        driver.quit()

    def test_olx_open(self):
        driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
        driver.get("https://www.olx.ua")
        self.assertEqual(driver.title, "OLX.ua - Купити та Продати в Україні")
        driver.quit()

    def test_cookies_load(self):
        driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
        driver.get("https://www.olx.ua")
        with open("data/cookies.txt", "r") as file:
            cookies = eval(file.read())
            for cookie in cookies:
                driver.add_cookie(cookie)
            time.sleep(2)
            self.assertTrue(driver.get_cookies())
        driver.quit()

    def test_ad_open(self):
        driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
        driver.get("https://www.olx.ua/obyavlenie/sample-ad-ID12345")
        self.assertEqual(driver.title, "Sample Ad - ID12345")
        driver.quit()

    def test_message_send(self):
        driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
        driver.get("https://www.olx.ua/obyavlenie/sample-ad-ID12345")
        message_field = driver.find_element(By.NAME, "message[message]")
        message_field.send_keys("Доброго Дня")
        message_field.send_keys(Keys.ENTER)
        time.sleep(2)
        message_container = driver.find_element(By.ID, "message-container")
        self.assertEqual(message_container.text, "Доброго Дня")
        driver.quit()


if __name__ == "__main__":
    unittest.main()