from locators import Locators
from page_object_models.basemodel import BaseModel


class DatePicker(BaseModel):
    def wait_visible(self):
        self.wait.until(lambda driver: self.picker_visible())
    
    @property
    def el(self):
        return self.driver.find_element(*Locators.DATE_PICKER)
    
    def picker_visible(self):
        try:
            assert self.el
            return True
        except AssertionError:
            return False

    def get_selected_day(self):
        day_el = self.el.find_element(*Locators.DATE_PICKER_SELECTED_DAY)
        return int(day_el.text)

    def get_year_month(self):
        attr = self.el.find_element(*Locators.DATE_PICKER_GRID).get_attribute('aria-label')
        return [int(attr[-7:-3]), int(attr[-2:])]

    def get_year(self):
        return self.get_year_month()[0]

    def get_month(self):
        return self.get_year_month()[1]

    def click_next_month(self):
        current_month = self.get_month()
        el = self.el.find_element(*Locators.DATE_PICKER_NEXT_BTN)
        el.click()
        self.wait.until(lambda driver: not self.get_month() == current_month)

    def get_today_day(self):
        el = self.el.find_element(*Locators.DATE_PICKER_TODAY)
        return int(el.text)

    def select_day(self, day: int):
        day_el = self.el.find_element(*Locators.DATE_PICKER_SPECIFIC_DAY(day))
        day_el.click()
        self.wait.until(self.EC.invisibility_of_element(Locators.DATE_PICKER))

    def get_grid_last_day(self):
        last_day = self.el.find_element(*Locators.DATE_PICKER_LAST_DAY)
        return int(last_day.text)

    def is_selected_last_day(self):
        selected = self.get_selected_day()
        last_day = self.get_grid_last_day()
        return selected == last_day

    def is_today_last_day(self):
        today = self.get_today_day()
        last_day = self.get_grid_last_day()
        return today == last_day
