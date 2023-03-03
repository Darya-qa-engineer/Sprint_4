import allure


@allure.title('Создание заказа')
def test_order(open_url, wait, order_test_data, home_page, order_page, track_page):
    open_url()

    home_page.header.order_btn.click()
    order_page.assert_url()
    order_form = order_page.form
    order_form.fill_first_step(order_test_data)
    order_page.next()

    # step 2
    order_form.validate_today()
    assert order_form.value(order_form.ValueFields.RentalPeriod) is None
    order_form.fill_second_step(order_test_data)
    order_form.assert_delivery_date(order_test_data.DeliveryDate)
    assert order_form.value(order_form.ValueFields.RentalPeriod) == order_test_data.RentalPeriod
    
    order_page.complete_order()
    assert order_page.is_confirmation_modal_open()

    order_page.confirm_order()
    order_num = order_page.get_order_num()
    assert order_num

    order_page.view_order()

    track_page.assert_url()

