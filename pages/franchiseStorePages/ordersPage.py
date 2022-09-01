from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class OrdersPage:
  RELOG_IFRAME = (By.TAG_NAME, "iframe")
  RELOG_MODAL = (By.CLASS_NAME, "visuraloverlaycontent")
  PREPARE_ORDER = (By.XPATH, "//*[text()[contains(.,'+ Przygotuj zamówienie')]]") 
  PREPARE_ORDER_CHECK = (By.XPATH, "//*[text()[contains(.,'Zamówienia w przygotowaniu')]]")
  FIRST_ORDER = (By.CSS_SELECTOR, "tr.odd:nth-child(1) > td:nth-child(6)") 
  SEND_ORDER_INSIDE_ORDER_BUTTON = (By.XPATH, "//*[text()[contains(.,'Złóż zamówienie')]]")
  WYKONAJ_BUTTON = (By.CSS_SELECTOR, "[value^='Wykonaj']")
  CLOSE_BUTTON =(By.CSS_SELECTOR, "[value^='Zamknij']")

  

  def prepare_order_press(self):
    button = self.driver.find_element(*OrdersPage.PREPARE_ORDER)
    button.click()

  def prepare_order_check(self):
    check = self.driver.find_element(*OrdersPage.PREPARE_ORDER_CHECK)
    return check

  def first_order_press(self):
    actionChains = ActionChains(self.driver)
    order = self.driver.find_element(*OrdersPage.FIRST_ORDER)
    actionChains.double_click(order).perform()

  def send_order_inside_order_button_press(self):
    button = self.driver.find_element(*OrdersPage.SEND_ORDER_INSIDE_ORDER_BUTTON)
    button.click()

  def send_operation(self):
    button = self.driver.find_element(*OrdersPage.WYKONAJ_BUTTON)
    button.click()

  def close_operation(self):
    button = self.driver.find_element(*OrdersPage.CLOSE_BUTTON)
    button.click()
    
    

