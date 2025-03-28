from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_HISTORY_ITEM = lambda index: [By.XPATH,
                                        f"//li[contains(@class, 'OrderHistory_listItem__2x95r mb-6')][{index}]/a"]
    INGREDIENT = [By.XPATH, "//a[p[text()='Краторная булка N-200i']]"]
    ADD_BUTTON = [By.XPATH, "//button[text()='Добавить']"]
    ORDER_MODAL_TITLE = [By.XPATH,
                         "//h2[contains(@class, 'Modal_modal__title') and contains(@class, 'text_type_digits-large')]"]
    ORDER_NUMBER_LOCATOR_FEED = [By.XPATH,
                                     "//p[contains(@class, 'text_type_digits-default') and contains(@class, 'mb-10') and contains(@class, 'mt-5')]"]

    COUNTER = [By.XPATH, "//a[p[text()='Краторная булка N-200i']]//p[contains(@class, 'counter_counter__num__3nue1')]"]
    ORDER_HISTORY = [By.XPATH, "//a[text()='История заказов']"]
    TEXT_IN_POPUP = [By.XPATH, "//p[text()='Cостав']"]
    ORDERS_FROM_FEED = [By.CSS_SELECTOR, ".OrderHistory_listItem__2x95r"]
    ID_ORDERS_FROM_FEED = [By.CSS_SELECTOR, "p.text.text_type_digits-default"]
    ORDERS_FROM_HISTORY = [By.CSS_SELECTOR, ".OrderHistory_listItem__2x95r"]
    ID_ORDERS_FROM_HISTORY = [By.CSS_SELECTOR, "p.text.text_type_digits-default"]
    TOTAL_COMPLETED = [By.XPATH, "//div[@class='undefined mb-15']/p[contains(text(), 'Выполнено за все время:')]/following-sibling::p"]
    TODAY_COMPLETED = [By.XPATH, "//div/p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p"]
    ORDER_IN_PROGRESS = [By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']"]
    ORDER_NUMBER = [By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"]
    CLOSE_BUTTON = [By.XPATH,"//button[contains(@class, 'Modal_modal__close_modified__3V5XS') and contains(@class, 'Modal_modal__close__TnseK')]"]
    MODAL_OVERLAY = [By.CSS_SELECTOR, '.Modal_modal_overlay__x2ZCr']
