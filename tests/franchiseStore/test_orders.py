import pytest
import time
from selenium.webdriver.common.by import By
from ..configTest import setup, franchiseStore
from pages.loginLogoutPage import LoginLogoutPage
from pages.franchiseStorePages.homePage import HomePage
from pages.franchiseStorePages.ordersPage import OrdersPage

@pytest.mark.usefixtures("setup")
class TestOrders:
    def test_prepare_orders(self):
        LoginLogoutPage.select_shop(self, franchiseStore)
        LoginLogoutPage.zaloguj_button_press(self)
        HomePage.articles_press(self)
        time.sleep(3)
        OrdersPage.prepare_order_press(self)
        time.sleep(5)
        assert OrdersPage.prepare_order_check(self)

    def test_send_order(self):
        LoginLogoutPage.select_shop(self, franchiseStore)
        LoginLogoutPage.zaloguj_button_press(self)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        time.sleep(1)
        HomePage.orders_prepare_press(self)
        time.sleep(5)
        OrdersPage.first_order_press(self)
        OrdersPage.send_order_inside_order_button_press(self)
        time.sleep(2)
        OrdersPage.send_operation(self)
        time.sleep(5)
        OrdersPage.close_operation(self)
        time.sleep(2)
        assert OrdersPage.prepare_order_check(self)