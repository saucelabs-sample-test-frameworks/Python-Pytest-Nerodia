import pytest


def test_removes_one(browser):
    browser.goto('www.saucedemo.com/inventory.html')

    browser.button(class_name='btn_primary').click()
    browser.button(class_name='btn_primary').click()

    browser.button(class_name='btn_secondary').click()
    assert browser.span(class_name='shopping_cart_badge').text == '1'

    browser.goto("https://www.saucedemo.com/cart.html")
    assert len(browser.divs(class_name='inventory_item_name')) == 1
