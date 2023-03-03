from selenium.webdriver.remote.webelement import WebElement
from locators import Locators
from page_object_models.basemodel import BaseModel


class _Panel:
    def __init__(self, el: WebElement, text):
        self.el = el
        self.text = text

    def is_visible(self) -> bool:
        return self.el.is_displayed()


class _Heading:
    def __init__(self, el: WebElement, text):
        self.el = el
        self.text = text

    def is_open(self) -> bool:
        return self.el.get_attribute('aria-expanded') == 'true'


class _Item:
    def __init__(self, el: WebElement, heading: _Heading, panel: _Panel):
        self.el = el
        self.panel = panel
        self.heading = heading

    def open(self):
        self.heading.el.click()

    def is_open(self) -> bool:
        return self.heading.is_open() and self.panel.is_visible()


class Accordion(BaseModel):
    items: list[_Item] = []
    items_by_text: dict[str, _Item] = {}

    def __init__(self, driver, wait, locator):
        super().__init__(driver, wait)
        self.locator = locator
        self.initialize()

    @property
    def el(self):
        return self.driver.find_element(*self.locator)

    def get_item(self, name):
        item = self.items_by_text[name]
        if item:
            return item
        raise ValueError(f'Item "{name} not found"')

    def initialize(self):
        rows = self.el.find_elements(*Locators.ACCORDION_ITEM)
        for row in rows:
            panel_el = row.find_element(*Locators.ACCORDION_ITEM_PANEL)
            heading_el = row.find_element(*Locators.ACCORDION_ITEM_HEADING)
            heading = _Heading(heading_el, heading_el.text)
            panel = _Panel(panel_el, panel_el.get_attribute('textContent'))
            item = _Item(row, heading=heading, panel=panel)
            self.items.append(item)
            self.items_by_text[heading.text] = item

    def open(self, name):
        self.get_item(name).open()

    def has(self, name):
        try:
            self.get_item(name)
            return True
        except ValueError:
            return False

    def is_open(self, name):
        return self.get_item(name).is_open()


