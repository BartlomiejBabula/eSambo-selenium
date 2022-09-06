from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from tests.configTest import getElement



class OrdersPage:
  RELOG_IFRAME = (By.TAG_NAME, "iframe")
  PREPARE_ORDER_BUTTON = (By.XPATH, "//*[text()[contains(.,'+ Przygotuj zamówienie')]]") 
  REPLENISH_ASSORTMENT_BUTTON = (By.XPATH, "//*[text()[contains(.,'+ Uzupełnij asortyment')]]") 
  PREPARE_ORDER_TITLE = (By.XPATH, "//*[text()[contains(.,'Zamówienia w przygotowaniu')]]")
  ORDER_IN_FUTURE_TITLE = (By.XPATH, "//div[text()[contains(.,'Zamówienia w przyszłość')]]")
  ORDER_FROM_SCANNER_TITLE = (By.XPATH, "//*[text()[contains(.,'ZAMÓWIENIE - DOSTĘPNE PLIKI SKANERA')]]") 
  ORDER_LIST_FIRST_ORDER = (By.CSS_SELECTOR, "tr.odd:nth-child(1) > td:nth-child(4)") 
  ORDER_LIST_SHIPMENT = (By.XPATH, "//*[text()[contains(.,'Zlecono wysłanie')]]")
  SEND_ORDER_INSIDE_ORDER_BUTTON = (By.XPATH, "//*[text()[contains(.,'Złóż zamówienie')]]")
  WYKONAJ_BUTTON = (By.CSS_SELECTOR, "[value^='Wykonaj']")
  CONFIRM_BUTTON = (By.CSS_SELECTOR, "[value^='Zatwierdź']")
  RUN_TASK_BUTTON = (By.CSS_SELECTOR, "[value^='Uruchom Zadanie']")
  CLOSE_BUTTON =(By.CSS_SELECTOR, "[value^='Zamknij']")
  ORDER_IN_FUTURE_BUTTON = (By.XPATH, "//*[text()[contains(.,'Zamówienie w przyszłość')]]")
  ORDER_IN_FUTURE_DATA_INPUT = (By.CLASS_NAME, "hasDatepicker")
  ACTIVE_DATE_PICK = (By.CSS_SELECTOR, "a.ui-state-active")
  ORDER_FROM_SCANER_TAB = (By.XPATH, "//*[text()[contains(.,'Zamów ze skanera lub pliku')]]")
  LOAD_FILE_BUTTON =(By.XPATH, "//*[text()[contains(.,'Wczytaj plik')]]")
  LOAD_SCANNER_BUTTON =(By.XPATH, "//*[text()[contains(.,'Prześlij plik ze skanera')]]")
  SELECT_FILE=(By.CLASS_NAME, 'ml1')
  SELECT_PATH_SCANNER=(By.XPATH, './/span[2]/div[3]/table/tbody/tr/td[2]/div/span/select')
  REFRESH_BUTTON =(By.XPATH, "//*[text()[contains(.,'Odśwież ręcznie')]]")
  


  def prepare_order_press(self):
    button = getElement(self, OrdersPage.PREPARE_ORDER_BUTTON)
    button.click()

  def prepare_order_check(self):
    check = getElement(self, OrdersPage.PREPARE_ORDER_TITLE)
    return check

  def first_order_press(self):
    actionChains = ActionChains(self.driver)
    order = getElement(self, OrdersPage.ORDER_LIST_FIRST_ORDER)
    actionChains.double_click(order).perform()

  def send_order_inside_order_button_press(self):
    button = getElement(self, OrdersPage.SEND_ORDER_INSIDE_ORDER_BUTTON)
    button.click()

  def send_operation(self):
    button = getElement(self, OrdersPage.WYKONAJ_BUTTON)
    button.click()

  def close_operation(self):
    button = getElement(self, OrdersPage.CLOSE_BUTTON)
    button.click()
    
  def replenish_assortment_press(self):  
    button = getElement(self, OrdersPage.REPLENISH_ASSORTMENT_BUTTON)
    button.click()

  def order_in_future_press(self):
    button = getElement(self, OrdersPage.ORDER_IN_FUTURE_BUTTON)
    button.click()

  def order_in_future_input_send(self, data):
    input = getElement(self, OrdersPage.ORDER_IN_FUTURE_DATA_INPUT)
    input.send_keys(data)

  def active_date_select(self):
    button = getElement(self, OrdersPage.ACTIVE_DATE_PICK)
    button.click()

  def prepare_order_in_future_check(self):
    check = getElement(self, OrdersPage.ORDER_IN_FUTURE_TITLE)
    return check

  def order_list_sort_by_shipment(self):
    button = getElement(self, OrdersPage.ORDER_LIST_SHIPMENT)
    button.click()

  def tab_order_from_scanner_press(self):
    button = getElement(self, OrdersPage.ORDER_FROM_SCANER_TAB)
    button.click()

  def load_file_button_press(self):
    button = getElement(self, OrdersPage.LOAD_FILE_BUTTON)
    button.click()

  def load_scanner_button_press(self):
    button = getElement(self, OrdersPage.LOAD_SCANNER_BUTTON)
    button.click()

  def select_file(self, orderFile) :
    button = getElement(self, OrdersPage.SELECT_FILE)   
    button.send_keys(orderFile)

  def confirm_button_press(self):
    button = getElement(self, OrdersPage.CONFIRM_BUTTON)
    button.click()

  def run_task_press(self):
    button = getElement(self, OrdersPage.RUN_TASK_BUTTON)
    button.click()

  def prepare_order_from_scanner_check(self):
    check = getElement(self, OrdersPage.ORDER_FROM_SCANNER_TITLE)
    return check

  def send_order_from_file_check(self):
    check = getElement(self, (By.XPATH, "//*[text()[contains(.,'Generowanie zamówień zakończyło się.')]]")) 
    return check

  def order_from_scanner_icon_press(self, file_name):
    checkbox = getElement(self, (By.XPATH, f"//*[text()[contains(.,'{file_name}')]]"))
    parent = checkbox.find_element(By.XPATH, ".//ancestor::tr")
    icon = parent.find_element(By.XPATH, ".//*[@title='Dodaj nowe zamówienie z pliku skanera']")
    icon.click()

  def select_path_scanner(self):
    select = getElement(self, OrdersPage.SELECT_PATH_SCANNER)
    value = select.find_element(By.XPATH,".//option[2]")
    value.click()  

  def refresh_press(self):
    button = getElement(self, OrdersPage.REFRESH_BUTTON)
    button.click()
