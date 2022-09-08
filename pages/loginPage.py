from selenium.webdriver.common.by import By

class LoginPage:
  LOGIN_INPUT = (By.ID, "username-parameter")
  PASSWORD_INPUT = (By.ID, "password-parameter")
  BUTTON_LOGIN = (By.XPATH, "/html/body/div/div[3]/div[2]/form/div[2]/button/span")
  BUTTON_ZALOGUJ = (By.XPATH, "/html/body/div/div[3]/div[2]/form/div[3]/button/span")
  SELECT_SHOP =(By.CSS_SELECTOR, "[style^='display: list-item']")
  INPUT_SHOP = (By.ID, "id2_title")
  BUTTON_LOGOUT = (By.XPATH, "//*[text()[contains(.,'Wyloguj')]]") 
  RELOG_IFRAME = (By.TAG_NAME, "iframe")
  

  def login_pass(self, userLogin):
    self.driver.find_element(*LoginPage.LOGIN_INPUT).send_keys(userLogin)
    
  def password_pass(self, userPassword):
    self.driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(userPassword)

  def login_button_press(self):
    self.driver.find_element(*LoginPage.BUTTON_LOGIN).click()

  def login_test_check(self):
    button = self.driver.find_element(*LoginPage.BUTTON_ZALOGUJ)
    return button

  def logout_test_check(self):
    button = self.driver.find_element(*LoginPage.BUTTON_LOGIN)
    return button

  def zaloguj_button_press(self):
    self.driver.find_element(*LoginPage.BUTTON_ZALOGUJ).click()

  def logout_press(self):
    self.driver.switch_to.frame(self.driver.find_element(*LoginPage.RELOG_IFRAME))
    self.driver.find_element(*LoginPage.BUTTON_LOGOUT).click()


