
from selenium.common.exceptions import TimeoutException
from pages.cart_page import CartPage
from base.base_class import Base
import allure


@allure.description('Удаление всех товаров из корзины')
def test_clear_cart(chrome_driver,login):
        base = Base(chrome_driver)
        base.open_cart()

        cartpage = CartPage(chrome_driver)

        try:
                # Попытка удалить все элементы
                cartpage.delete_all_product()

                # Проверка, что корзина пуста
                finish_text = cartpage.get_item_is_successfully().text
                if finish_text == "Ваша корзина пуста.":
                        print("Корзина успешно очищена:", finish_text)
                else:
                        print("Корзина не очищена полностью:", finish_text)

        except TimeoutException:
                # Обработка случая, когда btn_delete отсутствует
                try:
                        finish_text = cartpage.get_item_is_successfully().text
                        if finish_text == "Ваша корзина пуста.":
                                print("Корзина изначально пуста:", finish_text)
                        else:
                                print("Некорректное сообщение о состоянии корзины:", finish_text)

                except Exception as e:
                        # Общая обработка других ошибок
                        print("Ошибка при проверке состояния корзины:", e)
                        raise




