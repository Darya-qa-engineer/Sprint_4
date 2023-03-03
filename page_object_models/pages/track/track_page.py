import allure

from page_object_models.pages.base_page import BasePage
from page_object_models.pages.track.track_form import TrackForm
from consts import Const
from locators import Locators


class Colors:
    ANY = 'любой'
    BLACK = 'чёрный жемчуг'
    GRAY = 'серая безысходность'


class TrackPage(BasePage):
    PATH = Const.TRACK_PAGE_PATH
    Scooter_At_Warehouse = 'Самокат на складе'
    Colors = Colors

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.track_form = TrackForm(driver, wait)

    @allure.step('Получение номера заказа из поля ввода')
    def order_num(self) -> int:
        self.wait.until(self.EC.visibility_of_element_located(Locators.TRACK_FORM_INPUT))
        num = self.driver.find_element(*Locators.TRACK_FORM_INPUT).get_attribute('value')
        return int(num)

    @allure.step('Проверка текущего активного статуса в роадмапе')
    def is_roadmap_current(self, name) -> bool:
        highlighted_brick = self.driver.find_element(*Locators.TRACK_ORDER_ROADMAP_BRICK_HIGHLIGHTED)
        title = highlighted_brick.find_element(*Locators.TRACK_ORDER_ROADMAP_BRICK_TITLE).text
        return name == title
