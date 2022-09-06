import pytest
import time
from tests.configTest import setup, franchiseStore, select_store
from pages.loginPage import LoginPage

@pytest.mark.usefixtures("setup")
class Test_login_logout:
     def test_login(self): 
         assert LoginPage.login_test_check(self)
   
     def test_logout(self):
        select_store(self, franchiseStore)
        LoginPage.logout_press(self)
        time.sleep(2)
        assert LoginPage.logout_test_check(self)