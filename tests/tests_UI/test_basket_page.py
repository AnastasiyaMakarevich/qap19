import time
import pytest
import allure
from pages.basket_page import BasketPage
from pages.main_page import MainPage


@allure.title('Basket is empty')
def test_basket_is_empty(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()

    basket_page = BasketPage(driver)
    basket_page.open_basket()
    basket_page.assert_that_basket_is_empty()

@allure.title('Basket is not empty')
def test_basket_is_not_empty(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.add_to_basket_by_index(0)

    basket_page = BasketPage(driver)
    basket_page.open_basket()
    basket_page.assert_that_basket_is_not_empty()

@allure.title('Button make an order')
def test_assert_that_button_make_an_order_is_working(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.add_to_basket_by_index(0)

    basket_page = BasketPage(driver)
    basket_page.open_basket()
    basket_page.click_make_order()
    basket_page.assert_that_make_order_is_working()

@pytest.mark.parametrize("promocode", ['11111', '8888', '333'])
@allure.title('Invalid promocode')
def test_assert_that_the_promo_code_is_invalid(driver, promocode):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.add_to_basket_by_index(0)

    basket_page = BasketPage(driver)
    basket_page.open_basket()
    basket_page.set_promocode(promocode)
    basket_page.click_use_promocode()
    basket_page.assert_that_promocode_is_incorrect()

@pytest.mark.parametrize("index", range(3))
@allure.title('The right product in the basket')
def test_add_product_in_basket_and_compare_names(driver, index):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    time.sleep(1)
    product_text = main_page.get_text_product_by_index(index)
    main_page.add_to_basket_by_index(index)

    basket_page = BasketPage(driver)
    basket_page.open_basket()
    product_text_from_basket = basket_page.get_product_text_by_index(0)
    assert product_text == product_text_from_basket

@pytest.mark.parametrize("n", [2, 4, 5])
@allure.title('The right products in the basket')
def test_add_some_products_in_basket_and_compare_names(driver, n):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    time.sleep(1)
    # Собираем названия продуктов на главной странице
    main_page_products = []
    for i in range(n):
        product_text = main_page.get_text_product_by_index(i).strip()
        main_page_products.append(product_text)
        main_page.add_to_basket_by_index(i)

    basket_page = BasketPage(driver)
    basket_page.open_basket()
    # Собираем названия продуктов из корзины
    basket_products = []
    for i in range(n):
        product_text_from_basket = basket_page.get_product_text_by_index(i).strip()
        basket_products.append(product_text_from_basket)
    # Сравниваем множества
    assert set(main_page_products) == set(basket_products)

@allure.title('Delete all products from basket')
def test_add_two_products_in_basket_and_delete_two_from_basket(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.add_to_basket_by_index(0)
    main_page.add_to_basket_by_index(1)

    basket_page = BasketPage(driver)
    basket_page.open_basket()
    basket_page.delete_from_basket_by_index(1)
    basket_page.delete_from_basket_by_index(0)
    basket_page.assert_that_basket_is_empty()

@allure.title('Delete not all products from basket')
def test_add_two_products_in_basket_and_delete_one_from_basket(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.add_to_basket_by_index(0)
    main_page.add_to_basket_by_index(1)

    basket_page = BasketPage(driver)
    basket_page.open_basket()
    basket_page.delete_from_basket_by_index(1)
    basket_page.assert_that_basket_is_not_empty()
