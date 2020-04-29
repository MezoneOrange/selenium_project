import pytest

from .pages.main_page import MainPage
from .pages.basket_page import BasketPage


MAIN_LINK = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.main_page
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MAIN_LINK)
    page.open()
    page.go_to_login_page()


@pytest.mark.main_page
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, MAIN_LINK)
    page.open()
    page.should_be_login_link()


@pytest.mark.empty_basket
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, MAIN_LINK)
    page.open()
    page.go_to_basket_page()
    basket = BasketPage(browser, browser.current_url)
    basket.basket_is_empty()


@pytest.mark.empty_basket
def test_guest_can_see_basket_empty_message(browser):
    page = MainPage(browser, MAIN_LINK)
    page.open()
    page.go_to_basket_page()
    basket = BasketPage(browser, browser.current_url)
    basket.basket_is_empty_text()

