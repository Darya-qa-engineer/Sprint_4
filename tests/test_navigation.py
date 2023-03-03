from selenium.webdriver.support import expected_conditions as EC

from consts import Const


def test_click_yandex_logo(open_url, wait, home_page):
    driver = open_url()
    assert len(driver.window_handles) == 1
    home_page.header.yandex_logo.click()
    wait.until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[-1])
    wait.until(EC.url_matches(Const.YANDEX_MAIN_URL))
    assert Const.YANDEX_MAIN_URL in driver.current_url


def test_click_scooter_logo_from_order_page(open_url, wait, home_page, order_page):
    open_url()
    header = home_page.header
    header.order_btn.click()
    order_page.assert_url()
    header.scooter_logo.click()
    home_page.assert_url()
