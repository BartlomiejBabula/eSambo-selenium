import pytest
import time
import datetime 
from tests.configTest import setup, select_store, orderFilePath, orderFile, orderScanner, orderScannerPath, franchiseStore, refresh_until
from pages.franchiseStorePages.homePage import HomePage
from pages.franchiseStorePages.ordersPage import OrdersPage

@pytest.mark.usefixtures("setup")
class Test_orders_send_and_prepare:
    
    def test_prepare_orders(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        OrdersPage.prepare_order_press(self)
        time.sleep(60)
        assert OrdersPage.prepare_order_check(self)
  
    def test_send_order(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        HomePage.orders_prepare_press(self)
        OrdersPage.first_order_press(self)
        OrdersPage.set_quantity_of_first_article(self, 2)
        OrdersPage.send_order_inside_order_button_press(self)
        OrdersPage.execute_operation(self)
        time.sleep(1)
        refresh_until(self, OrdersPage.CLOSE_BUTTON)
        OrdersPage.close_operation(self)
        assert OrdersPage.prepare_order_check(self)

    def test_send_order_from_list(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        HomePage.orders_prepare_press(self)
        OrdersPage.order_list_first_order_checkbox_press(self)
        OrdersPage.order_list_menu_select_option(self, OrdersPage.ORDER_LIST_MENU_SEND)
        OrdersPage.execute_operation(self)
        refresh_until(self, OrdersPage.CLOSE_BUTTON)
        OrdersPage.close_operation(self)
        assert OrdersPage.prepare_order_check(self)

    def test_send_order_from_replenish_assortment(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        OrdersPage.replenish_assortment_press(self)
        OrdersPage.first_order_press(self)
        OrdersPage.set_quantity_of_first_article(self, 2)
        OrdersPage.send_order_inside_order_button_press(self)
        OrdersPage.execute_operation(self)
        refresh_until(self, OrdersPage.CLOSE_BUTTON)
        OrdersPage.close_operation(self)
        assert OrdersPage.prepare_order_check(self)

    def test_send_order_from_replenish_assortment_from_list(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        OrdersPage.replenish_assortment_press(self)
        OrdersPage.order_list_first_order_checkbox_press(self)
        OrdersPage.order_list_menu_select_option(self, OrdersPage.ORDER_LIST_MENU_SEND)
        OrdersPage.execute_operation(self)
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
        time.sleep(60)
        assert OrdersPage.prepare_order_in_future_check(self)

    def test_send_order_in_future(self):
        tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d.%m.%Y")
        tomorrow_to_search = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        HomePage.orders_in_future_press(self)
        OrdersPage.find_order_menu_date_from_send_keys(self, tomorrow)
        OrdersPage.search_button_press(self, tomorrow_to_search)
        OrdersPage.order_list_sort_by_shipment(self)
        OrdersPage.first_order_press(self)
        OrdersPage.set_quantity_of_first_article(self, 1)
        OrdersPage.send_order_inside_order_button_press(self)
        OrdersPage.execute_operation(self)
        time.sleep(1)
        refresh_until(self, OrdersPage.CLOSE_BUTTON)
        OrdersPage.close_operation(self)
        assert OrdersPage.prepare_order_in_future_check(self)

    def test_send_order_in_future_from_list(self):
        tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d.%m.%Y")
        tomorrow_to_search = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        HomePage.orders_in_future_press(self)
        OrdersPage.find_order_menu_date_from_send_keys(self, tomorrow)
        OrdersPage.search_button_press(self, tomorrow_to_search)
        OrdersPage.order_list_sort_by_shipment(self)
        OrdersPage.order_list_first_order_checkbox_press(self)
        OrdersPage.order_list_menu_select_option(self, OrdersPage.ORDER_LIST_MENU_SEND)
        OrdersPage.execute_operation(self)
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
        time.sleep(1)
        OrdersPage.close_operation(self)
        assert OrdersPage.prepare_order_from_scanner_check(self)

    def test_send_order_from_file(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        HomePage.orders_from_scanner_press(self)
        OrdersPage.order_from_scanner_icon_press(self, orderFile)
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
        time.sleep(1)
        OrdersPage.close_operation(self)
        assert OrdersPage.prepare_order_from_scanner_check(self)

    def test_send_order_from_scanner(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        HomePage.orders_from_scanner_press(self)
        OrdersPage.order_from_scanner_icon_press(self, orderScanner)
        OrdersPage.confirm_button_press(self)
        refresh_until(self, OrdersPage.CLOSE_BUTTON)
        OrdersPage.close_operation(self)
        assert OrdersPage.send_order_from_file_check(self)