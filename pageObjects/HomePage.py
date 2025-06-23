from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:
    #locators
    lnk_myaccount_xpath = "//span[text()='My Account']"
    lnk_register_lnktext="Register"
    lnk_login_lnktext="Login"

    #constructor
    def __init__(self,driver):
        self.driver=driver


    # Action methods
    def clickMyAccount(self):
        self.driver.find_element(By.XPATH,self.lnk_myaccount_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_register_lnktext).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_login_lnktext).click()
