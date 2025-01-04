import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента с ожиданием')
    def find_element_with_wait(self, locator):
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
            return self.driver.find_element(*locator)


    @allure.step('Клик по элементу')
    def click_to_element(self, locator):
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Проверка доступности элемента для клика')
    def is_element_clickable(self,locator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))

    @allure.step('Ожидание наличия всех элементов на странице')
    def presence_of_all_elements_located(self,locator, timeout=25):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    @allure.step('Отправка данных для заполнения поля')
    def add_text_to_element(self, locator, text):
            self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получение текста из элемента')
    def get_text_from_element(self, locator):
            return self.find_element_with_wait(locator).text

    @allure.step('Скролл до искомого элемента')
    def scroll_to_element(self, locator):
            element = self.find_element_with_wait(locator)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Очистка поля')
    def clear_element(self, locator):
            element = self.find_element_with_wait(locator)
            element.clear()

    @allure.step("Ожидание элемента и проверка его отображения")
    def is_element_displayed(self, locator):
            element = self.find_element_with_wait(locator)
            return element.is_displayed()

    @allure.step("Переключение на окно по индексу")
    def switch_to_window(self, index):
            self.driver.switch_to.window(self.driver.window_handles[index])


    @allure.step("Получение текущего URL")
    def get_current_url(self):
            return self.driver.current_url

    @allure.step("Открытие URL")
    def open_url(self, url):
        self.driver.get(url)
        time.sleep(5)

    @allure.step('Перетаскивание элемента в Chrome')
    def drag_and_drop_for_chrome(self, ingredient, drop_area):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, drop_area).perform()

    @allure.step('Перетаскивание элемента с помощью JavaScript')
    def drag_and_drop_with_js(self, ingredient, drop_area):
        js_script = """
        function createEvent(typeOfEvent) {
            var event = document.createEvent("CustomEvent");
            event.initCustomEvent(typeOfEvent, true, true, null);
            event.dataTransfer = {
                data: {},
                setData: function(key, value) {
                    this.data[key] = value;
                },
                getData: function(key) {
                    return this.data[key];
                }
            };
            return event;
        }

        function dispatchEvent(element, event, transferData) {
            if (transferData !== undefined) {
                event.dataTransfer = transferData;
            }
            if (element.dispatchEvent) {
                element.dispatchEvent(event);
            } else if (element.fireEvent) {
                element.fireEvent("on" + event.type, event);
            }
        }

        function simulateHTML5DragAndDrop(element, destination) {
            var dragStartEvent = createEvent('dragstart');
            dispatchEvent(element, dragStartEvent);

            var dropEvent = createEvent('drop');
            dispatchEvent(destination, dropEvent);

            var dragEndEvent = createEvent('dragend');
            dispatchEvent(element, dragEndEvent);
        }

        var source = arguments[0];
        var target = arguments[1];
        simulateHTML5DragAndDrop(source, target);
        """
        self.driver.execute_script(js_script, ingredient, drop_area)