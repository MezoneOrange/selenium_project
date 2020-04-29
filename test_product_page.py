import pytest

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


ITEM_LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
ITEM_LINK_2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
ITEM_LINK_3 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                     marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.product_page
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                     marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.product_page
def test_item_should_be_into_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.item_should_be_into_basket()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                     marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.product_page
def test_basket_value_and_item_value_should_be_same(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.basket_value_and_item_value_should_be_same()


@pytest.mark.xfail
@pytest.mark.alert_not_present
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, ITEM_LINK_2)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


@pytest.mark.alert_not_present
def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, ITEM_LINK_2)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
@pytest.mark.alert_not_present
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, ITEM_LINK_2)
    product_page.open()
    product_page.add_to_basket()
    product_page.element_should_be_disappear()


@pytest.mark.login_link
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, ITEM_LINK_3)
    page.open()
    page.should_be_login_link()


@pytest.mark.login_link
def test_guest_can_go_to_login_page_from_product_page (browser):
    page = ProductPage(browser, ITEM_LINK_3)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()


@pytest.mark.to_basket
class TestBasketFromProductPage:
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = ProductPage(browser, ITEM_LINK_3)
        page.open()
        page.go_to_basket_page()
        basket = BasketPage(browser, browser.current_url)
        basket.basket_is_empty()

    def test_guest_can_see_basket_empty_message(self, browser):
        page = ProductPage(browser, ITEM_LINK_3)
        page.open()
        page.go_to_basket_page()
        basket = BasketPage(browser, browser.current_url)
        basket.basket_is_empty_text()