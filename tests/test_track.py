from page_object_models.pages.track.track_form import TrackFormValues
from page_object_models.pages.track.track_page import TrackPage


def test_track_after_order(open_url, wait, order_test_data, order_page, track_page, home_page):
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

    # Track page validation
    track_page.assert_url()
    track_form = track_page.track_form
    assert track_page.order_num() == order_num
    track_form.validate_order(TrackFormValues(
        User=order_test_data.User,
        Metro=order_test_data.Metro,
        DeliveryDate=order_test_data.DeliveryDate,
        RentalPeriod=order_test_data.RentalPeriod,
        ScooterPeriod=TrackPage.Colors.ANY
    ))
    track_page.is_roadmap_current(TrackPage.Scooter_At_Warehouse)
