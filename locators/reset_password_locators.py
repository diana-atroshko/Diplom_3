from selenium.webdriver.common.by import By


class RecoverPasswordLocators:

    BUTTON_RECOVER_PASSWORD = [By.XPATH,'//a[@class="Auth_link__1fOlj" and @href="/forgot-password"]']
    BUTTON_PERSONAL_ACCOUNT = [By.XPATH,'//p[@class="AppHeader_header__linkText__3q_va ml-2"]']
    FIELD_EMAIL = [By.XPATH,'//div[@class="input__container"]//input[@type="text" and @name="name"]']
    BUTTON_RECOVER = [By.XPATH,'//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" and text()="Восстановить"]']
    ICON_HIDE = [By.XPATH, "//div[@class='input__icon input__icon-action']"]
    FIELD_PASSWORD = [By.XPATH,'//input[@type="password" and @name="Введите новый пароль"]']
    TITLE_RESET_PASSWORD = [By.XPATH, "//h2[text()='Восстановление пароля']"]
    FIELD_CODE_FROM_EMAIL = [By.XPATH, "//label[text()='Введите код из письма']"]
    PASSWORD_INPUT = (By.XPATH, "//div[@class='input pr-6 pl-6 input_type_password input_size_default']")




