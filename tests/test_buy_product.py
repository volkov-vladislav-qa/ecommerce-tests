import time

from pages.login_page import LoginPage
from pages.maine_page import MainPage
from pages.promo_page import PromoPage
from pages.cart_page import CartPage
from base.base_class import Base
from pages.checkout import CheckOut
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure

@allure.description('Тест добавления товара в корзину')
def test_select_product(set_up):
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-webrtc")
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    with webdriver.Chrome(options=options) as driver:
        print('Start Test')
        login = LoginPage(driver)
        login.authorization() # авторизация

        main = MainPage(driver)
        main.go_to_the_promo() # переход на страницу с акционным товаром

        promo = PromoPage(driver)
        promo.filter_by_price(100,200) # фильтр по цене от и до
        promo.sort_by_price() # сортировка от мин цены до макс в выбранном ценовом диапазоне
        promo.change_to_table_view() # переключаем отображение товара с плиточного на табличный вид
        print(promo.min_price_product())
        promo.move_product_to_cart() # добавляем 1 товар на странице в корзину

        base=Base(driver)
        base.open_cart() # открываем корзину с покупками

        cartpage = CartPage(driver)
        cartpage.get_current_url()
        print(cartpage.comparison_price())
        cartpage.move_complete_order()

        checkout = CheckOut(driver)
        checkout.fill_form()

        time.sleep(10)





