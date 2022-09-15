import pytest
import time
import datetime 
from tests.configTest import getElement, refresh_until, setup, select_store, franchiseStore
from pages.franchiseStorePages.homePage import HomePage
from pages.franchiseStorePages.warehouseManagementPage import WarehouseManagementPage
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class Test_delivery:
    
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

    def test_send_PZ_without_order(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.warehouse_management_press(self)
        WarehouseManagementPage.delivery_status_prepared_button_press(self)
        WarehouseManagementPage.first_doc_select(self)
        WarehouseManagementPage.confirm_doc_press(self)
        refresh_until(self, (By.XPATH, "//*[contains(@class, 'window_header')]//*[text()[contains(.,'Zatwierdzone')]]"))
        assert getElement(self, (By.XPATH, "//*[contains(@class, 'window_header')]//*[text()[contains(.,'Zatwierdzone')]]"))
        