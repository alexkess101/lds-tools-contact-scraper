# Activate venv
# source bin/activate
#
# Deactivate venv
# deactivate

from selenium import webdriver
from time import sleep
from credentials import *
PATH = "/usr/local/bin/chromedriver.exe"

class script():
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://www.churchofjesuschrist.org/?lang=eng")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/header/div[2]/div/ul/li[2]").click()
        self.driver.find_element_by_xpath("//a[contains(text(), 'Sign In')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath('//input[@type="submit"]').click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath('//input[@type="submit"]').click()
        sleep(2)
        # self.driver.find_element_by_xpath("/html/body/div[2]/header/div[2]/div/ul/li[2]").click()
        # self.driver.find_element_by_xpath("//a[contains(text(), 'Ward Directory and Map')]").click()
        self.driver.get("https://directory.churchofjesuschrist.org/")
        sleep(3)

    def getInfo(self, index):
        dataList = []
        links = self.driver.find_elements_by_class_name("ListingEntry__HouseholdEntry-sc-1tjfxc9-0")
        # for link in links:
        dataItem = {}
        links[index].click()
        sleep(1)
        dataItem["name"] = self.driver.find_element_by_class_name("Page__Heading-r1ca7-6").text
        dataItem["number"] = self.driver.find_element_by_class_name("bspPTM").text #all items have this class
        dataList.append(dataItem)
        print(dataList)
        self.driver.find_element_by_xpath("/html/body/div[2]/churchofjesuschrist-eden-normalize/main/div/section/div[2]/section/button").click()
        sleep(1)



bot = script(username, password)
