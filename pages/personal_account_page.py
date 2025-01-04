import time
from pages.base_page import BasePage
import allure
from locators.personal_account_locators import PersonalAccountLocators
from urls import ORDER_HISTORY_PAGE


class PersonalAccountPage(BasePage):

    @allure.step('Клик на личный кабинет')
    def click_personal_account(self):
        return self.click_to_element(PersonalAccountLocators.PERSONAL_ACCOUNT) and time.sleep(2)

    @allure.step('Проверка наличия заголовка "Вход"')
    def check_title_enter(self):
        return self.is_element_displayed(PersonalAccountLocators.TEXT_ENTER)

    @allure.step('Проверка текста в личном кабинете')
    def check_text_in_personal_account(self):
        return self.is_element_displayed(PersonalAccountLocators.TEXT_IN_PERSONAL_ACCOUNT)

    @allure.step('Клик на историю заказов')
    def click_history_list(self):
        self.is_element_clickable(PersonalAccountLocators.HISTORY_BUTTON)
        return self.click_to_element(PersonalAccountLocators.HISTORY_BUTTON) and time.sleep(2)

    @allure.step('Проверка URL истории заказов')
    def check_url_history_list(self):
        return self.get_current_url() == ORDER_HISTORY_PAGE

    @allure.step('Клик на выход')
    def click_button_exit(self):
        self.is_element_clickable(PersonalAccountLocators.EXIT)
        return self.click_to_element(PersonalAccountLocators.EXIT)

    @allure.step('Проверка после выхода')
    def check_after_exit(self):
        self.find_element_with_wait(PersonalAccountLocators.TEXT_ENTER)
        return self.is_element_displayed(PersonalAccountLocators.TEXT_ENTER)

