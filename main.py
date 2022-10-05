import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import config

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/diana/chromedriver"
SERVICE = Service(CHROME_DRIVER_PATH)
TWITTER_EMAIL = config.twitter_email
TWITTER_PASSWORD = config.twitter_password
SPEEDTEST_URL = "https://www.speedtest.net/result/13762499492"


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver_path = webdriver.Chrome(service=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver_path.get(SPEEDTEST_URL)

        time.sleep(3)
        go_button = self.driver_path.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()

        time.sleep(60)
        self.up = self.driver_path.find_element(By.XPATH,
                                                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver_path.find_element(By.XPATH,
                                                  '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"up: {self.up}")
        print(f"up: {self.down}")

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot(SERVICE)
bot.get_internet_speed()
bot.tweet_at_provider()
