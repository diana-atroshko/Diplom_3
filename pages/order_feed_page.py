import time
import allure
from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage

from pages.main_page import MainPage


class OrderFeedPage(BasePage):

    @allure.step('Открытие заказа по индексу')
    def open_order_by_index(self, index):
        order_item_locator = OrderFeedLocators.ORDER_HISTORY_ITEM(index)
        self.find_element_with_wait(order_item_locator).click()

    @allure.step('Проверка всплывающего окна с деталями заказа')
    def check_order_details_popup(self):
        return (self.is_element_displayed(OrderFeedLocators.ORDER_NUMBER_LOCATOR_FEED)
                and self.is_element_displayed(OrderFeedLocators.TEXT_IN_POPUP))

    @allure.step('Получение списка заказов из ленты')
    def get_list_of_orders_from_feed(self):
       elements = self.presence_of_all_elements_located(OrderFeedLocators.ORDERS_FROM_FEED)
       print(f"Found order elements: {elements}")
       return [OrderFeedPage(element) for element in elements]

    @allure.step('Получение списка заказов из истории')
    def get_list_of_orders_from_history(self):
        elements = self.presence_of_all_elements_located(OrderFeedLocators.ORDERS_FROM_HISTORY)
        print(f"Found order elements: {elements}")
        return [OrderFeedPage(element) for element in elements]

    @allure.step('Получение ID заказов из ленты')
    def get_id_from_feed(self):
        return self.get_text_from_element(OrderFeedLocators.ID_ORDERS_FROM_FEED)

    @allure.step('Получение ID заказов из истории')
    def get_id_from_history(self):
        return self.get_text_from_element(OrderFeedLocators.ID_ORDERS_FROM_HISTORY)

    @allure.step('Получение общего количества завершенных заказов')
    def get_total_completed_orders(self):
        total_completed_element = self.find_element_with_wait(OrderFeedLocators.TOTAL_COMPLETED)
        return int(total_completed_element.text)

    @allure.step('Получение количества завершенных заказов за сегодня')
    def get_today_completed_orders(self):
        today_completed_element = self.find_element_with_wait(OrderFeedLocators.TODAY_COMPLETED)
        return int(today_completed_element.text)

    @allure.step('Проверка отображения заказа в процессе')
    def check_order_in_progress_displayed(self):
        in_progress_element = self.find_element_with_wait(OrderFeedLocators.ORDER_IN_PROGRESS)
        return in_progress_element.text

    @allure.step('Получение номера заказа')
    def get_order_number(self):
        order_number_element = self.find_element_with_wait(OrderFeedLocators.ORDER_NUMBER)
        return order_number_element.text

    @allure.step('Создание и совершения заказа')
    def create_and_complete_order(self):
        main_page= MainPage(self.driver)
        main_page.open_constructor()
        main_page.drop_ingredient_for_order(self.driver.name)
        main_page.checkout_order()
        self.find_element_with_wait(OrderFeedLocators.ORDER_NUMBER)
        time.sleep(5)
        return self.get_order_number()

    @allure.step('Закрытие деталей заказа')
    def close_order_details(self):
        self.click_to_element(OrderFeedLocators.CLOSE_BUTTON)

