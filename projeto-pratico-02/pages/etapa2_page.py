from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from seleniumpagefactory import PageFactory

class Etapa2Page(BasePage, PageFactory):

    locators = {
        "buttonsAddToCart": (By.XPATH, "//button[text()='Add to cart']"),
        "QuantElementos": (By.CLASS_NAME, "shopping_cart_badge").text
    }



    def obterMensagem(self,buttonsAddToCart,QuantElementos):
        for button in buttonsAddToCart:
            self.button.click_button()

        return self.QuantElementos.get_text()
    
       
        self.QuantElementos.set_text(QuantElementos)