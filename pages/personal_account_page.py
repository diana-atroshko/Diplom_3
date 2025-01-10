from locators.main_functional_locators import MainFunctionalLocators
from pages.base_page import BasePage
import allure
from locators.personal_account_locators import PersonalAccountLocators
from urls import ORDER_HISTORY_PAGE
from data import NAME, PASSWORD


class PersonalAccountPage(BasePage):

    @allure.step('Клик на личный кабинет')
    def click_personal_account(self, browser):
        if browser == 'chrome':
            return self.click_to_element(PersonalAccountLocators.PERSONAL_ACCOUNT)
        elif browser =='firefox':
            return self.click_element_with_action(
            locator=PersonalAccountLocators.PERSONAL_ACCOUNT,
            modal_overlay_locator=MainFunctionalLocators.MODAL_OVERLAY)

    @allure.step('Проверка наличия заголовка "Вход"')
    def check_title_enter(self):
        return self.is_element_displayed(PersonalAccountLocators.TEXT_ENTER)

    @allure.step('Проверка текста в личном кабинете')
    def check_text_in_personal_account(self):
        return self.is_element_displayed(PersonalAccountLocators.TEXT_IN_PERSONAL_ACCOUNT)

    @allure.step('Клик на историю заказов')
    def click_history_list(self,browser):
        if browser == 'chrome':
            self.is_element_clickable(PersonalAccountLocators.HISTORY_BUTTON)
            return self.click_to_element(PersonalAccountLocators.HISTORY_BUTTON)
        elif browser =='firefox':
            return self.click_element_with_action(
            locator=PersonalAccountLocators.HISTORY_BUTTON,
            modal_overlay_locator=MainFunctionalLocators.MODAL_OVERLAY)

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

    @allure.step('Вход в личный кабинет')
    def login(self):
        self.add_text_to_element(PersonalAccountLocators.NAME_INPUT,NAME)
        self.add_text_to_element(PersonalAccountLocators.PASSWORD_INPUT,PASSWORD)
        self.click_to_element(PersonalAccountLocators.LOGIN_BUTTON)
        self.find_element_with_wait(MainFunctionalLocators.BURGER_TITLE)
        self.is_element_displayed(MainFunctionalLocators.BURGER_TITLE)