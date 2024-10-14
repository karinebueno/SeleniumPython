from selenium.webdriver.common.by import By
from pages.base_page_sauce import BasePage
from time import sleep
from seleniumpagefactory import PageFactory

class CartItems(BasePage, PageFactory):

    locators = {
        "CARTDETAILS": ('class_name', "shopping_cart_link"),
        "removerItem": (By.ID, "remove-sauce-labs-backpack"),
        "QuantElementosAposRemocao": ('class_name', "shopping_cart_badge"),
        "Checkout": (By.ID, "checkout")
    }

    def removerItemDoCarrinho(self):
        self.CARTDETAILS.click_button()
        self.removerItem.click_button()

    def QuantAposRemocao(self):
        return self.QuantElementosAposRemocao.get_text()
    
    def CheckoutCart(self):
        self.Checkout.click_button()