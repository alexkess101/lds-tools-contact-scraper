from selenium import webdriver
from time import sleep
from credentials import *
PATH = "/usr/local/bin/chromedriver.exe"

class script():
     def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://www.churchofjesuschrist.org/?lang=eng")
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[2]/header/div[2]/div/ul/li[2]").click()
        self.driver.find_element_by_xpath("//a[contains(text(), 'Sign In')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath('//input[@type="submit"]').click()
        sleep(1)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath('//input[@type="submit"]').click()
        sleep(2)
        mobile_menu_element = self.driver.find_element_by_xpath("/html/body/div[2]/header/div[3]/span[2]/span")
        desktop_menu_element = self.driver.find_element_by_xpath("/html/body/div[2]/header/div[2]/div/ul/li[2]")

        if mobile_menu_element:
            mobile_menu_element.click()
            self.driver.find_element_by_xpath("/html/body/div[2]/header/div[3]/span[2]/div/div[2]/a[3]").click()
        else:
            desktop_menu_element.click()
            self.driver.find_element_by_xpath("/html/body/div[2]/header/div[2]/div/ul/li[2]/div/div[2]/div[2]/div/div[2]/a[3]").click()
            
        sleep(3)


bot = script(username, password)


