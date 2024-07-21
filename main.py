import os
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time

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
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "start-text"))).click()
        #Wait for the evaluation to be finished
        time.sleep(45)
        self.down = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)
        return self.down, self.up

    def tweet_at_internet_provider(self):
        self.driver.get("https://x.com/i/flow/login")
        time.sleep(2)
        email_field = self.driver.find_element(By.NAME, "text")
        email_field.send_keys(os.getenv("XEMAIL"))
        email_field.send_keys(Keys.ENTER)

        time.sleep(2)

        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(os.getenv("XPASS"))
        password_field.send_keys(Keys.ENTER)

        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click()
        time.sleep(1)
        text_box = self.driver.find_element(By.CLASS_NAME, "public-DraftEditor-content")
        text_box.send_keys(f"Hey, @comcast why is my internet speed {self.down}down/{self.up}up when I'm paying for more than that?")
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]').click()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if bot.down < PROMISED_DOWN or bot.up < PROMISED_UP:
    bot.tweet_at_internet_provider()
