import openpyxl 
import pytest
import time
import sys
sys.path.append('..\\poetry')
from datetime import datetime
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import Firefox

wb = openpyxl.load_workbook(rf'TestConfig.xlsx')
sheet = wb["1"]
url = sheet['B1'].value
password = sheet['B4'].value
login = sheet['B3'].value

@pytest.fixture(scope="class")
def setup(request):
    current_data= datetime.now().strftime("%H.%M.%S %d.%m.%Y")
    if sheet['B2'].value == "chrome":
        driver = Chrome(executable_path=ChromeDriverManager().install())
    if sheet['B2'].value == "firefox":
        driver = Firefox(executable_path=GeckoDriverManager().install()) 
    driver.implicitly_wait(10)
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    request.cls.driver = driver
    yield driver
    if request.session.testsfailed:
        print(current_data)
        driver.save_screenshot(rf'screenshots\Test Failed {current_data}.png')
    driver.close()

