import dataclasses
import datetime

import allure

from locators import Locators
from page_object_models.basemodel import BaseModel
from page_object_models.components.datepicker_input import DatePickerInput
from page_object_models.components.dropdown_input import DropdownInput
from util import User


class OrderFormValueFields:
    Metro = 1
    DeliveryDate = 2
    RentalPeriod = 3


@dataclasses.dataclass
class OrderFormValues:
    User: User
    DeliveryDate: datetime.date
    RentalPeriod: str
    Metro: str
    Days: int


# TODO allow setting delivery date by datetime
class OrderForm(BaseModel):
    ValueFields = OrderFormValueFields

    @allure.step('Заполнение первого экрана формы заказа')
    def fill_first_step(self, values: OrderFormValues):
        self.fill_user(values.User)
        self.fill_metro(values.Metro)

    @allure.step('Заполнение второго экрана формы заказа')
    def fill_second_step(self, values: OrderFormValues):
        self.set_delivery_date_days_after(values.Days)
        self.fill_rental_period(values.RentalPeriod)

    @allure.step('Заполнение данных пользователя в форме заказа')
    def fill_user(self, user: User):
        self.driver.find_element(*Locators.ORDER_FORM_NAME_FIELD).send_keys(user.name)
        self.driver.find_element(*Locators.ORDER_FORM_LAST_NAME_FIELD).send_keys(user.last_name)
        self.driver.find_element(*Locators.ORDER_FORM_ADDRESS_FIELD).send_keys(user.address)
        self.driver.find_element(*Locators.ORDER_FORM_PHONE_FIELD).send_keys(user.phone)

    @allure.step('Заполнение метро в форме заказа')
    def fill_metro(self, name):
        metro_input = self.driver.find_element(*Locators.ORDER_FORM_METRO_FIELD)
        # btw checking the case insensitivity
        metro_input.send_keys(name.upper())
        self.wait.until(self.EC.visibility_of_element_located(Locators.METRO_SEARCH_RESULTS))
        search_item = self.driver.find_element(*Locators.METRO_SEARCH_RESULTS)
        assert search_item.text == name
        search_item.click()
        assert self.value(self.ValueFields.Metro) == name

    @allure.step('Заполнение срока аренды в форме заказа')
    def fill_rental_period(self, value):
        input_ = self.get_rental_period_input()
        input_.select(value)

    @allure.step('Заполнение даты доставки в форме заказа')
    def set_delivery_date_days_after(self, days: int):
        input_ = self.get_delivery_date_picker_input()
        input_.set_day_after(days)

    def get_delivery_date_picker_input(self):
        date_picker_input = DatePickerInput(driver=self.driver, wait=self.wait, locator=Locators.ORDER_FORM_DELIVERY_DATE_INPUT)
        return date_picker_input

    def get_rental_period_input(self):
        rental_input = DropdownInput(driver=self.driver, wait=self.wait, locator=Locators.ORDER_FORM_DATE_RENTAL_PERIOD_INPUT)
        return rental_input

    def value(self, name):
        if name == OrderFormValueFields.Metro:
            metro_input = self.driver.find_element(*Locators.ORDER_FORM_METRO_FIELD)
            return metro_input.get_attribute('value')
        if name == OrderFormValueFields.DeliveryDate:
            return self.get_delivery_date_picker_input().value()
        if name == OrderFormValueFields.RentalPeriod:
            return self.get_rental_period_input().value

    def assert_delivery_date(self, delivery_date: datetime):
        form_delivery_date = self.value(self.ValueFields.DeliveryDate)
        assert form_delivery_date.day == delivery_date.day

    @allure.step('Валидация что текущая дата выбрана в поле доставки формы заказа')
    def validate_today(self):
        now = datetime.date.today()
        input_ = self.get_delivery_date_picker_input()
        picker = input_.get_picker()
        picker_today = picker.get_today_day()
        assert picker_today == now.day
        assert picker.get_selected_day() == now.day
