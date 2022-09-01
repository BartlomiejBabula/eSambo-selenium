import pytest
import time
# import sys
# sys.path.append('..\\poetry\tests')
from .configTest import setup, franchiseStore
from pages.loginLogoutPage import LoginLogoutPage

@pytest.mark.usefixtures("setup")
class TestLoginLogout:
     def test_login(self): 
        assert LoginLogoutPage.login_test_check(self)
   
     def test_logout(self):
        LoginLogoutPage.select_shop(self, franchiseStore)
        LoginLogoutPage.zaloguj_button_press(self)
        LoginLogoutPage.logout_press(self)
        time.sleep(2)
        assert LoginLogoutPage.login_button_press(self)