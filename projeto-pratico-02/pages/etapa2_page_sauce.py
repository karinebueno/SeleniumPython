from selenium.webdriver.common.by import By
from pages.base_page_sauce import BasePage
from time import sleep
from seleniumpagefactory import PageFactory

class Etapa2Page(BasePage, PageFactory):

    locators = {
        "buttonsAddToCart": (By.XPATH, "//button[contains(@id, 'add-to-cart')]"),
        "QuantElementos": (By.CLASS_NAME, "shopping_cart_badge"),
        "cartLink": (By.CLASS_NAME, "shopping_cart_link")
    }
    
    def adicionar_todos_ao_carrinho(self):
        buttons = self.driver.find_elements(*self.locators["buttonsAddToCart"])
        for button in buttons:
            button.click()
        # for button in self.buttonsAddToCart:
        #     button.click_button()

    def obter_quantidade_no_carrinho(self):
        return self.QuantElementos.get_text()

    def remover_item_do_carrinho(self):
        self.removerItem.click_button()

    def acessar_carrinho(self):
        self.cartLink.click_button()