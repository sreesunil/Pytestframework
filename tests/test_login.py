import pytest

from pages.LoginPage import LoginPage
from tests.conftest import init_driver

from config.testdata import testdata

@pytest.mark.usefixtures("init_driver" , "log_on_failure")
class Test_Login():

    def test_login(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login(testdata.USER_NAME , testdata.PASSWORD)

    def test_forgotPassword(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.forgot_password(testdata.USER_NAME , testdata.EMAIL)

    def test_errorMessage(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.login_errorMessage(testdata.USER_NAME)
        
    def test_wrongCredentials(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.wrong_credentials("123" , "1234")














