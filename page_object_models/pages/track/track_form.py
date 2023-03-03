import dataclasses
import datetime
import allure

from page_object_models.basemodel import BaseModel
from locators import Locators
from util import User


class _FieldToTitle:
    Name = 'Имя'
    LastName = 'Фамилия'
    Address = 'Адрес'
    Metro = 'Станция метро'
    Phone = 'Телефон'
    DeliveryDate = 'Дата доставки'
    RentalPeriod = 'Срок аренды'
    Color = 'Цвет'


@dataclasses.dataclass
class TrackFormValues:
    User: User
    Metro: str
    DeliveryDate: datetime.date
    RentalPeriod: str
    ScooterPeriod: str


class TrackForm(BaseModel):
    def get_field_value(self, name):
        locator = Locators.TRACK_ORDER_ROW_VALUE_FOR_TITLE(name)
        self.wait.until(self.EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    @allure.step('Валидация имени пользователя в форме трекинга')
    def validate_order_user_name(self, expected_value: str):
        assert self.get_field_value(_FieldToTitle.Name) == expected_value

    @allure.step('Валидация фамилии пользователя в форме трекинга')
    def validate_order_user_last_name(self, expected_value: str):
        assert self.get_field_value(_FieldToTitle.LastName) == expected_value

    @allure.step('Валидация адреса пользователя в форме трекинга')
    def validate_order_user_address(self, expected_value: str):
        assert self.get_field_value(_FieldToTitle.Address) == expected_value

    @allure.step('Валидация телефона пользователя в форме трекинга')
    def validate_order_user_phone(self, expected_value: str):
        assert self.get_field_value(_FieldToTitle.Phone) == expected_value

    @allure.step('Валидация даты доставки в форме трекинга')
    def validate_order_delivery_date(self, expected_value: datetime.date):
        # TODO find a way to get locale str of date
        raise NotImplemented()

    @allure.step('Валидация срока аренды в форме трекинга')
    def validate_order_rental_period(self, expected_value: str):
        assert self.get_field_value(_FieldToTitle.RentalPeriod) == expected_value

    @allure.step('Валидация цвета самоката в форме трекинга')
    def validate_order_scooter_color(self, expected_value: str):
        assert self.get_field_value(_FieldToTitle.Color) == expected_value

    @allure.step('Валидация станции метро в форме трекинга')
    def validate_order_metro(self, expected_value: str):
        assert self.get_field_value(_FieldToTitle.Metro) == expected_value

    @allure.step('Валидация данных заказа в трекинг форме')
    def validate_order(self, values: TrackFormValues):
        self.wait.until(self.EC.visibility_of_element_located(Locators.TRACK_ORDER_ROW_VALUE))
        self.validate_order_user_name(values.User.name)
        self.validate_order_user_last_name(values.User.last_name)
        self.validate_order_user_address(values.User.address)
        self.validate_order_user_phone(values.User.phone)
        # TODO implement
        # self.validate_order_delivery_date(values.delivery_date)
        self.validate_order_rental_period(values.RentalPeriod)
        self.validate_order_scooter_color(values.ScooterPeriod)
        self.validate_order_metro(values.Metro)
