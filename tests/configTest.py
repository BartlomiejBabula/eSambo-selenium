import pytest
import os
import sys
import time
from dotenv import load_dotenv
from datetime import datetime
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import Firefox
from pages.loginPage import LoginPage

# wywalić sleepy
load_dotenv(override=False)

url = os.getenv('URL')
password = os.getenv('USER_PASSWORD')
login = os.getenv('USER_LOGIN')
driverEnv = os.getenv('DRIVER')
franchiseStore = os.getenv('FRANCHISE_STORE')
networkStore = os.getenv('NETWORK_STORE')
orderFile = os.getenv('ORDER_FILE_NAME')
orderScanner = os.getenv('ORDER_SCANNER_NAME')
timeout = os.getenv('TIMEOUT')
orderFilePath = os.path.join(sys.path[0] , f'ScannerFiles/{orderFile}')
orderScannerPath = os.path.join(sys.path[0] , f'ScannerFiles/{orderScanner}')

@pytest.fixture(scope="function")
def setup(request):
    current_data= datetime.now().strftime("%H.%M.%S %d.%m.%Y")
    if driverEnv == "chrome":
        driver = Chrome(executable_path=ChromeDriverManager().install())
    if driverEnv == "firefox":
        driver = Firefox(executable_path=GeckoDriverManager().install()) 
    # driver.implicitly_wait(10)
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


def login_franchise(self):
        LoginPage.select_shop(self, franchiseStore)
        LoginPage.zaloguj_button_press(self)

def check_block_ui(self):
        try:
            self.driver.find_element(By.CLASS_NAME, "blockOverlay")
        except :
            return False
        return True

def getElement(self, locator):    
            for x in range(20):
                check = check_block_ui(self)
                if check:
                    time.sleep(0.5)
                else:
                    try:
                        element = self.driver.find_element(*locator)
                    except:
                        time.sleep(0.5)
            return element
            

