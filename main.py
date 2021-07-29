import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
web_driver_path = "./chromedriver.exe"
competitor_id = "instagram"


class InstaFollowerBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=web_driver_path)
        self.list_to_be_followed = []

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        username_box = self.driver.find_element_by_name("username")
        username_box.send_keys(username)
        password_box = self.driver.find_element_by_name("password")
        password_box.send_keys(password + Keys.ENTER)

    def get_following(self, id_followers):
        search_box = self.driver.find_element_by_css_selector("input.XTCLo.x3qfX")
        search_box.send_keys(id_followers)
        time.sleep(2)
        search_box.send_keys(Keys.ENTER + Keys.ENTER)
        time.sleep(3)
        following = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/'
                                                      'section/ul/li[3]/a')
        following.click()
        body = self.driver.find_element_by_tag_name("body")
        following_list = []
        time.sleep(2)
        print(len(self.driver.find_elements_by_css_selector("div.PZuss li")))
        while len(following_list) < len(self.driver.find_elements_by_css_selector("div.PZuss li")):
            following_list = self.driver.find_elements_by_css_selector("div.PZuss li")
            body.send_keys(Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.END)
            time.sleep(3)
        self.list_to_be_followed = following_list

    def follow_following(self):
        for insta_account in self.list_to_be_followed:
            follow_button = insta_account.find_element_by_tag_name("button")
            try:
                follow_button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()


bot = InstaFollowerBot()
bot.login(USERNAME, PASSWORD)
time.sleep(3)
bot.get_following(competitor_id)
bot.follow_following()

