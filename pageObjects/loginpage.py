from selenium.webdriver.common.by import By

class Login:
    txtbx_email_id = "Email"
    txtbx_password_id = "Password"
    btn_login_button = "//button[text()='Log in']"

    def __init__(self,driver):
        self.driver = driver
    def setUserName(self,username):
        self.driver.find_element(By.ID,self.txtbx_email_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID, self.txtbx_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_button).click()