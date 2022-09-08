from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from tests.configTest import getElement

class ReportPage:

  REPORT_GENERATE = (By.XPATH, "//*[text()[contains(.,'Generuj raport')]]")
  REPORT_START_DATE = (By.XPATH, "//*[contains(@name, 'componentDiv:component:first')] [contains(@class, 'calendar hasDatepicker')]")
  REPORT_END_DATE = (By.XPATH, "//*[contains(@name, 'componentDiv:component:second')] [contains(@class, 'calendar hasDatepicker')]")
  REPORT_SELECT_FORMAT_XLSX = (By.XPATH, "//option[text()[contains(.,'XLSX (Excel)')]]")
  REPORT_SELECT_FORMAT_XLS = (By.XPATH, "//option[text()[contains(.,'XLS (Excel)')]]")
  REPORT_SELECT_FORMAT_XML = (By.XPATH, "//option[text()[contains(.,'XML (Java)')]]")


    
  def report_generate_press(self):
    getElement(self, ReportPage.REPORT_GENERATE).click()

  def report_set_start_date(self, data=str):
    getElement(self, ReportPage.REPORT_START_DATE).send_keys(data)

  def report_set_end_date(self, data=str):
    getElement(self, ReportPage.REPORT_END_DATE).send_keys(data)

  def report_set_format(self, locator):
    getElement(self, locator).click()

  def report_generate_test_check(self):
    return getElement(self, (By.XPATH, "//*[text()[contains(.,'Zlecono wykonanie raportu.')]]"))

