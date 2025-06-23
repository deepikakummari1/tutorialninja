from selenium.webdriver.common.by import By


class AccountRegistrationPage:
    txt_firstname_name="firstname"
    txt_lastname_name="lastname"
    txt_email_name="email"
    txt_telephone_name="telephone"
    txt_password_name="password"
    txt_conpassword_name="confirm"
    chk_policy_name="agree"
    btn_con_xpath="//input[@type='submit']"
    txt_msg_con_xpath="//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self,driver):
        self.driver=driver


    def setFirstName(self,fname):
        self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.NAME,self.txt_lastname_name).send_keys(lname)

    def setEmail(self, email):
        self.driver.find_element(By.NAME, self.txt_email_name).send_keys(email)

    def setTelephone(self, tel):
        self.driver.find_element(By.NAME, self.txt_telephone_name).send_keys(tel)

    def setPassword(self, pwd):
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(pwd)

    def setConfirmPassword(self, cnfpwd):
        self.driver.find_element(By.NAME, self.txt_conpassword_name).send_keys(cnfpwd)

    def setPrivacyPolicy(self):
        self.driver.find_element(By.NAME, self.chk_policy_name).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.btn_con_xpath).click()

    def getconfirmationmsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_msg_con_xpath).text
        except:
            None

