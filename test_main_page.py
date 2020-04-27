import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage


MAIN_LINK = "http://selenium1py.pythonanywhere.com/"
LOGIN_LINK = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


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


@pytest.mark.login_page
def test_forms_should_be_in_login_in_url(browser):
    login_page = LoginPage(browser, LOGIN_LINK)
    login_page.should_be_login_url()


@pytest.mark.login_page
def test_forms_should_be_in_login_form(browser):
    login_page = LoginPage(browser, LOGIN_LINK)
    login_page.open()
    login_page.should_be_login_form()


@pytest.mark.login_page
def test_forms_should_be_in_register_form(browser):
    login_page = LoginPage(browser, LOGIN_LINK)
    login_page.open()
    login_page.should_be_register_form()