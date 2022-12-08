from requests import get
from selenium.webdriver.common.by import By
from tests.configTest import getElement



class WarehouseManagementPage:
    CREATE_NEW_DOC_BUTTON = (By.XPATH, "//*[text()[contains(.,'Utwórz nowy dokument')]]")
    DELIVERY_STATUS_PREPARED_BUTTON = (By.XPATH, "//div[contains(@class, 'deliveryStructureTree')]/table[6]")
    KPZ_STATUS_PREPARED_BUTTON = (By.XPATH, "//div[contains(@class, 'deliveryStructureTree')]/table[9]")
    PZZ_STATUS_PREPARED_BUTTON = (By.XPATH, "//div[contains(@class, 'deliveryStructureTree')]/table[15]")
    DELIVERY_CREATE_NEW_DOC_MENU_PZ_WITHOUT_ORDER_BUTTON = (By.XPATH, "//button[text()[contains(.,'PZ bez zamówienia')]]")
    DELIVERY_CREATE_NEW_DOC_MENU_KPZ_BUTTON = (By.XPATH, "//*[text()[contains(.,'Korektę KPZ')]]")
    DELIVERY_CREATE_NEW_DOC_MENU_PZZ_BUTTON = (By.XPATH, "//button/span[text()[contains(.,'PZZ')]]")
    DELIVERY_DOC_BASIS_OF_THE_DOC_INPUT = (By.XPATH, "//input[contains(@name, ':documentData:tabs:panel:documentFields:docDeliveryPZ')][contains(@type, 'text')]")
    DELIVERY_DOC_SUPPLIER_INPUT = (By.XPATH, "//input[contains(@name, ':supplier.orgUnit')]")
    DELIVERY_DOC_SUPPLIER_SEARCH_ICON = (By.XPATH, "//td[contains(@class, 'lookup')]")
    CLOSE_EDIT_BUTTON = (By.XPATH, "//*[text()[contains(.,'Zakończ edycję')]]")
    CONFIRM_DOC_BUTTON = (By.XPATH, "//*[text()[contains(.,'Zatwierdź')]]")
    KPZ_DELIVERY_DOC = (By.CSS_SELECTOR, ".docRelatedSymbol span.find a")
    KPZ_DOC_DELIVERY_INPUT = (By.CSS_SELECTOR, ".docDelivery .field input")
    KPZ_DOC_DELIVERY_DATE_INPUT = (By.CSS_SELECTOR, ".docDeliveryDate input")
    OPERATION_MENU = (By.XPATH, "//*[text()[contains(.,'Operacje')]]")
    OPERATION_MENU_ADD_ITEM_DELIVERY = (By.CSS_SELECTOR, "li.operation-addItemDelivery")
    PZZ_NR_DOC_WZ_INPUT = (By.CSS_SELECTOR, '.docDelivery input')
    PZZ_DELIVERY_DATE_INPUT = (By.CSS_SELECTOR, '.deliveryDate input')
    PZZ_SUPPLIER_SEARCH_INPUT = (By.CSS_SELECTOR, '.supplier-orgUnit-fullName input')
    PZZ_SUPPLIER_SEARCH_ICON = (By.CSS_SELECTOR, '.supplier-orgUnit-fullName a')
    PZZ_SUPPLIER_DEPARTMENT_SELECT = (By.CSS_SELECTOR, '.supplier select')
    PZZ_SUPPLIER_DEPARTMENT_SELECT_OPTION = (By.XPATH, "//*[text()[contains(.,'PIWO')]]")
    PZZ_FIRST_ARTICLE_NAME_INPUT = (By.XPATH, "//tr[1]/td[contains(@class, 'nameOfGood')]//input")
    PZZ_FIRST_ARTICLE_NAME_SEARCH_ICON = (By.XPATH, "//tr[1]/td[contains(@class, 'nameOfGood')]//a")
    PZZ_FIRST_ARTICLE_QUANTITY_INPUT = (By.XPATH, "//tr[1]/td[contains(@class, 'supplierQuantity')]//input")
    RESET_CONTENT = (By.CSS_SELECTOR, "div.content")



    def delivery_create_new_doc_button_press(self):
        getElement(self, WarehouseManagementPage.CREATE_NEW_DOC_BUTTON).click()

    def delivery_status_prepared_button_press(self):
        getElement(self, WarehouseManagementPage.DELIVERY_STATUS_PREPARED_BUTTON).click()

    def KPZ_status_prepared_button_press(self):
        getElement(self, WarehouseManagementPage.KPZ_STATUS_PREPARED_BUTTON).click()

    def PZZ_status_prepared_button_press(self):
        getElement(self, WarehouseManagementPage.PZZ_STATUS_PREPARED_BUTTON).click()

    def delivery_create_new_doc_menu_pz_without_order(self):
        getElement(self, WarehouseManagementPage.DELIVERY_CREATE_NEW_DOC_MENU_PZ_WITHOUT_ORDER_BUTTON).click()

    def delivery_create_new_doc_menu_kpz_press(self):
        getElement(self, WarehouseManagementPage.DELIVERY_CREATE_NEW_DOC_MENU_KPZ_BUTTON).click()

    def delivery_create_new_doc_menu_pzz_press(self):
        getElement(self, WarehouseManagementPage.DELIVERY_CREATE_NEW_DOC_MENU_PZZ_BUTTON).click()

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
        
    def KPZ_delivery_doc_find_press(self):
        getElement(self, WarehouseManagementPage.KPZ_DELIVERY_DOC).click()

    def KPZ_first_delivery_doc_select(self):
        getElement(self, (By.XPATH, "//div/span/div[1]/span/div/table/tbody/tr[1]/td")).click()

    def KPZ_delivery_doc_input_send_key(self):
        getElement(self, WarehouseManagementPage.KPZ_DOC_DELIVERY_INPUT).send_keys("automatic.test")
        getElement(self, WarehouseManagementPage.RESET_CONTENT).click()

    def KPZ_delivery_doc_date_input_send_key(self, date = '09.10.2022'):
        input = getElement(self, WarehouseManagementPage.KPZ_DOC_DELIVERY_DATE_INPUT)
        input.send_keys(date)
        getElement(self, WarehouseManagementPage.RESET_CONTENT).click()

    def operation_menu_press(self):
        getElement(self, WarehouseManagementPage.OPERATION_MENU).click()

    def operation_menu_add_item_delivery_press(self):
        getElement(self, WarehouseManagementPage.OPERATION_MENU_ADD_ITEM_DELIVERY).click()

    def KPZ_first_article_press(self):
        getElement(self, (By.XPATH, "//div/span/div[1]/span/table/tbody/tr/td[1]/span/input")).click()

    def KPZ_article_quantity_send_key(self, quantity):
        input = getElement(self, (By.CSS_SELECTOR, ".tabColumnQuantity input"))
        input.clear()
        getElement(self, WarehouseManagementPage.RESET_CONTENT).click()
        input.send_keys(quantity)
        getElement(self, WarehouseManagementPage.RESET_CONTENT).click()

    def operation_menu_confirm_press(self):
        getElement(self, (By.CSS_SELECTOR, "[value^='Zatwierdź']")).click()

    def PZZ_nr_doc_wz_send_key(self):
        getElement(self, WarehouseManagementPage.PZZ_NR_DOC_WZ_INPUT).send_keys("automatic.test")
        getElement(self, WarehouseManagementPage.RESET_CONTENT).click()

    def PZZ_delivery_date_input_send_key(self, date = '09.10.2022'):
        input = getElement(self, WarehouseManagementPage.PZZ_DELIVERY_DATE_INPUT)
        input.send_keys(date)
        getElement(self, WarehouseManagementPage.RESET_CONTENT).click()

    def PZZ_supplier_select(self):
        getElement(self, WarehouseManagementPage.PZZ_SUPPLIER_SEARCH_INPUT).send_keys("348")
        getElement(self, WarehouseManagementPage.RESET_CONTENT).click()
        getElement(self, WarehouseManagementPage.PZZ_SUPPLIER_SEARCH_ICON).click()

    def PZZ_supplier_department_select(self):
        getElement(self, WarehouseManagementPage.PZZ_SUPPLIER_DEPARTMENT_SELECT).click()
        getElement(self, WarehouseManagementPage.PZZ_SUPPLIER_DEPARTMENT_SELECT_OPTION).click()

    def PZZ_firts_element_supplier_article_name_select(self):
        getElement(self, WarehouseManagementPage.PZZ_FIRST_ARTICLE_NAME_INPUT).send_keys("1242529")
        getElement(self, WarehouseManagementPage.RESET_CONTENT).click()
        getElement(self, WarehouseManagementPage.PZZ_FIRST_ARTICLE_NAME_SEARCH_ICON).click()

    def PZZ_firts_element_quantity_send_keys(self, quantity = '1'):
        getElement(self, WarehouseManagementPage.PZZ_FIRST_ARTICLE_QUANTITY_INPUT).send_keys(quantity)
        getElement(self, WarehouseManagementPage.RESET_CONTENT).click()


