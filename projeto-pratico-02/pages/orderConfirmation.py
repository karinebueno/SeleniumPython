from selenium.webdriver.common.by import By
from pages.base_page_sauce import BasePage
from time import sleep
from seleniumpagefactory import PageFactory

class orderConfirmation(BasePage, PageFactory):

    locators = {
        "mensagemFinal": ('class_name', "complete-header")
    }

    def validarMensagemFinal(self):
        return self.mensagemFinal.get_text()
