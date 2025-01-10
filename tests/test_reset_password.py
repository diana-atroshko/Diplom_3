import allure
import pytest
from urls import LOGIN_PAGE
from data import EMAIL


@allure.epic("Восстановление пароля")
@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
class TestPasswordRecovery:

    @allure.title("Клик по кнопке 'Восстановить пароль'")
    def test_click_recover_password(self, driver,password_page):
        password_page.open_url(LOGIN_PAGE)
        password_page.click_recover_password(driver.name)
        assert password_page.is_title_displayed, "Заголовок 'Восстановление пароля' не найден!"

    @allure.title("Ввод email и отправка формы")
    def test_enter_email_and_submit(self, driver,password_page):
        password_page.open_url(LOGIN_PAGE)
        password_page.click_recover_password(driver.name)
        password_page.enter_email(EMAIL)
        password_page.click_submit()
        assert password_page.is_code_input_label_displayed(), "Поле для ввода кода не найдено!"

    @allure.title("Переключение видимости пароля")
    def test_toggle_password_visibility(self, driver,password_page):
        password_page.open_url(LOGIN_PAGE)
        password_page.click_recover_password(driver.name)
        password_page.enter_email(EMAIL)
        password_page.click_submit()
        password_page.click_toggle_password()
        assert password_page.check_label_highlighted, "Поле ввода не подсвечивается!"
        password_page.click_toggle_password()
        assert password_page.check_label_is_not_highlighted, "Поле ввода подсвечивается!"

