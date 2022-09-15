from selenium.webdriver.common.by import By
from tests.configTest import getElement



class WarehouseManagementPage:
    CREATE_NEW_DOC_BUTTON = (By.XPATH, "//*[text()[contains(.,'Utwórz nowy dokument')]]")
    DELIVERY_STATUS_PREPARED_BUTTON = (By.XPATH, "//div[contains(@class, 'deliveryStructureTree')]/table[6]")
    DELIVERY_CREATE_NEW_DOC_MENU_PZ_WITHOUT_ORDER_BUTTON = (By.XPATH, "//button[text()[contains(.,'PZ bez zamówienia')]]")
    DELIVERY_DOC_BASIS_OF_THE_DOC_INPUT = (By.XPATH, "//input[contains(@name, ':documentData:tabs:panel:documentFields:docDeliveryPZ')][contains(@type, 'text')]")
    DELIVERY_DOC_SUPPLIER_INPUT = (By.XPATH, "//input[contains(@name, ':supplier.orgUnit')]")
    DELIVERY_DOC_SUPPLIER_SEARCH_ICON = (By.XPATH, "//td[contains(@class, 'lookup')]")
    CLOSE_EDIT_BUTTON = (By.XPATH, "//*[text()[contains(.,'Zakończ edycję')]]")
    CONFIRM_DOC_BUTTON = (By.XPATH, "//*[text()[contains(.,'Zatwierdź')]]")


    def delivery_create_new_doc_button_press(self):
        getElement(self, WarehouseManagementPage.CREATE_NEW_DOC_BUTTON).click()

    def delivery_status_prepared_button_press(self):
        getElement(self, WarehouseManagementPage.DELIVERY_STATUS_PREPARED_BUTTON).click()

    def delivery_create_new_doc_menu_pz_without_order(self):
        getElement(self, WarehouseManagementPage.DELIVERY_CREATE_NEW_DOC_MENU_PZ_WITHOUT_ORDER_BUTTON).click()

    def delivery_doc_basis_of_the_doc_send_key(self):
        getElement(self, WarehouseManagementPage.DELIVERY_DOC_BASIS_OF_THE_DOC_INPUT).send_keys("automatic.test")

    def delivery_doc_supplier_select(self, supplier = "Herbaciarnia"):
        getElement(self, WarehouseManagementPage.DELIVERY_DOC_SUPPLIER_INPUT).click()
        getElement(self, WarehouseManagementPage.DELIVERY_DOC_SUPPLIER_INPUT).send_keys(supplier)
        getElement(self, WarehouseManagementPage.DELIVERY_DOC_SUPPLIER_SEARCH_ICON).click()

    def delivery_doc_article_select(self, article = "800716"):
        getElement(self, (By.XPATH, "//table/tbody/tr[1]/td[4]/span/span/table/tbody/tr/td[2]")).click()
        getElement(self, (By.XPATH, f"//*[text()[contains(.,'{article}')]]")).click()
        getElement(self, (By.XPATH, "//*[contains(@class, 'noCntxMenu')][contains(@name, ':rows:1:cells:7:')]")).send_keys("2")
        getElement(self, (By.XPATH, "//*[contains(@class, 'window_header')]")).click()

    def close_edit_press(self):
        getElement(self, WarehouseManagementPage.CLOSE_EDIT_BUTTON).click()

    def confirm_doc_press(self):
        self.driver.execute_script("scrollBy(0,250);")
        element = getElement(self, WarehouseManagementPage.CONFIRM_DOC_BUTTON)
        element.click()
        
    def first_doc_select(self):
        getElement(self,(By.XPATH, "//div[2]/table/tbody/tr[1]")).click()
        

    
