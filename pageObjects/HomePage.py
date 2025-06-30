from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchResultsPage import SearchResultsPage


class HomePage:
    #locators
    lnk_myaccount_xpath = "//span[text()='My Account']"
    lnk_register_lnktext="Register"
    lnk_login_lnktext="Login"
    txt_searchbox_xpath="//input[@placeholder='Search']"
    btn_search_xpath="//div[@id='search']//button[@type='button']"

    #constructor
    def __init__(self,driver):
        self.driver=driver


    # Action methods
    def clickMyAccount(self):
        self.driver.find_element(By.XPATH,self.lnk_myaccount_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_register_lnktext).click()
        return AccountRegistrationPage

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_login_lnktext).click()
        return LoginPage

    def enterProductName(self,productname):
        self.driver.find_element(By.XPATH,self.txt_searchbox_xpath).send_keys(productname)

    def clickSearch(self):
        self.driver.find_element(By.XPATH,self.btn_search_xpath).click()
        return SearchResultsPage(self.driver)

    def isHomePageExists(self):
        try:
            return self.driver.title == "Your Store"
        except:
            return False
