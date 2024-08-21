from selenium.webdriver.common.by import By

from config.testdata import testdata
from pages.BasePage import BasePage


class LoginPage(BasePage):

    USERNAME = (By.ID,"username")
    PASSWORD = (By.ID,"password")
    LOGIN_BUTTON = (By.ID , "Login")
    FORGOT_YOUR_PASSWORD =(By.LINK_TEXT,"Forgot Your Password?")
    FORGOT_USERNAME = (By.ID ,"un")
    CONTINUE_BUTTON = (By.ID , "continue")
    EROOR_MESSAGE = (By.ID , "error")


    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(testdata.URL)

    def get_login_page_title(self , title):
        return self.get_title(title)


    def do_login(self, username , password):
        self.do_send_keys(self.USERNAME , username)
        self.do_send_keys(self.PASSWORD,password)
        self.do_click(self.LOGIN_BUTTON)


    def forgot_password(self,username,email):
        self.do_send_keys(self.USERNAME , username)
        self.do_click(self.FORGOT_YOUR_PASSWORD)
        self.do_send_keys(self.FORGOT_USERNAME ,email)
        self.do_click(self.CONTINUE_BUTTON)


    def login_errorMessage(self,username):
        self.do_send_keys(self.USERNAME, username)
        self.do_click(self.LOGIN_BUTTON)
        expected_message = "Please enter your password."
        assert self.EROOR_MESSAGE.__eq__(expected_message)


    def wrong_credentials(self , username , password):
        self.do_send_keys(self.USERNAME , username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)







