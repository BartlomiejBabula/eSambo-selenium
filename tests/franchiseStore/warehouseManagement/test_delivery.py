import pytest
import time
import datetime 
from tests.configTest import getElement, refresh_until, setup, select_store, franchiseStore
from pages.franchiseStorePages.homePage import HomePage
from pages.franchiseStorePages.warehouseManagementPage import WarehouseManagementPage
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class Test_delivery:
    today = datetime.date.today().strftime("%Y-%m-%d") 
    
    def test_create_PZ_without_order(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.warehouse_management_press(self)
        WarehouseManagementPage.delivery_create_new_doc_button_press(self)
        WarehouseManagementPage.delivery_create_new_doc_menu_pz_without_order(self)
        WarehouseManagementPage.delivery_doc_basis_of_the_doc_send_key(self)
        WarehouseManagementPage.delivery_doc_supplier_select(self)
        WarehouseManagementPage.delivery_doc_article_select(self)
        WarehouseManagementPage.close_edit_press(self)
        assert getElement(self, (By.XPATH, "//*[text()[contains(.,'Zmiany zostały zapisane!')]]"))

    def test_confirm_PZ_without_order(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.warehouse_management_press(self)
        WarehouseManagementPage.delivery_status_prepared_button_press(self)
        WarehouseManagementPage.first_doc_select(self)
        WarehouseManagementPage.confirm_doc_press(self)
        refresh_until(self, (By.XPATH, "//*[contains(@class, 'window_header')]//*[text()[contains(.,'Zatwierdzone')]]"))
        assert getElement(self, (By.XPATH, "//*[contains(@class, 'window_header')]//*[text()[contains(.,'Zatwierdzone')]]"))
        
    def test_create_KPZ(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.warehouse_management_press(self)
        WarehouseManagementPage.delivery_create_new_doc_button_press(self)
        WarehouseManagementPage.delivery_create_new_doc_menu_kpz_press(self)
        WarehouseManagementPage.KPZ_delivery_doc_input_send_key(self)
        WarehouseManagementPage.KPZ_delivery_doc_date_input_send_key(self, Test_delivery.today)
        WarehouseManagementPage.KPZ_delivery_doc_find_press(self)
        WarehouseManagementPage.KPZ_first_delivery_doc_select(self)
        WarehouseManagementPage.operation_menu_press(self)
        WarehouseManagementPage.operation_menu_add_item_delivery_press(self)
        WarehouseManagementPage.KPZ_first_article_press(self)
        WarehouseManagementPage.operation_menu_confirm_press(self)
        WarehouseManagementPage.KPZ_article_quantity_send_key(self, "5")
        WarehouseManagementPage.close_edit_press(self)
        assert getElement(self, (By.XPATH, "//*[text()[contains(.,'Zmiany zostały zapisane!')]]"))


    def test_confirm_KPZ(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.warehouse_management_press(self)
        WarehouseManagementPage.KPZ_status_prepared_button_press(self)
        WarehouseManagementPage.first_doc_select(self)
        WarehouseManagementPage.confirm_doc_press(self)
        refresh_until(self, (By.XPATH, "//*[contains(@class, 'window_header')]//*[text()[contains(.,'Zatwierdzone')]]"))
        assert getElement(self, (By.XPATH, "//*[contains(@class, 'window_header')]//*[text()[contains(.,'Zatwierdzone')]]"))


    def test_create_PZZ(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.warehouse_management_press(self)
        WarehouseManagementPage.delivery_create_new_doc_button_press(self)
        WarehouseManagementPage.delivery_create_new_doc_menu_pzz_press(self)
        WarehouseManagementPage.PZZ_nr_doc_wz_send_key(self)
        WarehouseManagementPage.PZZ_delivery_date_input_send_key(self, Test_delivery.today)
        WarehouseManagementPage.PZZ_supplier_select(self)
        WarehouseManagementPage.PZZ_supplier_department_select(self)
        WarehouseManagementPage.PZZ_firts_element_supplier_article_name_select(self)
        WarehouseManagementPage.PZZ_firts_element_quantity_send_keys(self, "2")
        WarehouseManagementPage.close_edit_press(self)
        assert getElement(self, (By.XPATH, "//*[text()[contains(.,'Zmiany zostały zapisane!')]]"))


    def test_confirm_PZZ(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.warehouse_management_press(self)
        WarehouseManagementPage.PZZ_status_prepared_button_press(self)
        WarehouseManagementPage.first_doc_select(self)
        WarehouseManagementPage.confirm_doc_press(self)
        refresh_until(self, (By.XPATH, "//*[contains(@class, 'window_header')]//*[text()[contains(.,'Zatwierdzone')]]"))
        assert getElement(self, (By.XPATH, "//*[contains(@class, 'window_header')]//*[text()[contains(.,'Zatwierdzone')]]"))

# Brak (KPZZ potrzebny interfejs FRANKO faktury), PZC, KPZ

    # def test_create_PZC(self):
        