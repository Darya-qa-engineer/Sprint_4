from page_object_models.basemodel import BaseModel
from consts import Const


class BasePage(BaseModel):
    PATH: Const.TRACK_PAGE_PATH

    def assert_url(self):
        self.wait.until(self.EC.url_contains(self.PATH))
        assert self.PATH in self.driver.current_url
