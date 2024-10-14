from selenium.webdriver.common.by import By
from pages.base_page_sauce import BasePage
from time import sleep
from seleniumpagefactory import PageFactory

class orderSummary(BasePage, PageFactory):

    locators = {
        "finish": (By.ID, "finish")
      
    }

    def ClickInFinish(self):
        self.finish.click_button()