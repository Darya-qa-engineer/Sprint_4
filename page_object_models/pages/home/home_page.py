from page_object_models.pages.base_page import BasePage
from page_object_models.pages.home.home_faq import HomeFAQ
from page_object_models.pages.home.home_header import HomeHeader


class HomePage(BasePage):
    PATH = '/'

    @property
    def faq(self):
        return HomeFAQ(driver=self.driver, wait=self.wait)

    @property
    def header(self):
        return HomeHeader(driver=self.driver, wait=self.wait)