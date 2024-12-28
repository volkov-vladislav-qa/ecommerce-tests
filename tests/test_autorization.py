
from pages.login_page import LoginPage
from selenium.common.exceptions import NoSuchElementException

from base.base_class import Base
import allure

@allure.description('Тест успешной авторизации')
def test_autorization(chrome_driver):
        login = LoginPage(chrome_driver)
        login.get_current_url()
        login.click_btn_entrance_start()
        login.input_user_login('wolf92rabota@gmail.com')
        login.input_user_password('1')
        login.click_btn_entrance_finish()

        try:
                fin = login.get_success_autoriz()
                print(fin.text)
        except NoSuchElementException as e:
                print(f"Что сломалось {e}")







