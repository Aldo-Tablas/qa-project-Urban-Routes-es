from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    submit_button = (By.XPATH, "//button[text()='Pedir un taxi']")
    comfort_tariff = (By.XPATH, "//div[text()='Comfort']")
    phone_trigger = (By.XPATH, "//div[text()='Número de teléfono']")
    phone_input = (By.ID, "phone")
    phone_next_button = (By.XPATH, "//button[text()='Siguiente']")
    code_input = (By.ID, "code")
    confirm_button = (By.XPATH, "//button[text()='Confirmar']")
    open_payment_method = (By.XPATH, "//div[contains(@class, 'pp-button') and .//div[text()='Método de pago']]")
    open_add_card = (By.XPATH, "//div[text()='Agregar tarjeta']")
    card_number_input = (By.ID, "number")
    card_code_input = (By.CSS_SELECTOR, "div.card-code-input > input#code")
    add_card_button = (By.XPATH, "//button[text()='Agregar']")
    card_modal_close = By.XPATH, "(//button[@class='close-button section-close'])[3]"
    comment_input = (By.ID, "comment")
    blanket_and_tissues_toggle = (By.CLASS_NAME, "slider")
    ice_cream_plus_button = (By.CLASS_NAME, "counter-plus")
    order_taxi_button = (By.XPATH, "//button[.//span[text()='Pedir un taxi']]")
    driver_info = (By.CLASS_NAME, "number")

    def __init__(self, driver):
        self.driver = driver

    # Dirección
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def set_route(self, from_address, to_address):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.from_field)
        )
        self.set_from(from_address)
        self.set_to(to_address)

    def submit_route(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.submit_button)
        ).click()

    def get_from(self) -> str:
        return self.driver.find_element(*self.from_field).get_property('value') or ""

    def get_to(self) -> str:
        return self.driver.find_element(*self.to_field).get_property('value') or ""

    # Tarifa
    def select_comfort_tariff(self):
        self.driver.find_element(*self.comfort_tariff).click()

    # Teléfono
    def open_phone_modal(self):
        self.driver.find_element(*self.phone_trigger).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_input).send_keys(phone_number)

    def click_next_button(self):
        self.driver.find_element(*self.phone_next_button).click()

    def enter_confirmation_code(self, code):
        self.driver.find_element(*self.code_input).send_keys(code)

    def click_confirm_button(self):
        self.driver.find_element(*self.confirm_button).click()

    # Tarjeta
    def open_payment_section(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.open_payment_method)
        ).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.open_add_card)
        ).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.card_number_input)
        )

    def add_credit_card(self, card_number, card_code):
        # Espera y llena el número de tarjeta
        number_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.card_number_input)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", number_field)
        number_field.send_keys(card_number)

        # Espera que el campo de código esté visible e interactuable
        code_field = WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(self.card_code_input)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", code_field)
        code_field.send_keys(card_code)

        code_field.send_keys(Keys.TAB)

        # Scroll al botón por si también está fuera de vista
        add_btn = self.driver.find_element(*self.add_card_button)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_btn)
        add_btn.click()

    def close_card_modal(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.card_modal_close)
        ).click()

    # Mensaje
    def write_message(self, message):
        self.driver.find_element(*self.comment_input).send_keys(message)

    # Servicios extra
    def request_blanket_and_tissues(self):
        self.driver.find_element(*self.blanket_and_tissues_toggle).click()

    def request_ice_cream(self, quantity=1):
        for _ in range(quantity):
            self.driver.find_element(*self.ice_cream_plus_button).click()

    # Confirmar taxi
    def order_taxi(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.order_taxi_button)
        ).click()

    # Verificar conductor
    def wait_for_driver_info(self):
        WebDriverWait(self.driver, 40).until(
            expected_conditions.visibility_of_element_located(self.driver_info)
        )