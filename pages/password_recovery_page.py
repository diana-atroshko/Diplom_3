
from pages.base_page import BasePage
import allure
from locators.reset_password_locators import RecoverPasswordLocators


class PasswordRecoveryPage(BasePage):

    @allure.step('Клик по кнопке восстановить пароль')
    def click_recover_password(self,browser):
        if browser == 'chrome':
            self.scroll_to_element(RecoverPasswordLocators.BUTTON_RECOVER_PASSWORD)
            self.is_element_clickable(RecoverPasswordLocators.BUTTON_RECOVER_PASSWORD)
            self.click_to_element(RecoverPasswordLocators.BUTTON_RECOVER_PASSWORD)
        elif browser == 'firefox':
            self.scroll_to_element(RecoverPasswordLocators.BUTTON_RECOVER_PASSWORD)
            self.click_element_with_action(locator= RecoverPasswordLocators.BUTTON_RECOVER_PASSWORD)

    @allure.step('Ввод почты')
    def enter_email(self, email):
        self.clear_element(RecoverPasswordLocators.FIELD_EMAIL)
        self.add_text_to_element(RecoverPasswordLocators.FIELD_EMAIL, email)

    @allure.step('Клик по кнопке восстановить')
    def click_submit(self):
        self.click_to_element(RecoverPasswordLocators.BUTTON_RECOVER)

    @allure.step('Клик по кнопке показать/скрыть пароль')
    def click_toggle_password(self):
        self.find_element_with_wait(RecoverPasswordLocators.ICON_HIDE)
        self.is_element_clickable(RecoverPasswordLocators.ICON_HIDE)
        self.click_to_element(RecoverPasswordLocators.ICON_HIDE)


    @allure.step('Проверка, что заголовок отображается')
    def is_title_displayed(self):
        return self.is_element_displayed(RecoverPasswordLocators.TITLE_RESET_PASSWORD)

    @allure.step('Проверка, что поле ввода кода отображается')
    def is_code_input_label_displayed(self):
        return self.is_element_displayed(RecoverPasswordLocators.FIELD_CODE_FROM_EMAIL)

    @allure.step('Проверка, что поле выделено')
    def check_label_highlighted(self):
        return 'input_status_active' in self.find_element_with_wait(RecoverPasswordLocators.PASSWORD_INPUT).get_attribute('class')

    @allure.step('Проверка, что поле не выделено')
    def check_label_is_not_highlighted(self):
        return 'input_status_active' not in self.find_element_with_wait(RecoverPasswordLocators.PASSWORD_INPUT).get_attribute('class')


