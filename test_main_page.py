import pytest

from .pages.main_page import MainPage


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


