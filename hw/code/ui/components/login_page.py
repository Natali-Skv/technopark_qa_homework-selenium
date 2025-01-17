from ui.locators.locators import LoginLocators
from ui.components.base_component import BaseComponent
from ui.paths import paths


class LoginPage(BaseComponent):
    locators = LoginLocators()
    PATH = paths.LOGIN
    REGISTERED_PHONE = "+7(901)502-04-56"

    def login(self, phone, code):
        self.send_keys(self.locators.PHONE_INPUT, phone)
        self.click((self.locators.LOGIN_BUTTON))
        self.send_keys(self.locators.CODE_INPUT, code)
        self.click((self.locators.CONFIRM_CODE_BUTTON))
        self.wait_visability_of_elem(self.locators.PROFILE_BUTTON)

    def input_phone(self, phone=REGISTERED_PHONE):
        self.send_keys(self.locators.PHONE_INPUT, phone)

    def send_phone(self, phone=REGISTERED_PHONE):
        self.send_keys(self.locators.PHONE_INPUT, phone)
        self.click(self.locators.LOGIN_BUTTON)

    def send_code_to_confirm(self, code):
        self.send_keys(self.locators.CODE_INPUT, code)
        self.click(self.locators.CONFIRM_CODE_BUTTON)
