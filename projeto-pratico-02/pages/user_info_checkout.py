from selenium.webdriver.common.by import By
from pages.base_page_sauce import BasePage
from time import sleep
from seleniumpagefactory import PageFactory

class user_info_checkout(BasePage, PageFactory):

    locators = {
        "firstname": (By.ID, "first-name"),
        "lastName": (By.ID, "last-name"),
        "postalCode": (By.ID, "postal-code"),
        "continueButton": (By.ID, "continue")
    }

    def fill_checkout_info(self, firstname, lastName,postalCode):
        self.firstname.set_text(firstname)
        self.lastName.set_text(lastName)
        self.postalCode.set_text(postalCode)
        sleep(3)

    def ClickInContinue(self):
        self.continueButton.click_button()