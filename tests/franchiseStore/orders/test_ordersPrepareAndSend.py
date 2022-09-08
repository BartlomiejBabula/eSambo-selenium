import pytest
import time
import datetime 
from tests.configTest import setup, select_store, orderFilePath, orderScannerPath, franchiseStore, refresh_until
from pages.franchiseStorePages.homePage import HomePage
from pages.franchiseStorePages.ordersPage import OrdersPage

@pytest.mark.usefixtures("setup")
class Test_orders_send_and_prepare:
    
    def test_prepare_orders(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        OrdersPage.prepare_order_press(self)
        assert OrdersPage.prepare_order_check(self)

    def test_send_order(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        HomePage.orders_prepare_press(self)
        OrdersPage.first_order_press(self)
        OrdersPage.send_order_inside_order_button_press(self)
        OrdersPage.send_operation(self)
        refresh_until(self, OrdersPage.CLOSE_BUTTON)
        OrdersPage.close_operation(self)
        assert OrdersPage.prepare_order_check(self)

    def test_send_order_from_replenish_assortment(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        OrdersPage.replenish_assortment_press(self)
        OrdersPage.first_order_press(self)
        OrdersPage.send_order_inside_order_button_press(self)
        OrdersPage.send_operation(self)
        refresh_until(self, OrdersPage.CLOSE_BUTTON)
        OrdersPage.close_operation(self)
        assert OrdersPage.prepare_order_check(self)

    def test_prepare_orders_in_future(self):
        tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d.%m.%Y")
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        OrdersPage.order_in_future_press(self)
        time.sleep(1)
        OrdersPage.order_in_future_input_send(self, tomorrow)
        OrdersPage.active_date_select(self)
        OrdersPage.prepare_order_press(self)
        assert OrdersPage.prepare_order_in_future_check(self)

    def test_send_order_in_future(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        HomePage.orders_in_future_press(self)
        OrdersPage.order_list_sort_by_shipment(self)
        OrdersPage.first_order_press(self)
        OrdersPage.send_order_inside_order_button_press(self)
        OrdersPage.send_operation(self)
        refresh_until(self, OrdersPage.CLOSE_BUTTON)
        OrdersPage.close_operation(self)
        assert OrdersPage.prepare_order_in_future_check(self)

    def test_prepare_order_from_file(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        OrdersPage.tab_order_from_scanner_press(self)
        OrdersPage.load_file_button_press(self)
        OrdersPage.select_file(self, orderFilePath)
        OrdersPage.confirm_button_press(self)
        OrdersPage.run_task_press(self)
        refresh_until(self, OrdersPage.CLOSE_BUTTON)
        OrdersPage.close_operation(self)
        assert OrdersPage.prepare_order_from_scanner_check(self)

    def test_send_order_from_file(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        HomePage.orders_from_scanner_press(self)
        OrdersPage.order_from_scanner_icon_press(self, 'order_file.txt')
        OrdersPage.confirm_button_press(self)
        refresh_until(self, OrdersPage.CLOSE_BUTTON)
        OrdersPage.close_operation(self)
        assert OrdersPage.send_order_from_file_check(self)

    def test_prepare_order_from_scanner(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        OrdersPage.tab_order_from_scanner_press(self)
        OrdersPage.load_scanner_button_press(self)
        OrdersPage.select_path_scanner(self)
        OrdersPage.select_file(self, orderScannerPath)
        OrdersPage.confirm_button_press(self)
        OrdersPage.run_task_press(self)
        refresh_until(self, OrdersPage.CLOSE_BUTTON)
        OrdersPage.close_operation(self)
        assert OrdersPage.prepare_order_from_scanner_check(self)

    def test_send_order_from_scanner(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        HomePage.orders_from_scanner_press(self)
        OrdersPage.order_from_scanner_icon_press(self, 'order_scanner.txt')
        OrdersPage.confirm_button_press(self)
        refresh_until(self, OrdersPage.CLOSE_BUTTON)
        OrdersPage.close_operation(self)
        assert OrdersPage.send_order_from_file_check(self)