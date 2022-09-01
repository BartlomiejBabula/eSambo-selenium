from selenium.webdriver.common.by import By

class HomePage:
  RELOG_IFRAME = (By.TAG_NAME, "iframe")
  ARTICLES_BUTTON = (By.CLASS_NAME, "F2articles")
  ORDERS_BUTTON = (By.XPATH, "//*[text()[contains(.,'Zamówienia')]]")
  ORDERS_PREPARE_MENU = (By.XPATH, "//*[text()[contains(.,'W przygotowaniu')]]")

  def articles_press(self):
    self.driver.switch_to.frame(self.driver.find_element(*HomePage.RELOG_IFRAME))
    button = self.driver.find_element(*HomePage.ARTICLES_BUTTON)
    button.click()

  def orders_press(self):
    button = self.driver.find_element(*HomePage.ORDERS_BUTTON)
    button.click()

  def orders_prepare_press(self):
    button = self.driver.find_element(*HomePage.ORDERS_PREPARE_MENU)
    button.click()
    