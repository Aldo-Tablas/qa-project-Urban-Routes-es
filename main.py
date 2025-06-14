import data
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
import json
import time

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    code = None
    for _ in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance')
                    if log.get("message") and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
                if code:
                    return code
        except WebDriverException:
            time.sleep(1)
            continue

    raise Exception("No se encontró el código de confirmación del teléfono.\n"
                    "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")


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



class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        options = webdriver.ChromeOptions()
        options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)

    def test_full_ride_request(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)

        # Paso 1: Ingresar direcciones
        page.set_route(data.address_from, data.address_to)
        page.submit_route()

        # Paso 2: Seleccionar tarifa Comfort
        page.select_comfort_tariff()

        # Paso 3: Ingresar número de teléfono
        page.open_phone_modal()
        page.enter_phone_number(data.phone_number)
        page.click_next_button()

        # Paso 4: Obtener y escribir código de confirmación
        code = retrieve_phone_code(self.driver)
        page.enter_confirmation_code(code)
        page.click_confirm_button()

        # Paso 5: Agregar tarjeta de crédito
        page.open_payment_section()
        page.add_credit_card(data.card_number, data.card_code)
        page.close_card_modal()

        # Paso 6: Escribir mensaje para el conductor
        page.write_message(data.message_for_driver)

        # Paso 7: Pedir manta y pañuelos
        page.request_blanket_and_tissues()

        # Paso 8: Pedir 2 helados
        page.request_ice_cream(2)

        # Paso 9: Confirmar el pedido del taxi
        page.order_taxi()

        # Paso 10: Esperar información del conductor
        page.wait_for_driver_info()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()