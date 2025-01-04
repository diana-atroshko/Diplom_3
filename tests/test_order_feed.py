import allure
import pytest
from urls import BASE_PAGE, FEED_PAGE

@allure.epic("Лента заказов")
@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
class TestOrderFeed:

    @allure.story("Проверка всплывающего окна деталей заказа")
    def test_order_details_popup(self,driver, main_page,order_page,login_account):
        main_page.open_url(BASE_PAGE)
        main_page.open_order_feed()
        index = 1
        order_page.open_order_by_index(index)
        assert order_page.check_order_details_popup(), 'Информации о деталях заказа не обнаружено'

    @allure.story("Проверка отображения заказов на ленте")
    def test_orders_displayed_on_feed(self,driver, main_page,order_page,account_page, login_account):
        account_page.click_personal_account()
        account_page.click_history_list()
        feed_order_elements = order_page.get_list_of_orders_from_history()
        history_orders_ids = [element.get_id_from_history() for element in feed_order_elements]
        last_five_history_orders_ids = history_orders_ids[-5:]
        main_page.open_order_feed()
        order_elements= order_page.get_list_of_orders_from_feed()
        order_ids = [element.get_id_from_feed() for element in order_elements]
        print(f"Order IDs from feed: {order_ids}")
        print(f"Last 5 Order IDs from history: {last_five_history_orders_ids}")

        for history_orders_id in last_five_history_orders_ids:
            assert history_orders_id in order_ids, f"Order ID {history_orders_id} not found in the feed. Available IDs: {order_ids}"

    @allure.story("Проверка увеличения счетчика завершенных заказов")
    def test_completed_orders_counter_increments(self, driver, main_page, order_page, account_page, login_account):
        main_page.open_order_feed()
        initial_total_completed = order_page.get_total_completed_orders()
        main_page.open_constructor()
        order_page.create_and_complete_order()
        order_page.close_order_details()
        main_page.open_order_feed()
        total_completed = order_page.get_total_completed_orders()
        assert total_completed == initial_total_completed+1, f"Expected total completed orders to be {initial_total_completed + 1}, but got {total_completed}"

    @allure.story("Проверка увеличения счетчика завершенных заказов за сегодня")
    def test_today_completed_orders_counter_increments(self, driver, main_page, order_page, account_page,
                                                       login_account):
        main_page.open_order_feed()
        initial_today_completed = order_page.get_today_completed_orders()
        main_page.open_constructor()
        order_page.create_and_complete_order()
        order_page.close_order_details()
        main_page.open_order_feed()
        new_today_completed = order_page.get_today_completed_orders()
        assert new_today_completed == initial_today_completed + 1, f"Expected today's completed orders to be {initial_today_completed + 1}, but got {new_today_completed}"

    @allure.story("Проверка появления заказа в разделе в работе")
    def test_order_appears_in_working_section(self, driver, main_page, order_page, account_page, login_account):
        main_page.open_constructor()
        order_number = order_page.create_and_complete_order()
        order_page.close_order_details()
        main_page.open_order_feed()
        order_page.open_url(FEED_PAGE)
        in_progress_count = order_page.check_order_in_progress_displayed()
        assert order_number in in_progress_count, f"Order number {order_number} not found in working section."

