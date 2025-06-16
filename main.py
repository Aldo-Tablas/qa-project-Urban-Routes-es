import data
from selenium import webdriver
from pages import UrbanRoutesPage
from helpers import retrieve_phone_code

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        options = webdriver.ChromeOptions()
        options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.address_from, data.address_to)
        assert page.get_from() == data.address_from
        assert page.get_to() == data.address_to

    def test_select_comfort_tariff(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.address_from, data.address_to)
        page.submit_route()
        page.select_comfort_tariff()
        assert True

    def test_enter_phone_number(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.address_from, data.address_to)
        page.submit_route()
        page.select_comfort_tariff()
        page.open_phone_modal()
        page.enter_phone_number(data.phone_number)
        page.click_next_button()
        assert page.driver.find_element(*page.code_input).is_displayed()

    def test_confirm_phone_code(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.address_from, data.address_to)
        page.submit_route()
        page.select_comfort_tariff()
        page.open_phone_modal()
        page.enter_phone_number(data.phone_number)
        page.click_next_button()
        code = retrieve_phone_code(self.driver)
        page.enter_confirmation_code(code)
        page.click_confirm_button()
        assert page.driver.find_element(*page.open_payment_method).is_displayed()

    def test_add_credit_card(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.address_from, data.address_to)
        page.submit_route()
        page.select_comfort_tariff()
        page.open_phone_modal()
        page.enter_phone_number(data.phone_number)
        page.click_next_button()
        code = retrieve_phone_code(self.driver)
        page.enter_confirmation_code(code)
        page.click_confirm_button()
        page.open_payment_section()
        page.add_credit_card(data.card_number, data.card_code)
        page.close_card_modal()
        assert True

    def test_write_message_to_driver(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.address_from, data.address_to)
        page.submit_route()
        page.write_message(data.message_for_driver)
        actual_message = page.driver.find_element(*page.comment_input).get_attribute("value")
        assert data.message_for_driver in actual_message

    def test_request_blanket_and_tissues(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.address_from, data.address_to)
        page.submit_route()
        page.request_blanket_and_tissues()
        assert True

    def test_request_ice_cream(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.address_from, data.address_to)
        page.submit_route()
        page.request_ice_cream(2)
        assert True

    def test_order_taxi_and_check_driver_info(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.address_from, data.address_to)
        page.submit_route()
        page.select_comfort_tariff()
        page.open_phone_modal()
        page.enter_phone_number(data.phone_number)
        page.click_next_button()
        code = retrieve_phone_code(self.driver)
        page.enter_confirmation_code(code)
        page.click_confirm_button()
        page.open_payment_section()
        page.add_credit_card(data.card_number, data.card_code)
        page.close_card_modal()
        page.write_message(data.message_for_driver)
        page.request_blanket_and_tissues()
        page.request_ice_cream(2)
        page.order_taxi()
        page.wait_for_driver_info()
        assert page.driver.find_element(*page.driver_info).is_displayed()