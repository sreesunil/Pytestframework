
import pytest
from selenium import webdriver

from config.testdata import testdata

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.yield_fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        driver.save_screenshot("page.png")



@pytest.fixture(params=["chrome" , "firefox"] , scope= "class")
def init_driver(request):
    global driver
    if request.param =="chrome":
        driver = webdriver.Chrome()
    if request.param =="firefox":
        driver = webdriver.Firefox()
    driver.get(testdata.URL)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


