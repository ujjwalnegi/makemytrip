import time

from Pages.FlightSearchPage import FlightSearchPage
from Test_Cases.BaseTest import BaseTest


class Test_Correct_flight_search(BaseTest):
    def test_correct_city_flight_search(self):
        flight_search_page = FlightSearchPage(self.driver)
        flight_search_page.close_exception_modal()
        flight_search_page.select_from_city()
        flight_search_page.enter_from_valid_city("Goa")
        flight_search_page.enter_to_city()
        flight_search_page.select_day()
        flight_search_page.select_regular_button()
        flight_search_page.click_search_button()

    def test_incorrect_city_flight_search(self):
        flight_search_page = FlightSearchPage(self.driver)
        flight_search_page.close_exception_modal()
        flight_search_page.select_from_city()
        flight_search_page.enter_from_invalid_city("New")
        flight_search_page.enter_to_city()
        flight_search_page.incorrect_flight_error_msg()
