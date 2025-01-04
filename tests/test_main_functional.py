import allure
import pytest
from urls import BASE_PAGE, LOGIN_PAGE

@allure.epic("Основной функционал")
@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
class TestMainPage:

    @allure.story("Открытие конструктора")
    def test_open_constructor(self,main_page):
        main_page.open_url(LOGIN_PAGE)
        main_page.open_constructor()
        assert main_page.check_title_main(), "Заголовок 'Соберите бургер' не отображается."


    @allure.story("Открытие ленты заказов")
    def test_open_order_feed(self,main_page):
        main_page.open_url(BASE_PAGE)
        main_page.open_order_feed()
        assert main_page.check_order_title(),"Заголовок 'Лента заказов' не отображается."


    @allure.story("Проверка деталей ингредиентов")
    def test_check_ingredient_details(self,main_page):
        main_page.open_url(BASE_PAGE)
        assert main_page.check_ingredient_details(), "Всплывающее окно с деталями не отображается."


    @allure.story("Закрытие деталей ингредиентов")
    def test_close_ingredient_details(self,main_page):
        main_page.open_url(BASE_PAGE)
        main_page.check_ingredient_details()
        main_page.close_ingredient_details()
        assert not main_page.is_element_popup_clickable(), "Всплывающее окно не закрылось."


    @allure.story("Проверка увеличения счетчика")
    def test_check_counter_increased(self,main_page,driver):
        main_page.open_url(BASE_PAGE)
        initial_counter_value = int(main_page.check_counter_value())
        main_page.drop_ingredient_for_order(driver.name)
        new_counter_value = int(main_page.check_counter_value())
        assert new_counter_value == initial_counter_value + 2, "Счетчик ингредиента не равен 2."


    @allure.story("Оформление заказа")
    def test_checkout_order(self,main_page,driver, login_account):
        main_page.drop_ingredient_for_order(driver.name)
        main_page.checkout_order()
        assert main_page.check_order_confirmation(), "Окно с идентификатором заказа не отображается."
