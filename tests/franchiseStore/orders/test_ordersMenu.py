import pytest
import time
import datetime 
from tests.configTest import setup, select_store, getElement, franchiseStore, refresh_until
from pages.franchiseStorePages.homePage import HomePage
from pages.franchiseStorePages.ordersPage import OrdersPage
from selenium.webdriver.common.by import By

def isComplited(self):
    fisrt_element = getElement(self, (By.XPATH, '//table/tbody/tr[1]/td[4]/div')).get_attribute('innerHTML')
    for x in range(10):
        try:
            check = self.driver.find_element(By.XPATH, '//table/tbody/tr[1]/td[4]/div').get_attribute('innerHTML')
            print(check, fisrt_element)
            if check != fisrt_element:
                break
            time.sleep(0.5)
        except:
            time.sleep(0.5)

def checking_menu(self):
        OrdersPage.order_list_first_order_checkbox_press(self)
        OrdersPage.order_list_menu_select_option(self, OrdersPage.ORDER_LIST_MENU_DELETE)
        OrdersPage.execute_operation(self)
        refresh_until(self)
        OrdersPage.close_operation(self)
        isComplited(self)
        OrdersPage.order_list_menu_select_option(self, OrdersPage.ORDER_LIST_MENU_NULL)
        OrdersPage.order_list_first_order_checkbox_press(self)
        OrdersPage.order_list_menu_select_option(self, OrdersPage.ORDER_LIST_MENU_SEND)
        OrdersPage.execute_operation(self)
        refresh_until(self)
        OrdersPage.close_operation(self)
        isComplited(self)
        OrdersPage.order_list_menu_select_option(self, OrdersPage.ORDER_LIST_MENU_NULL)
        OrdersPage.order_list_first_order_checkbox_press(self)
        OrdersPage.order_list_menu_select_option(self, OrdersPage.ORDER_LIST_MENU_PRINT)


@pytest.mark.usefixtures("setup")
class Test_orders_list_menu:

    def test_orders_prepare_list_menu(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        HomePage.orders_prepare_press(self)
        checking_menu(self)
        assert getElement(self, (By.XPATH, "//*[text()[contains(.,'Zamówienia w przygotowaniu')]]"))

    def test_orders_in_future_list_menu(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        HomePage.orders_in_future_press(self)
        checking_menu(self)
        assert getElement(self, (By.XPATH, "//*[text()[contains(.,'Zamówienia w przyszłość')]]"))

    def test_orders_in_future_list_menu(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        HomePage.orders_generated_for_today_press(self)
        checking_menu(self)
        assert getElement(self, (By.XPATH, "//*[text()[contains(.,'Zamówienia wygenerowane na dziś')]]"))


@pytest.mark.usefixtures("setup")
class Test_orders_find_order_menu:

    def test_orders_prepare_find_menu(self):
        tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d.%m.%Y")
        yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%d.%m.%Y")
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        HomePage.orders_sent_today_press(self)
        OrdersPage.find_order_menu_checkbox_press(self)
        OrdersPage.find_order_menu_checkbox_press(self)
        OrdersPage.find_order_menu_checkbox_press(self, OrdersPage.FIND_ORDER_MENU_C4_CROSS_CHECKBOX)
        OrdersPage.find_order_menu_checkbox_press(self, OrdersPage.FIND_ORDER_MENU_C4_CROSS_CHECKBOX)
        OrdersPage.find_order_menu_checkbox_press(self, OrdersPage.FIND_ORDER_MENU_C4_EXTERNAL_CHECKBOX)
        OrdersPage.find_order_menu_checkbox_press(self, OrdersPage.FIND_ORDER_MENU_C4_EXTERNAL_CHECKBOX)
        OrdersPage.find_order_menu_checkbox_press(self, OrdersPage.FIND_ORDER_MENU_C4_LOCAL_CHECKBOX)
        OrdersPage.find_order_menu_checkbox_press(self, OrdersPage.FIND_ORDER_MENU_C4_LOCAL_CHECKBOX)
        OrdersPage.find_order_menu_status_select(self, OrdersPage.FIND_ORDER_MENU_STATUS_ACCEPTED)
        OrdersPage.find_order_menu_status_select(self, OrdersPage.FIND_ORDER_MENU_STATUS_SENT)
        OrdersPage.find_order_menu_status_select(self, OrdersPage.FIND_ORDER_MENU_STATUS_TO_SEND)
        OrdersPage.find_order_menu_source_select(self, OrdersPage.FIND_ORDER_MENU_SOURCE_ORDER_AUTOMATIC)
        OrdersPage.find_order_menu_source_select(self, OrdersPage.FIND_ORDER_MENU_SOURCE_ORDER_FROM_SCANNER)
        OrdersPage.find_order_menu_source_select(self, OrdersPage.FIND_ORDER_MENU_SOURCE_ORDER_CENTRAL)
        OrdersPage.find_order_menu_source_select(self, OrdersPage.FIND_ORDER_MENU_SOURCE_ORDER_FROM_FRANET)
        OrdersPage.find_order_menu_source_select(self, OrdersPage.FIND_ORDER_MENU_SOURCE_ORDER_FROM_USER)
        OrdersPage.find_order_menu_delivery_to_send_keys(self, tomorrow)
        OrdersPage.find_order_menu_delivery_from_send_keys(self, yesterday)
        OrdersPage.find_order_menu_date_from_send_keys(self, yesterday)
        OrdersPage.find_order_menu_date_to_send_keys(self, tomorrow)
        OrdersPage.find_order_menu_supplier_select(self)
        OrdersPage.find_order_menu_user_select(self)
        OrdersPage.find_order_menu_article_code_select(self)
        OrdersPage.find_order_menu_article_group_select(self)
        OrdersPage.find_order_menu_doc_symbol_select(self)
