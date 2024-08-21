from selenium.webdriver.common.by import By

from config.testdata import testdata
from pages.BasePage import BasePage

class usermenuPage(BasePage):

    USER_NAV_BUTTON = (By.ID , "userNavButton")
    MY_PROFILE = (By.XPATH,"//a[@title='My Profile']")
    EDIT_CONTACT_BUTTON = (By.XPATH ,"//*[@class= 'contactInfo profileSection']//img")
    TAB_ABOUT = (By.LINK_TEXT , "About")
    IFRAME = (By.ID , "contactInfoContentId")
    LAST_NAME = (By.ID , "lastName")
    SAVE_BUTTON = (By.XPATH , "//input[@value = 'Save All']")
    POST_TAB = (By.ID , "publisherAttachTextPost")
    POST_IFRAME = (By.XPATH ,"//iframe[contains(@title,'Rich Text Editor, publisherRichTextEditor')]")
    POST_BODY = (By.XPATH , "//html[1]/body[1]")

    def __init__(self, driver):
        super().__init__(driver)


    def select_profile(self , driver):
        self.do_click(self.USER_NAV_BUTTON)
        self.do_click(self.MY_PROFILE)
        self.do_click(self.EDIT_CONTACT_BUTTON)
        driver.switch_to.frame("contactInfoContentId")
        self.do_click(self.TAB_ABOUT)
        self.do_clear(self.LAST_NAME)
        self.do_send_keys(self.LAST_NAME,"Sunil")
        self.do_click(self.SAVE_BUTTON)
        self.do_click(self.POST_TAB)
        #driver.switch_to.frame(self.POSTIFRAME)
        #self.do_click(self.POST_TAB)








