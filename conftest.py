import datetime

import pytest
from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait

from page_object_models.pages.home.home_page import HomePage
from page_object_models.pages.order.order_form import OrderFormValues
from page_object_models.pages.order.order_page import OrderPage
from page_object_models.pages.track.track_page import TrackPage
from consts import Const
from locators import Locators
from util import Generate


@pytest.fixture
def driver():
    driver = Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def order_test_data(user):
    days = 2
    delivery_date = datetime.date.today() + datetime.timedelta(days=days)
    return OrderFormValues(
        User=user,
        RentalPeriod='трое суток',
        DeliveryDate=delivery_date,
        Days=days,
        Metro='Минская',
    )


@pytest.fixture
def user():
    return Generate.user()

@pytest.fixture
def root_url():
    return Const.ROOT_URL

@pytest.fixture
def open_url(driver, root_url):
    def _open(url=root_url):
        driver.get(url)
        driver.find_element(*Locators.COOKIE_BTN).click()
        return driver
    yield _open


@pytest.fixture
def wait(driver):
    _wait = WebDriverWait(driver, 5)
    yield _wait


# PAGES

@pytest.fixture
def home_page(driver, wait):
    yield HomePage(driver=driver, wait=wait)


@pytest.fixture
def order_page(driver, wait):
    yield OrderPage(driver=driver, wait=wait)


@pytest.fixture
def track_page(driver, wait):
    yield TrackPage(driver=driver, wait=wait)
