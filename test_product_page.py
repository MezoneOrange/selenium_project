import pytest

from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators


ITEM_LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


@pytest.mark.product_page
def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, ITEM_LINK)
    product_page.open()
    product_page.add_to_basket()


@pytest.mark.product_page
def test_item_should_be_into_basket(browser):
    product_page = ProductPage(browser, ITEM_LINK)
    product_page.open()
    product_page.add_to_basket()
    product_page.item_should_be_into_basket()


@pytest.mark.product_page
def test_basket_value_and_item_value_should_be_same(browser):
    product_page = ProductPage(browser, ITEM_LINK)
    product_page.open()
    product_page.add_to_basket()
    product_page.basket_value_and_item_value_should_be_same()