import re
import allure

from consts import Const
from locators import Locators
from page_object_models.pages.base_page import BasePage
from page_object_models.pages.order.order_form import OrderForm


def get_order_num(s: str, throw=True):
    regex = r"Номер заказа: (\d+)"
    matches = re.findall(regex, s)
    if throw and not len(matches):
        raise ValueError(f'Order Number not found in str: {s}')
    return int(matches[0])


class OrderPage(BasePage):
    PATH = Const.ORDER_PAGE_PATH

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.form = OrderForm(driver=driver, wait=wait)

    @allure.step('Нажатие кнопки "Далее" в форме заказа')
    def next(self):
        self.driver.find_element(*Locators.ORDER_FORM_BTN_NEXT).click()

    @allure.step('Нажатие кнопки "Готово" в форме заказа')
    def complete_order(self):
        self.driver.find_element(*Locators.ORDER_FORM_MAKE_ORDER_BTN).click()

    @allure.step('Проверка видимости модального окна подтверждения заказа')
    def is_confirmation_modal_open(self):
        self.wait.until(self.EC.visibility_of_element_located(Locators.ORDER_MODAL))
        return True

    @allure.step('Подтверждение заказа')
    def confirm_order(self):
        confirmation_window = self.driver.find_element(*Locators.ORDER_MODAL)
        confirmation_window.find_element(*Locators.ORDER_MODAL_YES_BTN).click()
        self.wait.until(lambda driver:
                        'Заказ оформлен' in driver.find_element(*Locators.ORDER_MODAL_HEADER).text)
        self.wait.until(lambda driver: self.get_order_num())

    @allure.step('Получение номера заказа из сообщения в модальном окне')
    def get_order_num(self):
        modal_text = self.driver.find_element(*Locators.ORDER_MODAL_TEXT_CONTAINER).text
        order_num = get_order_num(modal_text, throw=False)
        return order_num

    @allure.step('Нажатие кнопки просмотреть заказ')
    def view_order(self):
        confirmation_window = self.driver.find_element(*Locators.ORDER_MODAL)
        confirmation_window.find_element(*Locators.ORDER_MODAL_VIEW_BTN).click()
