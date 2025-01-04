import allure
import pytest
from urls import BASE_PAGE

@allure.epic("Восстановление пароля")
@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
class TestPasswordRecovery:

    @allure.story("Проверка доступа к личному кабинету без регистрации")
    def test_click_personal_account_without_registration(self, driver,account_page):
        account_page.open_url(BASE_PAGE)
        account_page.click_personal_account()
        assert account_page.check_title_enter(), 'Личный кабинет открылся без регистрации'

    @allure.story("Проверка доступа к личному кабинету с регистрацией")
    def test_click_personal_account_with_registration(self,driver,account_page,login_account):
        account_page.click_personal_account()
        assert account_page.check_text_in_personal_account()

    @allure.story("Проверка доступа к истории заказов")
    def test_click_history_orders(self,driver,login_account,account_page):
        account_page.click_personal_account()
        account_page.click_history_list()
        assert account_page.check_url_history_list()

    @allure.story("Проверка выхода из аккаунта")
    def test_exit_account(self, driver,account_page,login_account):
        account_page.click_personal_account()
        account_page.click_button_exit()
        assert account_page.check_after_exit()

