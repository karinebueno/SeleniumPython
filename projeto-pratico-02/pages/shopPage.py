from selenium.webdriver.common.by import By
from pages.base_page_sauce import BasePage
from time import sleep
from seleniumpagefactory import PageFactory

class ProductPage(BasePage, PageFactory):

    locators = {
        "buttonsAddToCart": (By.XPATH, "//button[contains(@id, 'add-to-cart')]"),
        "QuantElementos": ('class_name', "shopping_cart_badge"),
        "cartLink": ('class_name', "shopping_cart_link")
    }
    
    def adicionar_todos_ao_carrinho(self):
        buttons = self.driver.find_elements(*self.locators["buttonsAddToCart"])
        for button in buttons:
            button.click()
        # for button in self.buttonsAddToCart:
        #     button.click_button()

    def obter_quantidade_no_carrinho(self):
        return self.QuantElementos.get_text()
