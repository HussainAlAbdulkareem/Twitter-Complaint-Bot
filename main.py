from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

PROMISED_DOWN = 150
PROMISED_UP = 10

load_dotenv()


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(By.CLASS_NAME, "start-text").click()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
