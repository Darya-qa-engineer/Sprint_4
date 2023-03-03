from page_object_models.basemodel import BaseModel
from page_object_models.components.accordion import Accordion
from locators import Locators


class HomeFAQ(BaseModel):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.accordion = Accordion(driver=driver, wait=wait, locator=Locators.HOME_FAQ_CONTAINER)

    def has(self, question):
        return self.accordion.has(question)

    def open(self, question):
        self.accordion.open(question)

    def is_open(self, question):
        return self.accordion.is_open(question)

    def question_matches_answer(self, question, answer):
        item = self.accordion.get_item(question)
        return item.panel.text == answer
