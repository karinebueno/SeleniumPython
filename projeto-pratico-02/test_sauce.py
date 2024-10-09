from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import pytest
from pages.base_page_sauce import BasePage
from pages.etapa1_page_sauce import Etapa1Page
from pages.etapa2_page_sauce import Etapa2Page



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
    etapa1 = Etapa1Page(driver)
    etapa1.preencher_etapa1("standard_user", "secret_sauce")

    #Adicionar itens ao carrinho na Etapa 2
    etapa2 = Etapa2Page(driver)
    etapa2.adicionar_todos_ao_carrinho()

    sleep(5)

    #Verificar a quantidade no badge
    quantidade = etapa2.obter_quantidade_no_carrinho()
    assert quantidade == "6"

    #Acessar o carrinho e remover um item
    etapa2.acessar_carrinho()
    etapa2.remover_item_do_carrinho()

    #Verificar a quantidade após remover
    quantidade_apos_remover = etapa2.obter_quantidade_no_carrinho()
    assert quantidade_apos_remover == "5"

    sleep(5)
