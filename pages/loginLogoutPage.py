from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller

class LoginLogoutPage:
  LOGIN_INPUT = (By.ID, "username-parameter")
  PASSWORD_INPUT = (By.ID, "password-parameter")
  BUTTON_LOGIN = (By.XPATH, "/html/body/div/div[3]/div[2]/form/div[2]/button/span")
  BUTTON_ZALOGUJ = (By.XPATH, "/html/body/div/div[3]/div[2]/form/div[3]/button/span")
  SELECT_SHOP =(By.CSS_SELECTOR, "[style^='display: list-item']")
  INPUT_SHOP = (By.ID, "id2_title")
  BUTTON_LOGOUT = (By.XPATH, "//*[text()[contains(.,'Wyloguj')]]") 
  RELOG_IFRAME = (By.TAG_NAME, "iframe")

  def login_pass(self, userLogin):
    login = self.driver.find_element(*LoginLogoutPage.LOGIN_INPUT)
    login.send_keys(userLogin)
    
  def password_pass(self, userPassword):
    password = self.driver.find_element(*LoginLogoutPage.PASSWORD_INPUT)
    password.send_keys(userPassword)

  def login_button_press(self):
    button = self.driver.find_element(*LoginLogoutPage.BUTTON_LOGIN)
    button.click()
    return button

  def login_test_check(self):
    button = self.driver.find_element(*LoginLogoutPage.BUTTON_ZALOGUJ)
    return button

  def zaloguj_button_press(self):
    button = self.driver.find_element(*LoginLogoutPage.BUTTON_ZALOGUJ)
    button.click()

  def select_shop(self, shop):
    input = self.driver.find_element(*LoginLogoutPage.INPUT_SHOP)
    input.click()
    keyboard = Controller()
    keyboard.type(shop)
    select = self.driver.find_element(*LoginLogoutPage.SELECT_SHOP)
    select.click()

  def logout_press(self):
    self.driver.switch_to.frame(self.driver.find_element(*LoginLogoutPage.RELOG_IFRAME))
    button = self.driver.find_element(*LoginLogoutPage.BUTTON_LOGOUT)
    button.click()
