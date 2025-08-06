from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.Base_Pages import BasePage
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FlightSearchPage:
    close_modal_xpath = "//span[@class='commonModal__close']"
    from_input_xpath = "//input[contains(@placeholder,'From')]"
    to_input_xpath = "//input[@placeholder='To']"
    day_xpath = "//div[@class='DayPicker-Month'][1]/div[3]/div/div[@aria-label='Fri Aug 15 2025']"
    search_button_xpath = "//a[normalize-space()='Search']"
    from_city_xpath = "//label[@for='fromCity']"
    # from_city_suggestion_xpath = "//div[contains(@class,'autoSuggestPlugin')]/div[1]"
    from_city_suggestion_xpath = "//ul[@class='react-autosuggest__suggestions-list']"
    # from_city_text_xpath = "//p[contains(text(),'Goa (North), India')]"
    from_city_text_xpath = "//ul[contains(@class,'react-autosuggest')]/li[1]"
    to_city_xpath = "//label[@for='toCity']"
    to_city_suggestion_xpath = "//div[contains(@class,'autoSuggestPlugin')]/div[1]"
    to_city_text_xpath = "//div[contains(@class,'react-autosuggest__suggestions-container')]/div/ul/li[1]"
    day_picker_xpath = "//div[@class='DayPicker-Month'][1]"
    date_xpath = "//label[@for='departure']//span[contains(text(),'15')]"
    return_option_xpath = "//div[@class='fareCardItem '][2]"
    got_it_button_xpath = "//div[@class='fliCompCoachmark']//span[contains(text(),'GOT IT')]"
    flights_text_xpath = "//span[contains(text(),'Flights from')]"
    all_flight_price_xpath = "//div[contains(@data-test,'component  -clusterBody')]/div[1]/div[2]/div/div/div/span"
    incorrect_flight_error_xpath = "//div[@class='fltErrorSection makeFlex']//span[2]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def close_exception_modal(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.close_modal_xpath)))
            self.driver.find_element(By.XPATH, self.close_modal_xpath).click()
        except:
            pass

    def select_from_city(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.from_city_xpath))).click()

    def enter_from_valid_city(self, valid_city):
        actions = ActionChains(self.driver)
        from_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.from_input_xpath)))
        actions.move_to_element(from_input).click().perform()
        from_input.send_keys(valid_city)
        time.sleep(5)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.from_city_suggestion_xpath)))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.from_city_text_xpath))).click()

    def enter_from_invalid_city(self, invalid_city):
        actions = ActionChains(self.driver)
        from_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.from_input_xpath)))
        actions.move_to_element(from_input).click().perform()
        from_input.send_keys(invalid_city)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.from_city_suggestion_xpath)))
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.from_city_text_xpath)))
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.from_city_text_xpath).click()

    def incorrect_flight_error_msg(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.incorrect_flight_error_xpath)))
        print(self.driver.find_element(By.XPATH, self.incorrect_flight_error_xpath).text)

    def enter_to_city(self):
        self.driver.find_element(By.XPATH, self.to_city_xpath).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.to_input_xpath))).send_keys("Del")
        time.sleep(4)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.to_city_suggestion_xpath)))

        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, self.to_city_text_xpath))).click()
        time.sleep(2)

    def select_day(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.day_picker_xpath)))
        self.driver.find_element(By.XPATH, self.day_xpath).click()
        time.sleep(2)
        selected_date = self.driver.find_element(By.XPATH, self.date_xpath).text
        expected_text = "15"
        assert selected_date == expected_text

    def select_regular_button(self):
        self.driver.find_element(By.XPATH, self.return_option_xpath).click()

    def click_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()

    def click_got_it_button(self):
        try:
            self.driver.find_element(By.XPATH, self.got_it_button_xpath).click()
            print("Got it button clicked")
        except:
            pass

    def flight(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.flights_text_xpath)))
        flights_price = self.driver.find_elements(By.XPATH, self.all_flight_price_xpath)
        print(flights_price)
