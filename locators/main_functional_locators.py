from selenium.webdriver.common.by import By


class MainFunctionalLocators:
    CONSTRUCTOR_BUTTON = [By.XPATH, "//p[text()='Конструктор']"]
    BURGER_TITLE = [By.XPATH, "//h1[text()='Соберите бургер']"]
    ORDER_FEED_BUTTON = [By.XPATH, "//p[text()='Лента Заказов']"]
    ORDER_FEED_TITLE = [By.XPATH, "//h1[contains(@class, 'text_type_main-large') and text()='Лента заказов']"]
    INGREDIENT = [By.XPATH, "//a[p[text()='Краторная булка N-200i']]"]
    INGREDIENT_DETAILS_TEXT = [By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]"]
    INGREDIENT_DETAILS_POPUP = [By.CSS_SELECTOR, "ul.Modal_modal__statsList__6cEm5"]
    CLOSE_BUTTON = [By.CSS_SELECTOR, "button.Modal_modal__close__TnseK"]
    INGREDIENT_COUNTER = [By.XPATH, "//a[p[text()='Краторная булка N-200i']]//p[contains(@class, 'counter_counter__num__3nue1')]"]
    FOR_FIND_COUNTER = [By.TAG_NAME, 'p']
    ADD_BUTTON = [By.XPATH, "//div[@class='constructor-element constructor-element_pos_top']//span[contains(text(), 'Перетяните булочку сюда (верх)')]"]
    CHECKOUT_BUTTON = [By.XPATH, "//button[text()='Оформить заказ']"]
    ORDER_CONFIRMATION_TEXT = [By.XPATH, "//p[contains(@class, 'text_type_main-medium') and text()='идентификатор заказа']"]
    ORDER_PREPARING_MESSAGE = [By.XPATH, "//div[contains(@class, 'Modal_modal__textContainer__9TwLS')]//p[text()='Ваш заказ начали готовить']"]
    ORDER_READY_MESSAGE = [By.XPATH, "//div[contains(@class, 'Modal_modal__textContainer__9TwLS')]//p[text()='Дождитесь готовности на орбитальной станции']"]

