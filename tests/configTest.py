import pytest
import os
import sys
import time
from dotenv import load_dotenv, find_dotenv
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service as Service2
from pages.loginPage import LoginPage

url = "http://10.5.1.125:17013/esambo/ifp"
password = "eSambo001"
login = "automatic.test.001"
driverEnv = "chrome"
franchiseStore = "A88"
networkStore = "203"
orderFile = "order_file.txt"
orderScanner = "order_scanner.txt"

if find_dotenv():
    load_dotenv(override=True)
    url = os.getenv('URL')
    password = os.getenv('USER_PASSWORD')
    login = os.getenv('USER_LOGIN')
    driverEnv = os.getenv('DRIVER')
    franchiseStore = os.getenv('FRANCHISE_STORE')
    networkStore = os.getenv('NETWORK_STORE')
    orderFile = os.getenv('ORDER_FILE_NAME')
    orderScanner = os.getenv('ORDER_SCANNER_NAME')

orderFilePath = os.path.join(sys.path[0] , f'ScannerFiles/{orderFile}')
orderScannerPath = os.path.join(sys.path[0] , f'ScannerFiles/{orderScanner}')

@pytest.fixture(scope="function")
def setup(request):
    current_data= datetime.now().strftime("%H.%M.%S %d.%m.%Y")
    if driverEnv == "chrome":
        driver = Chrome(service=Service(ChromeDriverManager().install()))
    if driverEnv == "firefox":
        driver = Firefox(service=Service2(GeckoDriverManager().install()))
    driver.get(url)
    driver.maximize_window()
    driver.find_element(*LoginPage.LOGIN_INPUT).send_keys(login)
    driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPage.BUTTON_LOGIN).click()
    request.cls.driver = driver
    yield driver
    if request.session.testsfailed:
        driver.save_screenshot(rf'screenshots\Test Failed {current_data}.png')
    driver.close()


def getElement(self, locator): 
    for x in range(60):
            try:
                try:
                    self.driver.find_element(By.XPATH, '//div[@class="blockUI blockOverlay"]')
                    time.sleep(0.5)
                except:
                    return self.driver.find_element(*locator)            
            except: 
                time.sleep(0.5)
    raise RuntimeError(f"Page loading timeout") 
    
def select_store(self, store):
        input = getElement(self, LoginPage.INPUT_SHOP)
        input.click()
        time.sleep(0.5)
        storeSelect = getElement(self, (By.XPATH, f"//span[text()[contains(.,'{store}')]]") )
        storeSelect.click()
        button = getElement(self, LoginPage.BUTTON_ZALOGUJ)
        button.click()
        self.driver.switch_to.frame(self.driver.find_element(*LoginPage.RELOG_IFRAME))

def refresh_until(self, locator = (By.XPATH, "//span[contains(@aria-valuenow, '100')]")):
    for x in range(10):
            try:
                self.driver.find_element(*locator)
                break
            except NoSuchElementException:
                try:
                    refresh = self.driver.find_element(By.XPATH, "//a//*[text()[contains(.,'Od??wie??')]]") 
                    refresh.click()
                    time.sleep(1)
                except:
                    time.sleep(1)
                
                    
        
        
            
            
    

            

