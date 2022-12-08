from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from tests.configTest import getElement
from datetime import datetime 
import time



class OrdersPage:
  RELOG_IFRAME = (By.TAG_NAME, "iframe")
  PREPARE_ORDER_BUTTON = (By.XPATH, "//*[text()[contains(.,'+ Przygotuj zamówienie')]]") 
  REPLENISH_ASSORTMENT_BUTTON = (By.XPATH, "//*[text()[contains(.,'+ Uzupełnij asortyment')]]") 
  PREPARE_ORDER_TITLE = (By.XPATH, "//*[text()[contains(.,'Zamówienia w przygotowaniu')]]")
  ORDER_IN_FUTURE_TITLE = (By.XPATH, "//div[text()[contains(.,'Zamówienia w przyszłość')]]")
  ORDER_FROM_SCANNER_TITLE = (By.XPATH, "//*[text()[contains(.,'ZAMÓWIENIE - DOSTĘPNE PLIKI SKANERA')]]") 
  ORDER_LIST_FIRST_ORDER = (By.CSS_SELECTOR, "tr.odd:nth-child(1) > td:nth-child(4)") 
  ORDER_LIST_FIRST_ORDER_CHECKBOX = (By.XPATH, "//table/tbody/tr[1]/td[1]/div/input") 
  ORDER_LIST_SHIPMENT = (By.XPATH, "//*[text()[contains(.,'Zlecono wysłanie')]]")
  ORDER_LIST_MENU = (By.CLASS_NAME,  "ESOperations")
  ORDER_LIST_MENU_SEND = (By.XPATH, "//option[text()[contains(.,'Zatwierdź/Zleć wysyłkę')]]")
  ORDER_LIST_MENU_PRINT = (By.XPATH, "//option[text()[contains(.,'Drukuj zaznaczone pozycje')]]")
  ORDER_LIST_MENU_DELETE = (By.XPATH, "//option[text()[contains(.,'Usuń')]]")
  ORDER_LIST_MENU_NULL = (By.XPATH, "//option[text()[contains(.,'Co zrobic z zaznaczonymi...')]]")
  SEND_ORDER_INSIDE_ORDER_BUTTON = (By.XPATH, "//*[text()[contains(.,'Złóż zamówienie')]]")
  EXECUTE_BUTTON = (By.CSS_SELECTOR, "[value^='Wykonaj']")
  CONFIRM_BUTTON = (By.CSS_SELECTOR, "[value^='Zatwierdź']")
  RUN_TASK_BUTTON = (By.CSS_SELECTOR, "[value^='Uruchom Zadanie']")
  CLOSE_BUTTON = (By.XPATH, "//*[contains(@value, 'Zamknij')]")
  ORDER_IN_FUTURE_BUTTON = (By.XPATH, "//*[text()[contains(.,'Zamówienie w przyszłość')]]")
  ORDER_IN_FUTURE_DATA_INPUT = (By.CLASS_NAME, "hasDatepicker")
  ACTIVE_DATE_PICK = (By.CSS_SELECTOR, "a.ui-state-active")
  ORDER_FROM_SCANER_TAB = (By.XPATH, "//*[text()[contains(.,'Zamów ze skanera lub pliku')]]")
  LOAD_FILE_BUTTON = (By.XPATH, "//*[text()[contains(.,'Wczytaj plik')]]")
  LOAD_SCANNER_BUTTON = (By.XPATH, "//*[text()[contains(.,'Prześlij plik ze skanera')]]")
  SELECT_FILE = (By.CLASS_NAME, 'ml1')
  SELECT_PATH_SCANNER = (By.XPATH, './/span[2]/div[3]/table/tbody/tr/td[2]/div/span/select') 
  SEARCH_BUTTON = (By.XPATH, "//*[text()[contains(.,'Szukaj')]]") 
  FIND_ORDER_MENU_C4_PICK_CHECKBOX = (By.XPATH, "//input[contains(@name, ':model.carrefourPickOrders')]")
  FIND_ORDER_MENU_C4_CROSS_CHECKBOX = (By.XPATH, "//input[contains(@name, ':model.carrefourCrossOrders')]")
  FIND_ORDER_MENU_C4_EXTERNAL_CHECKBOX = (By.XPATH, "//input[contains(@name, ':model.externalOrders')]")
  FIND_ORDER_MENU_C4_LOCAL_CHECKBOX = (By.XPATH, "//input[contains(@name, ':model.localOrders')]")
  FIND_ORDER_MENU_SOURCE_ORDER = (By.XPATH, "//*[contains(@class, 'cb_criteria source')]")
  FIND_ORDER_MENU_SOURCE_ORDER_FROM_USER = (By.XPATH, "//*[text()[contains(.,'Ręczne')]]")
  FIND_ORDER_MENU_SOURCE_ORDER_FROM_SCANNER = (By.XPATH, "//*[text()[contains(.,'Z pliku_Skaner')]]")
  FIND_ORDER_MENU_SOURCE_ORDER_CENTRAL = (By.XPATH, "//*[text()[contains(.,'Centralne')]]")
  FIND_ORDER_MENU_SOURCE_ORDER_FROM_FRANET = (By.XPATH, "//*[text()[contains(.,'Z pliku_Franet')]]")
  FIND_ORDER_MENU_SOURCE_ORDER_AUTOMATIC = (By.XPATH, "//*[text()[contains(.,'Automat')]][contains(@id, 'select2')]")
  FIND_ORDER_MENU_DATE_FROM_INPUT = (By.XPATH, "//*[contains(@name, ':orderFrom:datePicker')]")
  FIND_ORDER_MENU_DATE_TO_INPUT = (By.XPATH, "//*[contains(@name, ':orderTo:datePicker')]")
  FIND_ORDER_MENU_DELIVERY_FROM_INPUT = (By.XPATH, "//*[contains(@name, ':deliveryFrom')]")
  FIND_ORDER_MENU_DELIVERY_TO_INPUT = (By.XPATH, "//*[contains(@name, ':deliveryTo')]")
  FIND_ORDER_MENU_SUPPLIER_SELECT = (By.XPATH, "//span[text()[contains(.,'Dostawca')]]") 
  FIND_ORDER_MENU_USER_SELECT = (By.XPATH, "//span[text()[contains(.,'Użytkownik')]]") 
  FIND_ORDER_MENU_ARTICLE_CODE_INPUT = (By.XPATH, "//*[contains(@placeholder, 'Kod towaru...')]")
  FIND_ORDER_MENU_ARTICLE_GROUP_SELECT = (By.XPATH, "//span[text()[contains(.,'Wybierz dział')]]") 
  FIND_ORDER_MENU_DOC_SYMBOL_INPUT = (By.XPATH, "//*[contains(@placeholder, 'Symbol zamówienia...')]")
  FIND_ORDER_MENU_STATUS = (By.XPATH, "//*[contains(@class, 'cb_criteria status')]")
  FIND_ORDER_MENU_STATUS_ACCEPTED = (By.XPATH, "//*[text()[contains(.,'Zaakceptowane')]][contains(@role, 'option')]")
  FIND_ORDER_MENU_STATUS_SENT = (By.XPATH, "//*[text()[contains(.,'Wysłane')]][contains(@role, 'option')]")
  FIND_ORDER_MENU_STATUS_TO_SEND = (By.XPATH, "//*[text()[contains(.,'Do wysłania')]][contains(@role, 'option')]")

  def prepare_order_press(self):
    getElement(self, OrdersPage.PREPARE_ORDER_BUTTON).click()

  def prepare_order_check(self):
    return getElement(self, OrdersPage.PREPARE_ORDER_TITLE)

  def first_order_press(self):
    actionChains = ActionChains(self.driver)
    order = getElement(self, OrdersPage.ORDER_LIST_FIRST_ORDER)
    actionChains.double_click(order).perform()

  def send_order_inside_order_button_press(self):
    getElement(self, OrdersPage.SEND_ORDER_INSIDE_ORDER_BUTTON).click()

  def execute_operation(self):
    getElement(self, OrdersPage.EXECUTE_BUTTON).click()

  def close_operation(self):
    getElement(self, OrdersPage.CLOSE_BUTTON).click()
    
  def replenish_assortment_press(self):  
    getElement(self, OrdersPage.REPLENISH_ASSORTMENT_BUTTON).click()

  def order_in_future_press(self):
    getElement(self, OrdersPage.ORDER_IN_FUTURE_BUTTON).click()

  def order_in_future_input_send(self, data):
    getElement(self, OrdersPage.ORDER_IN_FUTURE_DATA_INPUT).send_keys(data)

  def active_date_select(self):
    getElement(self, OrdersPage.ACTIVE_DATE_PICK).click()
  
  def prepare_order_in_future_check(self):
    return getElement(self, OrdersPage.ORDER_IN_FUTURE_TITLE)

  def order_list_sort_by_shipment(self):
    getElement(self, OrdersPage.ORDER_LIST_SHIPMENT).click()

  def tab_order_from_scanner_press(self):
    getElement(self, OrdersPage.ORDER_FROM_SCANER_TAB).click()

  def load_file_button_press(self):
    getElement(self, OrdersPage.LOAD_FILE_BUTTON).click()
    
  def load_scanner_button_press(self):
    getElement(self, OrdersPage.LOAD_SCANNER_BUTTON).click()

  def select_file(self, orderFile) :
    getElement(self, OrdersPage.SELECT_FILE).send_keys(orderFile) 

  def confirm_button_press(self):
    getElement(self, OrdersPage.CONFIRM_BUTTON).click()

  def run_task_press(self):
    getElement(self, OrdersPage.RUN_TASK_BUTTON).click()

  def prepare_order_from_scanner_check(self):
    return getElement(self, OrdersPage.ORDER_FROM_SCANNER_TITLE)

  def send_order_from_file_check(self):
    return getElement(self, (By.XPATH, "//*[text()[contains(.,'Generowanie zamówień zakończyło się.')]]")) 

  def order_from_scanner_icon_press(self, file_name):
    checkbox = getElement(self, (By.XPATH, f"//*[text()[contains(.,'{file_name}')]]"))
    parent = checkbox.find_element(By.XPATH, ".//ancestor::tr")
    icon = parent.find_element(By.XPATH, ".//*[@title='Dodaj nowe zamówienie z pliku skanera']")
    icon.click()

  def select_path_scanner(self):
    select = getElement(self, OrdersPage.SELECT_PATH_SCANNER)
    value = select.find_element(By.XPATH,".//option[2]")
    value.click()  

  def find_order_menu_date_from_send_keys(self, date = '14.09.2022'):
    input = getElement(self, OrdersPage.FIND_ORDER_MENU_DATE_FROM_INPUT)
    input.clear()
    input.send_keys(date) 
    getElement(self,(By.CLASS_NAME, 'tableHeadPanel')).click()

  def find_order_menu_date_to_send_keys(self, date = '14.09.2022'):
    input = getElement(self, OrdersPage.FIND_ORDER_MENU_DATE_TO_INPUT)
    input.clear()
    input.send_keys(date) 
    getElement(self,(By.CLASS_NAME, 'tableHeadPanel')).click()

  def find_order_menu_delivery_from_send_keys(self, date = '14.09.2022'):
    input = getElement(self, OrdersPage.FIND_ORDER_MENU_DELIVERY_FROM_INPUT)
    input.clear()
    input.send_keys(date)
    getElement(self,(By.CLASS_NAME, 'tableHeadPanel')).click()

  def find_order_menu_delivery_to_send_keys(self, date = '14.09.2022'):
    input = getElement(self, OrdersPage.FIND_ORDER_MENU_DELIVERY_TO_INPUT)
    input.clear()
    input.send_keys(date) 
    getElement(self,(By.CLASS_NAME, 'tableHeadPanel')).click()

  def search_button_press(self, tomorrow = "2022-09-14"):
    getElement(self, OrdersPage.SEARCH_BUTTON).click()
    if tomorrow:
      for x in range(10):
        data = getElement(self, (By.XPATH, "//table/tbody/tr[1]/td[4]/div")).get_attribute('innerHTML')
        a = datetime.strptime(tomorrow, "%Y-%m-%d")
        b = datetime.strptime(data, "%Y-%m-%d")
        if (b > a):
            break
        time.sleep(1)

  def order_list_first_order_checkbox_press(self):
    getElement(self, OrdersPage.ORDER_LIST_FIRST_ORDER_CHECKBOX).click()

  def order_list_menu_select_option(self, option):
    getElement(self, OrdersPage.ORDER_LIST_MENU).click()
    getElement(self, option).click()

  def set_quantity_of_first_article(self, quantity):
    input = getElement(self, (By.XPATH, "//table/tbody/tr/td[6]/div/input"))
    input.clear()
    input.send_keys(quantity) 

  def find_order_menu_checkbox_press(self, locator = (By.XPATH, "//input[contains(@name, ':model.carrefourPickOrders')]")):
    getElement(self, locator).click()

  def find_order_menu_source_select(self, source):
    getElement(self, OrdersPage.FIND_ORDER_MENU_SOURCE_ORDER).click()
    if source == OrdersPage.FIND_ORDER_MENU_SOURCE_ORDER_FROM_USER:
      element_to_hover_over = getElement(self, OrdersPage.FIND_ORDER_MENU_SOURCE_ORDER_CENTRAL)
      hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
      hover.perform()
    element = getElement(self, source)
    element.click()

  def find_order_menu_supplier_select(self, supplier = '9790'):
    getElement(self, OrdersPage.FIND_ORDER_MENU_SUPPLIER_SELECT).click()
    getElement(self, (By.XPATH, f"//*[text()[contains(.,'{supplier}')]]")).click()

  def find_order_menu_user_select(self, user = "AdminF.001"):
    getElement(self, OrdersPage.FIND_ORDER_MENU_USER_SELECT).click()
    getElement(self, (By.XPATH, f"//*[text()[contains(.,'{user}')]]")).click()
    
  def find_order_menu_article_code_select(self, code = '684804'):
    input = getElement(self, OrdersPage.FIND_ORDER_MENU_ARTICLE_CODE_INPUT)
    input.clear()
    input.send_keys(code) 

  def find_order_menu_doc_symbol_select(self, doc_symbol = '123456'):
    input = getElement(self, OrdersPage.FIND_ORDER_MENU_DOC_SYMBOL_INPUT)
    input.clear()
    input.send_keys(doc_symbol) 

  def find_order_menu_article_group_select(self, group = "10 NAPOJE"):
    getElement(self, OrdersPage.FIND_ORDER_MENU_ARTICLE_GROUP_SELECT).click()
    getElement(self, (By.XPATH, f"//*[text()[contains(.,'{group}')]]")).click()

  def find_order_menu_status_select(self, status):
    getElement(self, OrdersPage.FIND_ORDER_MENU_STATUS).click()
    if status == OrdersPage.FIND_ORDER_MENU_STATUS_TO_SEND:
      element_to_hover_over = getElement(self, OrdersPage.FIND_ORDER_MENU_STATUS_ACCEPTED)
      hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
      hover.perform()
    element = getElement(self, status)
    element.click()