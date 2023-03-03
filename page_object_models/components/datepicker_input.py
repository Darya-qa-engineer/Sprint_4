from datetime import datetime, timedelta
from page_object_models.basemodel import BaseModel
from page_object_models.components.datepicker import DatePicker


class DatePickerInput(BaseModel):
    def __init__(self, driver, wait, locator):
        super().__init__(driver, wait)
        self.locator = locator

    @property
    def input(self):
        return self.driver.find_element(*self.locator)

    def value(self) -> datetime | None:
        date_str = self.input.get_attribute('value')
        if not date_str:
            return None
        return datetime.strptime(date_str, '%d.%m.%Y')

    def set_day_after(self, days: int = 1):
        picker = self.open_datepicker()
        selected = picker.get_selected_day()
        [year, month] = picker.get_year_month()
        new_date = datetime(year, month, selected)
        new_date += timedelta(days=days)
        if picker.is_selected_last_day() or not month == new_date.month:
            # TODO: click multiple when days more than 1 month
            picker.click_next_month()
        picker.select_day(new_date.day)

    def open_datepicker(self):
        date_picker = DatePicker(driver=self.driver, wait=self.wait)
        self.input.click()
        date_picker.wait_visible()
        return date_picker

    def get_picker(self):
        return self.open_datepicker()

