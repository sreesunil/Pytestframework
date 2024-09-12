import pytest
from pages.UsermenuPage import usermenuPage
from pages.LoginPage import LoginPage
from tests.conftest import init_driver

from config.testdata import testdata

@pytest.mark.usefixtures("init_driver" , "log_on_failure")
class Test_usermenu():

    def test_Usermenu(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login(testdata.USER_NAME, testdata.PASSWORD)
        self.UsermenuPage = usermenuPage(self.driver)
        self.UsermenuPage.select_profile(self.driver)



