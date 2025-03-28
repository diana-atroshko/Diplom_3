from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    LOGO = [By.CSS_SELECTOR, "div.AppHeader_header__logo__2D0X2"]
    PERSONAL_ACCOUNT = [By.XPATH, "//a[normalize-space()='Личный Кабинет']"]
    TEXT_IN_PERSONAL_ACCOUNT = [By.XPATH,
                                "//p[@class='Account_text__fZAIn text text_type_main-default' and contains(text(), 'В этом разделе вы можете изменить свои персональные данные')]"]
    BUTTON_ENTER = [By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]"]  # кнопка войти в аккаунт
    EXIT = [By.XPATH, "//button[@type='button' and contains(@class, 'Account_button__14Yp3')]"]  # кнопка выход
    HISTORY_BUTTON = [By.XPATH, '//a[@href="/account/order-history" and contains(@class, "Account_link__2ETsJ")]']  # кнопка история заказов
    TEXT_ENTER = [By.XPATH, "//h2[contains(text(), 'Вход')]"]  # заголовок Вход в форме входа
    NAME_INPUT = [By.XPATH, "//input[@name='name' and @type='text']"]
    PASSWORD_INPUT = [By.XPATH, "//input[@name='Пароль' and @type='password']"]
    MODAL_OVERLAY = [By.CSS_SELECTOR, '.Modal_modal_overlay__x2ZCr']
    BURGER_TITLE = [By.XPATH, "//h1[text()='Соберите бургер']"]
    LOGIN_BUTTON = [By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Войти']"]
    ASSEMBLE_BURGER = [By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10' and contains(text(), 'Соберите бургер')]" ] # текст соберите бургер
