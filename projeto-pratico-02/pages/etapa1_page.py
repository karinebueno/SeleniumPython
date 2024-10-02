from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from seleniumpagefactory import PageFactory

class Etapa1Page(BasePage, PageFactory):

    locators = {
        "USERNAME": (By.ID, "user-name"),
        "PASSWORD": (By.ID, "password"),
        "loginButton": (By.ID, "login-button")
    }

    def preencher_etapa1(self,username,password):
        self.USERNAME.set_text(username)
        self.PASSWORD.set_text(password)
        self.loginButton.click_button()
