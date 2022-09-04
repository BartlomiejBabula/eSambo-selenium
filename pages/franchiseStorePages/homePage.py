from selenium.webdriver.common.by import By
from tests.configTest import getElement

class HomePage:
  RELOG_IFRAME = (By.TAG_NAME, "iframe")
  ARTICLES_BUTTON = (By.CLASS_NAME, "F2articles")
  ORDERS_BUTTON = (By.XPATH, "//*[text()[contains(.,'Zamówienia')]]")
  ORDERS_MENU_PREPARE_ORDERS = (By.XPATH, "//*[text()[contains(.,'W przygotowaniu')]]")
  ORDERS_MENU_ORDERS_IN_FUTURE = (By.XPATH, "//*[text()[contains(.,'Zamówienia w przyszłość')]]")
  ORDERS_MENU_SCANNER_ORDERS = (By.XPATH, "/html/body/form/div[4]/div[1]/div[1]/div[2]/ul/li[5]/ul/div/li[2]/div/ul/li[3]/a/span")


  def articles_press(self):
    self.driver.switch_to.frame(self.driver.find_element(*HomePage.RELOG_IFRAME))
    button = getElement(self, HomePage.ARTICLES_BUTTON)
    button.click()

  def orders_press(self):
    button = getElement(self, HomePage.ORDERS_BUTTON)
    button.click()

  def orders_prepare_press(self):
    button = getElement(self, HomePage.ORDERS_MENU_PREPARE_ORDERS)
    button.click()

  def orders_in_future_press(self):
    button = getElement(self, HomePage.ORDERS_MENU_ORDERS_IN_FUTURE)
    button.click()

  def orders_from_scanner_press(self):
    button = getElement(self, HomePage.ORDERS_MENU_SCANNER_ORDERS)
    button.click() 
    