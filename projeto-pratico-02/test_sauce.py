from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import pytest
from pages.base_page_sauce import BasePage
from pages.login import LoginPage
from pages.shopPage import ProductPage
from pages.shoppingCart import CartItems
from pages.user_info_checkout import user_info_checkout
from pages.orderSummary import orderSummary
from pages.orderConfirmation import orderConfirmation



#Page Factory
@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
    
    BasePage(driver).open_site()

    yield driver

    driver.quit()

def test_login(driver):
    #Login na Etapa 1
    etapa1 = LoginPage(driver)
    etapa1.preencher_etapa1("standard_user", "secret_sauce")

    #Adicionar itens ao carrinho na Etapa 2
    etapa2 = ProductPage(driver)
    etapa2.adicionar_todos_ao_carrinho()

    # sleep(5)

    #Verificar a quantidade no badge
    quantidade = etapa2.obter_quantidade_no_carrinho()
    assert quantidade == "6"

    #Remover Item do carrinho
    etapa3 = CartItems(driver)
    etapa3.removerItemDoCarrinho()
    

    #Verificar a quantidade após remover
    quantidade_apos_remover = etapa3.QuantAposRemocao()
    assert quantidade_apos_remover == "5"

    #Clicar no checkout
    etapa3.CheckoutCart()

    #Preencher as informações no checkout
    etapa4 = user_info_checkout(driver)
    etapa4.fill_checkout_info("Caio","Silveira",37540000)
    # sleep(3)
    etapa4.ClickInContinue()

    #Clicar no botão finish no checkout
    etapa5 = orderSummary(driver)
    etapa5.ClickInFinish()

    #Validar Mensagem Final
    etapa6 = orderConfirmation(driver)
    mensagemFinal = etapa6.validarMensagemFinal()
    assert mensagemFinal == "Thank you for your order!"