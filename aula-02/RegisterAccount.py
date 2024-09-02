from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

my_service = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=my_service, options=chrome_options)

browser.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")

browser.maximize_window()

firstName = browser.find_element(By.ID, "input-firstname")
firstName.send_keys("Joaquim")


lastname = browser.find_element(By.ID, "input-lastname")
lastname.send_keys("De Amaral")

email = browser.find_element(By.ID, "input-email")
email.send_keys("joaquimdeamaral@gmail.com")

telephone = browser.find_element(By.ID, "input-telephone")
telephone.send_keys("123456")

password = browser.find_element(By.ID, "input-password")
password.send_keys("Joa159AM!")

password = browser.find_element(By.ID, "input-confirm")
password.send_keys("Joa159AM!")


# newsletter = browser.find_element(By.XPATH, "//input[@id='input-newsletter-no']")
# newsletter.click()

newsletter = browser.find_element(By.XPATH, value="//label[@for='input-newsletter-no']")
newsletter.click()

# newsletter = browser.find_element(By.XPATH, "//label[@for='input-newsletter-no']")
# newsletter.click()

# newsletter = browser.find_element(By.XPATH,"//label[contains(@for,'input-newsletter-no')]")
# newsletter.click()

# newsletter = browser.find_element(By.XPATH,"//label[@for='input-newsletter-no')]")
# newsletter.click()


privacypolicy = browser.find_element(By.XPATH, "//label[@class='custom-control-label'][contains(.,'I have read and agree to the Privacy Policy')]")
privacypolicy.click()

continuebutton = browser.find_element(By.XPATH,"//input[@value='Continue']")
continuebutton.click()


sleep(5)