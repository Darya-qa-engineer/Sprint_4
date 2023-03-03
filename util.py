from faker import Faker
from selenium.webdriver.support import expected_conditions as EC

fake = Faker('ru_RU')


def scroll_into_view(driver, wait, el):
    driver.execute_script("arguments[0].scrollIntoView();", el)
    wait.until(EC.visibility_of(el))


class Generate:
    @staticmethod
    def user_name():
        return fake.first_name()

    @staticmethod
    def user_last_name():
        return fake.last_name()

    @staticmethod
    def user_address():
        return fake.numerify(f"{fake.street_name()} ##")

    @staticmethod
    def user_phone():
        return fake.numerify("+7##########")

    @staticmethod
    def user():
        return User(Generate.user_name(), Generate.user_last_name(), Generate.user_address(), Generate.user_phone())


class User:
    def __init__(self, name, last_name, address, phone):
        self.name = name
        self.last_name = last_name
        self.address = address
        self.phone = phone
