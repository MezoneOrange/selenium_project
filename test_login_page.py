import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .test_main_page import MAIN_LINK


# LOGIN_LINK = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


@pytest.mark.login_page
def test_forms_should_be_in_login_in_url(browser):
    page = MainPage(browser, MAIN_LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()


@pytest.mark.login_page
def test_forms_should_be_in_login_form(browser):
    page = MainPage(browser, MAIN_LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()


@pytest.mark.login_page
def test_forms_should_be_in_register_form(browser):
    page = MainPage(browser, MAIN_LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_register_form()