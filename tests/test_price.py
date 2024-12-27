import time

from pages.login_page import LoginPage
from pages.maine_page import MainPage
from pages.promo_page import PromoPage
from pages.cart_page import CartPage
from base.base_class import Base
import allure

@allure.description('Сравнение цены товара на странице и в корзине')
def test_price_product(chrome_driver,login):
        main = MainPage(chrome_driver)
        main.go_to_the_promo()  # переход на страницу с акционным товаром

        promo = PromoPage(chrome_driver)
        promo.filter_by_price(100, 200)  # фильтр по цене от и до
        promo.sort_by_price()  # сортировка от мин цены до макс в выбранном ценовом диапазоне
        promo.change_to_table_view()  # переключаем отображение товара с плиточного на табличный вид
        promo_price = promo.min_price_product()
        promo.move_product_to_cart()  # добавляем 1 товар на странице в корзину

        base = Base(chrome_driver)
        base.open_cart()  # открываем корзину с покупками

        cartpage = CartPage(chrome_driver)
        cartpage.get_current_url()
        final_price = cartpage.comparison_price()

        if final_price.split(":")[1] == promo_price.split(":")[1]:
                print('Всё сходится до копеечки')
        else:
                print(f'Ой вэй, цены не совпадают {final_price}    {promo_price}')





