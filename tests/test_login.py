import pytest
import time
import sys
sys.path.append('..\\poetry\tests')
from selenium.webdriver.common.by import By
from .configTest import setup, login, password
from pages.loginPage import loginPage


@pytest.mark.usefixtures("setup")
class TestLoginLogout:
    def test_login(self): 
        loginPage.login_pass(self,login)
        loginPage.password_pass(self, password)
        loginPage.login_button_press(self)
        time.sleep(2)
        assert loginPage.search_zaloguj_button_press(self)