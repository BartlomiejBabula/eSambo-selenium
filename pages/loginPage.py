from selenium.webdriver.common.by import By

class loginPage:
  LOGIN_INPUT = (By.ID, "username-parameter")
  PASSWORD_INPUT = (By.ID, "password-parameter")
  BUTTON_LOGIN = (By.XPATH, "/html/body/div/div[3]/div[2]/form/div[2]/button/span")
  BUTTON_ZALOGUJ = (By.XPATH, "/html/body/div/div[3]/div[2]/form/div[3]/button/span")

  def login_pass(self, userLogin):
    login = self.driver.find_element(*loginPage.LOGIN_INPUT)
    login.send_keys(userLogin)
    return login
    
  def password_pass(self, userPassword):
    password = self.driver.find_element(*loginPage.PASSWORD_INPUT)
    password.send_keys(userPassword)
    return password

  def login_button_press(self):
    button = self.driver.find_element(*loginPage.BUTTON_LOGIN)
    button.click()
    return button

  def search_zaloguj_button_press(self):
    button = self.driver.find_element(*loginPage.BUTTON_ZALOGUJ)
    return button