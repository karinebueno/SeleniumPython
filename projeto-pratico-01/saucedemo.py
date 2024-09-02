from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import pytest

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    yield driver

    driver.quit()


def test_badgeVerification(driver):
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    loginButton = driver.find_element(By.ID, "login-button")
    loginButton.click()

    buttonsAddToCart = driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
    for button in buttonsAddToCart:
        button.click()
    
    QuantElementos = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert QuantElementos == "6"
    
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()

    removerItem = driver.find_element(By.ID, "remove-sauce-labs-backpack")
    removerItem.click()

    QuantElementosAposRemocao = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert QuantElementosAposRemocao == "5"

    checkout = driver.find_element(By.ID, "checkout")
    checkout.click()

    firstname = driver.find_element(By.ID, "first-name")
    firstname.send_keys("Joaquim")

    LastName = driver.find_element(By.ID, "last-name")
    LastName.send_keys("De Amaral")

    postalCode = driver.find_element(By.ID, "postal-code")
    postalCode.send_keys("37540000")

    continueButton = driver.find_element(By.ID, "continue")
    continueButton.click()

    finish = driver.find_element(By.ID, "finish")
    finish.click()

    mensagemFinal = driver.find_element(By.CLASS_NAME,"complete-header").text
    assert mensagemFinal == "Thank you for your order!"
    
    sleep(5)