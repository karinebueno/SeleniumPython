from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import pytest
from pages.base_page import BasePage
from pages.etapa1_page import Etapa1Page

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
    etapa1 = Etapa1Page(driver)
    etapa1.preencher_etapa1("standard_user", "secret_sauce")

    final = Etapa2Page(driver)
    msg = final.obterMensagem()

    assert msg == "6"

    sleep(5)




