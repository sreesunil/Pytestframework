import pytest
from selenium import webdriver

from config.testdata import testdata


@pytest.fixture()
def init_driver(request):
    driver = webdriver.Firefox()
    driver.get(testdata.URL)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


