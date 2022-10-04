from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import config

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/diana/chromedriver"
SERVICE = Service(CHROME_DRIVER_PATH)
TWITTER_EMAIL = config.twitter_email
TWITTER_PASSWORD = config.twitter_password


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver_path = webdriver.Chrome(service=SERVICE)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()



