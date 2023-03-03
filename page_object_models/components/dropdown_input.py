from locators import Locators
from page_object_models.basemodel import BaseModel


class DropdownInput(BaseModel):
    def __init__(self, driver, wait, locator):
        super().__init__(driver, wait)
        self.locator = locator

    @property
    def input_el(self):
        return self.driver.find_element(*self.locator)

    @property
    def value(self) -> str | None:
        placeholder = self.input_el.find_element(*Locators.DROPDOWN_INPUT_PLACEHOLDER)
        has_value = 'selected' in placeholder.get_attribute('class')
        return placeholder.text if has_value else None

    def select(self, val):
        self.input_el.click()
        self.wait.until(self.EC.visibility_of_element_located(Locators.DROPDOWN_MENU))
        option_el = self.input_el.find_element(*Locators.DROPDOWN_OPTION_BY_VALUE(val))
        option_el.click()
