from selenium.common import TimeoutException
from pages.base_page import BasePage
import time
import allure
from locators.main_functional_locators import MainFunctionalLocators as mf

class MainPage(BasePage):
    @allure.step('Открытие конструктора')
    def open_constructor(self):
        self.find_element_with_wait(mf.CONSTRUCTOR_BUTTON)
        self.click_to_element(mf.CONSTRUCTOR_BUTTON)

    @allure.step('Проверка заголовка главной страницы')
    def check_title_main(self):
        return self.is_element_displayed(mf.BURGER_TITLE)

    @allure.step('Открытие ленты заказов')
    def open_order_feed(self):
        element = self.find_element_with_wait(mf.ORDER_FEED_BUTTON)
        self.is_element_clickable(mf.ORDER_FEED_BUTTON)
        self.click_to_element(mf.ORDER_FEED_BUTTON)

    @allure.step('Проверка заголовка заказа')
    def check_order_title(self):
        return self.is_element_displayed(mf.ORDER_FEED_TITLE)

    @allure.step('Проверка деталей ингредиента')
    def check_ingredient_details(self):
        self.find_element_with_wait(mf.INGREDIENT)
        self.click_to_element(mf.INGREDIENT)
        return self.is_element_displayed(mf.INGREDIENT_DETAILS_TEXT)

    @allure.step('Проверка кликабельности всплывающего окна')
    def is_element_popup_clickable(self):
        try:
            return self.is_element_clickable(mf.CLOSE_BUTTON)
        except TimeoutException:
            return False

    @allure.step('Закрытие деталей ингредиента')
    def close_ingredient_details(self):
        self.find_element_with_wait(mf.CLOSE_BUTTON)
        self.click_to_element(mf.CLOSE_BUTTON)

    @allure.step('Проверка значения счетчика ингредиентов')
    def check_counter_value(self):
        counter_element = self.find_element_with_wait(mf.INGREDIENT_COUNTER)
        value = counter_element.text.strip()  # Убираем лишние пробелы
        return int(value)

    @allure.step('Оформление заказа')
    def checkout_order(self):
        self.find_element_with_wait(mf.CHECKOUT_BUTTON)
        self.click_to_element(mf.CHECKOUT_BUTTON)

    @allure.step('Проверка подтверждения заказа')
    def check_order_confirmation(self):
        self.find_element_with_wait(mf.ORDER_CONFIRMATION_TEXT)
        return self.is_element_displayed(mf.ORDER_CONFIRMATION_TEXT) and self.is_element_displayed(
            mf.ORDER_PREPARING_MESSAGE)

    @allure.step('Перетаскивание ингредиента для заказа')
    def drop_ingredient_for_order(self, browser):
        ingredient_element = self.driver.find_element(*mf.INGREDIENT)
        drop_area_element = self.driver.find_element(*mf.ADD_BUTTON)

        if browser == 'chrome':
            self.drag_and_drop_for_chrome(ingredient_element, drop_area_element)
        elif browser == 'firefox':
            self.drag_and_drop_with_js(ingredient_element, drop_area_element)

