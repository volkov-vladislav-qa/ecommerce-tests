import time

from pages.login_page import LoginPage
from pages.maine_page import MainPage
from pages.promo_page import PromoPage
from pages.cart_page import CartPage
from base.base_class import Base
from pages.checkout import CheckOut
import allure

@allure.description('Тест полного пути до момента подтверждения заказа')
def test_select_product(chrome_driver,login_fix):
        main = MainPage(chrome_driver)
        main.go_to_the_promo() # переход на страницу с акционным товаром

        promo = PromoPage(chrome_driver)
        promo.filter_by_price(100,200) # фильтр по цене от и до
        promo.sort_by_price() # сортировка от мин цены до макс в выбранном ценовом диапазоне
        promo.change_to_table_view() # переключаем отображение товара с плиточного на табличный вид
        promo.move_product_to_cart() # добавляем 1 товар на странице в корзину

        base=Base(chrome_driver)
        base.open_cart() # открываем корзину с покупками

        cartpage = CartPage(chrome_driver)
        cartpage.get_current_url()
        cartpage.move_complete_order()

        checkout = CheckOut(chrome_driver)
        checkout.fill_form()

        time.sleep(10)





