from selenium.webdriver.common.by import By
from tests.configTest import getElement

class HomePage:
  ARTICLES_BUTTON = (By.CLASS_NAME, "F2articles")
  CONTRACTORS_BUTTON = (By.CLASS_NAME, "F2contractors")
  COMMUNICATION_BUTTON = (By.CLASS_NAME, "F2communication")
  EPLANUS_BUTTON = (By.CLASS_NAME, "F2csra")
  TOP_REPORT_BUTTON = (By.CLASS_NAME, "F2topreport")
  TOOLS_BUTTON = (By.CLASS_NAME, "F2tools")
  CART_BUTTON = (By.XPATH, "//div[contains(@title, 'Koszyk/Tymczasowa lista towarów')]")
  CHANGE_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@title, 'Zmień hasło')]")
  HOMEPAGE_BUTTON = (By.XPATH, "//*[text()[contains(.,'Strona główna')]]")
  ADMINISTRATION_BUTTON = (By.XPATH, "//*[text()[contains(.,'Administracja')]]")
  ADMINISTRATION_STORE_BUTTON = (By.XPATH, "//*[text()[contains(.,'Sklep')]]")
  ADMINISTRATION_USERS_BUTTON = (By.XPATH, "//*[text()[contains(.,'Użytkownicy')]]")
  WAREHOUSE_MANAGEMENT_BUTTON = (By.XPATH, "//*[text()[contains(.,'Gospodarka magazynowa')]]") 
  ORDERS_BUTTON = (By.XPATH, "/html/body/form/div[4]/div[1]/div[1]/div[2]/ul/li[5]/a/span[2]")
  ORDERS_MENU_PREPARE_ORDERS = (By.XPATH, "//*[text()[contains(.,'W przygotowaniu')]]")
  ORDERS_MENU_DESKTOP_BUTTON = (By.XPATH, "//*[text()[contains(.,'Pulpit zamówień')]]") 
  ORDERS_MENU_SENT_TODAY = (By.XPATH, "//*[text()[contains(.,'Wysłane dzisiaj')]]") 
  ORDERS_MENU_SENT = (By.XPATH, "/html/body/form/div[4]/div[1]/div[1]/div[2]/ul/li[5]/ul/div/li[1]/div/ul/li[8]/a/span") 
  ORDERS_MENU_PENDING = (By.XPATH, "//*[text()[contains(.,'Zamówienia oczekujące')]]") 
  ORDERS_MENU_ACCEPTED = (By.XPATH, "//*[text()[contains(.,'Zaakceptowane')]]")  
  ORDERS_MENU_REALIZED = (By.XPATH, "//*[text()[contains(.,'Zrealizowane')]]") 
  ORDERS_MENU_UNREALIZED = (By.XPATH, "//*[text()[contains(.,'Niezrealizowane')]]")   
  ORDERS_MENU_REJECTED = (By.XPATH, "//*[text()[contains(.,'Odrzucone')]]") 
  ORDERS_MENU_ALL_SENT = (By.XPATH, "//*[text()[contains(.,'Wszystkie złożone')]]") 
  ORDERS_MENU_GENERATED_FOR_TODAY = (By.XPATH, "//*[text()[contains(.,'Zamówienia wygenerowane na dziś')]]") 
  ORDERS_MENU_SUMMARY_PENDING = (By.XPATH, "//*[text()[contains(.,'Podsumowanie zamówień oczekujących')]]") 
  ORDERS_MENU_ORDERS_IN_FUTURE = (By.XPATH, "//*[text()[contains(.,'Zamówienia w przyszłość')]]")
  ORDERS_MENU_SCANNER_ORDERS = (By.XPATH, "/html/body/form/div[4]/div[1]/div[1]/div[2]/ul/li[5]/ul/div/li[2]/div/ul/li[3]/a/span")
  ORDERS_MENU_SCANNER_OUT_OF_STOCK = (By.XPATH, "//*[text()[contains(.,'Braki')]]")
  ORDERS_MENU_SCANNER_AUTOMATIC_OUT_OF_STOCK = (By.XPATH, "//*[text()[contains(.,'Braki automatyczne')]]")
  ORDERS_MENU_SCANNER_LOG = (By.XPATH, "//*[text()[contains(.,'Dziennik zdarzeń skanera')]]")
  ORDERS_MENU_REPORT_S001 = (By.XPATH, "//*[text()[contains(.,'Sprzedaż towarów wg wartości sprzedaży (S001)')]]")
  ORDERS_MENU_REPORT_S002 = (By.XPATH, "//*[text()[contains(.,'Raport straty znanej (S002)')]]")
  ORDERS_MENU_REPORT_M013 = (By.XPATH, "//*[text()[contains(.,'Stany magazynowe na dzień z karty magazynowej (M013)')]]")
  ORDERS_MENU_REPORT_T011 = (By.XPATH, "//*[text()[contains(.,'Raport - Asortyment nieefektywny (T011)')]]")
  ORDERS_MENU_REPORT_TOP = (By.XPATH, "//*[text()[contains(.,'Top raport')]]")
  ORDERS_MENU_SELECT_OTHER_REPORT = (By.XPATH, "//*[text()[contains(.,'Wybierz inny raport')]]")
  ORDERS_MENU_SELECT_OTHER_REPORT_T015 = (By.XPATH, "//*[text()[contains(.,'Zamówienia w przyszłość - odrzucenia (T015)')]]")
  ORDERS_MENU_SELECT_OTHER_REPORT_T001 = (By.XPATH, "//*[text()[contains(.,'Parametry zamawiania towarów (T001)')]]")
  ORDERS_MENU_SELECT_OTHER_REPORT_T002 = (By.XPATH, "//*[text()[contains(.,'Analiza cen uwolnionych (promocje) (T002)')]]")
  ORDERS_MENU_SELECT_OTHER_REPORT_T003 = (By.XPATH, "//*[text()[contains(.,'Aktualnie obowiązujące zestawy  (T003)')]]")
  ORDERS_MENU_SELECT_OTHER_REPORT_T004 = (By.XPATH, "//*[text()[contains(.,'Katalog towarów - braki parametrów do zamówień (T004)')]]")
  ORDERS_MENU_SELECT_OTHER_REPORT_T005 = (By.XPATH, "//*[text()[contains(.,'Dostawcy i ceny zakupu (T005)')]]")
  ORDERS_MENU_SELECT_OTHER_REPORT_T006 = (By.XPATH, "//*[text()[contains(.,'Towary przesłane z centrali - kody ean z ostatniej transmisji (T006)')]]")
  ORDERS_MENU_SELECT_OTHER_REPORT_T007 = (By.XPATH, "//*[text()[contains(.,'Towary przesłane z centrali zmiana cen zakupów (T007)')]]")
  ORDERS_MENU_SELECT_OTHER_REPORT_T008 = (By.XPATH, "//*[text()[contains(.,'Towary przesłane z centrali w ostatniej transmisji - ceny sprzedaży (T008)')]]")
  ORDERS_MENU_SELECT_OTHER_REPORT_T009 = (By.XPATH, "//*[text()[contains(.,'Katalog towarów - parametry do zamówień (T009)')]]")

  def articles_press(self):
    getElement(self, HomePage.ARTICLES_BUTTON).click()

  def homepage_press(self):
    getElement(self, HomePage.HOMEPAGE_BUTTON).click()

  def contractors_press(self):
    getElement(self, HomePage.CONTRACTORS_BUTTON).click()

  def eplanus_press(self):
    getElement(self, HomePage.EPLANUS_BUTTON).click()

  def orders_press(self):
    getElement(self, HomePage.ORDERS_BUTTON).click()

  def top_report_press(self):
    getElement(self, HomePage.TOP_REPORT_BUTTON).click()

  def tools_press(self):
    getElement(self, HomePage.TOOLS_BUTTON).click()

  def change_password_press(self):
    getElement(self, HomePage.CHANGE_PASSWORD_BUTTON).click()

  def cart_press(self):
    getElement(self, HomePage.CART_BUTTON).click()
  
  def communication_press(self):
    getElement(self, HomePage.COMMUNICATION_BUTTON).click()

  def administration_users_press(self):
    getElement(self, HomePage.ADMINISTRATION_BUTTON).click()
    getElement(self, HomePage.ADMINISTRATION_USERS_BUTTON).click()

  def administration_store_press(self):
    getElement(self, HomePage.ADMINISTRATION_BUTTON).click()
    getElement(self, HomePage.ADMINISTRATION_STORE_BUTTON).click()

  def orders_prepare_press(self):
    getElement(self, HomePage.ORDERS_MENU_PREPARE_ORDERS).click()

  def orders_in_future_press(self):
    getElement(self, HomePage.ORDERS_MENU_ORDERS_IN_FUTURE).click()

  def orders_desktop_press(self):
    getElement(self, HomePage.ORDERS_MENU_DESKTOP_BUTTON).click()

  def orders_from_scanner_press(self):
    getElement(self, HomePage.ORDERS_MENU_SCANNER_ORDERS).click()

  def orders_menu_report_S001_press(self):
    getElement(self, HomePage.ORDERS_MENU_REPORT_S001).click()
    
  def orders_menu_report_top_press(self):
    getElement(self, HomePage.ORDERS_MENU_REPORT_TOP).click()
    
  def orders_menu_report_S002_press(self):
    getElement(self, HomePage.ORDERS_MENU_REPORT_S002).click()
    
  def orders_menu_report_M013_press(self):
    getElement(self, HomePage.ORDERS_MENU_REPORT_M013).click()

  def orders_menu_report_T011_press(self):
    getElement(self, HomePage.ORDERS_MENU_REPORT_T011).click()

  def orders_menu_select_other_report(self, locator):
    getElement(self, HomePage.ORDERS_MENU_SELECT_OTHER_REPORT).click()
    if locator:
      getElement(self, locator).click()

  def orders_sent_today_press(self):
    getElement(self, HomePage.ORDERS_MENU_SENT_TODAY).click()

  def orders_pending_press(self):
    getElement(self, HomePage.ORDERS_MENU_PENDING).click()

  def orders_generated_for_today_press(self):
    getElement(self, HomePage.ORDERS_MENU_GENERATED_FOR_TODAY).click()

  def orders_summary_pending_press(self):
    getElement(self, HomePage.ORDERS_MENU_SUMMARY_PENDING).click()

  def orders_sent_press(self):
    getElement(self, HomePage.ORDERS_MENU_SENT).click()
  
  def orders_accept_press(self):
    getElement(self, HomePage.ORDERS_MENU_ACCEPTED).click()

  def orders_realized_press(self):
    getElement(self, HomePage.ORDERS_MENU_REALIZED).click()

  def orders_unrealized_press(self):
    getElement(self, HomePage.ORDERS_MENU_UNREALIZED).click()

  def orders_rejected_press(self):
    getElement(self, HomePage.ORDERS_MENU_REJECTED).click()
    
  def orders_all_sent_press(self):
    getElement(self, HomePage.ORDERS_MENU_ALL_SENT).click()

  def orders_scanner_out_of_stock_press(self):
    getElement(self, HomePage.ORDERS_MENU_SCANNER_OUT_OF_STOCK).click()

  def orders_scanner_automatic_out_of_stock_press(self):
    getElement(self, HomePage.ORDERS_MENU_SCANNER_AUTOMATIC_OUT_OF_STOCK).click()

  def orders_scanner_orders_press(self):
    getElement(self, HomePage.ORDERS_MENU_SCANNER_ORDERS).click()

  def orders_scanner_log_press(self):
    getElement(self, HomePage.ORDERS_MENU_SCANNER_LOG).click()

  def warehouse_management_press(self):
    getElement(self, HomePage.WAREHOUSE_MANAGEMENT_BUTTON).click()
