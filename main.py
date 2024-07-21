from selenium import webdriver
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
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        return self.down, self.up


bot = InternetSpeedTwitterBot()
print(bot.get_internet_speed())
