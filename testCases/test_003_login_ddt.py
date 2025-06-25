import os.path
import time

from pageObjects.HomePage import HomePage
from pageObjects.MyaccountPage import MyAccountPage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import pytest


class Test_LoginDDT:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = os.path.abspath(os.getcwd()) + "\\testdata\\Tutorialninja_LoginData.xlsx"

    def test_login_ddt(self, setup):
        self.logger.info("********* Test Login DDT Started *********")
        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        lst_status = []
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("********* Launching Application *********")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.mp = MyAccountPage(self.driver)

        for r in range(2, self.rows + 1):
            self.hp.clickMyAccount()
            self.hp.clickLogin()

            self.email = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(2)

            self.targetpage = self.lp.isMyAccountPageExists()

            if self.exp== "Valid":
                if self.targetpage == True:
                    lst_status.append("Pass")
                    self.mp.clickLogout()

                else:
                    lst_status.append("Fail")


            elif self.exp== "Invalid":
                if self.targetpage == True:
                    lst_status.append("Fail")
                    self.mp.clickLogout()

                else:
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("********* Test Login DDT Finished *********")


