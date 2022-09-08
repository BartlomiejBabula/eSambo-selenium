import pytest
import datetime 
from tests.configTest import setup, select_store, franchiseStore
from pages.franchiseStorePages.homePage import HomePage
from pages.raportPage import ReportPage


@pytest.mark.usefixtures("setup")
class Test_orders_rapors:
    yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    today = datetime.date.today().strftime("%Y-%m-%d") 

    def other_raport(self, locator, data = bool):
        HomePage.orders_menu_select_other_report(self, locator)
        ReportPage.report_generate_press(self)
        ReportPage.report_set_format(self, ReportPage.REPORT_SELECT_FORMAT_XLSX)
        if data:
            ReportPage.report_set_start_date(self, Test_orders_rapors.yesterday)
            ReportPage.report_set_end_date(self, Test_orders_rapors.today)
        ReportPage.report_generate_press(self)


    def test_report_S001(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        HomePage.orders_menu_report_S001_press(self)
        ReportPage.report_generate_press(self)
        ReportPage.report_set_format(self, ReportPage.REPORT_SELECT_FORMAT_XLS)
        ReportPage.report_set_start_date(self, Test_orders_rapors.yesterday)
        ReportPage.report_set_end_date(self,Test_orders_rapors.today)
        ReportPage.report_generate_press(self)
        assert ReportPage.report_generate_test_check(self)

    def test_report_S002(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        HomePage.orders_menu_report_S002_press(self)
        ReportPage.report_generate_press(self)
        ReportPage.report_set_format(self, ReportPage.REPORT_SELECT_FORMAT_XLSX)
        ReportPage.report_set_start_date(self, Test_orders_rapors.yesterday)
        ReportPage.report_set_end_date(self, Test_orders_rapors.today)
        ReportPage.report_generate_press(self)
        assert ReportPage.report_generate_test_check(self)

    def test_report_M013(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        HomePage.orders_menu_report_M013_press(self)
        ReportPage.report_generate_press(self)
        ReportPage.report_set_format(self, ReportPage.REPORT_SELECT_FORMAT_XLS)
        ReportPage.report_set_start_date(self, Test_orders_rapors.yesterday)
        ReportPage.report_generate_press(self)
        assert ReportPage.report_generate_test_check(self)

    def test_report_T011(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        HomePage.orders_menu_report_T011_press(self)
        ReportPage.report_generate_press(self)
        ReportPage.report_set_format(self, ReportPage.REPORT_SELECT_FORMAT_XLSX)
        ReportPage.report_set_start_date(self, Test_orders_rapors.yesterday)
        ReportPage.report_set_end_date(self, Test_orders_rapors.today)
        ReportPage.report_generate_press(self)
        assert ReportPage.report_generate_test_check(self)

    def test_report_T015(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        Test_orders_rapors.other_raport(self, HomePage.ORDERS_MENU_SELECT_OTHER_REPORT_T015, True)
        assert ReportPage.report_generate_test_check(self)

    def test_report_T001(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        Test_orders_rapors.other_raport(self, HomePage.ORDERS_MENU_SELECT_OTHER_REPORT_T001, False)
        assert ReportPage.report_generate_test_check(self)

    def test_report_T002(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        Test_orders_rapors.other_raport(self, HomePage.ORDERS_MENU_SELECT_OTHER_REPORT_T002, True)
        assert ReportPage.report_generate_test_check(self)

    def test_report_T003(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        Test_orders_rapors.other_raport(self, HomePage.ORDERS_MENU_SELECT_OTHER_REPORT_T003, False)
        assert ReportPage.report_generate_test_check(self)

    def test_report_T004(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        Test_orders_rapors.other_raport(self, HomePage.ORDERS_MENU_SELECT_OTHER_REPORT_T004, False)
        assert ReportPage.report_generate_test_check(self)

    def test_report_T005(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        Test_orders_rapors.other_raport(self, HomePage.ORDERS_MENU_SELECT_OTHER_REPORT_T005, False)
        assert ReportPage.report_generate_test_check(self)

    def test_report_T006(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        Test_orders_rapors.other_raport(self, HomePage.ORDERS_MENU_SELECT_OTHER_REPORT_T006, True)
        assert ReportPage.report_generate_test_check(self)

    def test_report_T007(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        Test_orders_rapors.other_raport(self, HomePage.ORDERS_MENU_SELECT_OTHER_REPORT_T007, True)
        assert ReportPage.report_generate_test_check(self)

    def test_report_T008(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        Test_orders_rapors.other_raport(self, HomePage.ORDERS_MENU_SELECT_OTHER_REPORT_T008, True)
        assert ReportPage.report_generate_test_check(self)

    def test_report_T009(self):
        select_store(self, franchiseStore)
        HomePage.articles_press(self)
        HomePage.orders_press(self)
        Test_orders_rapors.other_raport(self, HomePage.ORDERS_MENU_SELECT_OTHER_REPORT_T009, False)
        assert ReportPage.report_generate_test_check(self)



