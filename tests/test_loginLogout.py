import pytest
import time
from tests.configTest import setup, franchiseStore
from pages.loginPage import LoginPage

@pytest.mark.usefixtures("setup")
class Test_login_logout:
     def test_login(self): 
         assert LoginPage.login_test_check(self)
   
     def test_logout(self):
        LoginPage.select_shop(self, franchiseStore)
        LoginPage.zaloguj_button_press(self)
        LoginPage.logout_press(self)
        time.sleep(1)
        assert LoginPage.login_button_press(self)