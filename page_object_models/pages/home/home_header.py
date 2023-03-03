from page_object_models.basemodel import BaseModel
from locators import Locators


class HomeHeader(BaseModel):
    @property
    def yandex_logo(self):
        return self.driver.find_element(*Locators.YANDEX_LOGO)

    @property
    def scooter_logo(self):
        return self.driver.find_element(*Locators.SCOOTER_LOGO)

    @property
    def order_btn(self):
        return self.driver.find_element(*Locators.ORDER_BTN_TOP_RIGHT)
