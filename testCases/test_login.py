


from pageObjects.loginpage import Login

class Test_1:
    baseurl = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_user_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        loginPageObj = Login(self.driver)
        loginPageObj.setUserName(self.username)
        loginPageObj.setPassword(self.password)
        loginPageObj.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard":
            print("title is crt")
        else:
            print("url is wrong")
    #
    def test_verify_url(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        act_url = self.driver.current_url
        if act_url == self.baseurl:
            print("crct")
        else:
            print("wrong")

