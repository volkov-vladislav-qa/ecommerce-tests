from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage(Base):
    """ Класс содержащий локаторы и методы для страницы Авторизации"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    url = "https://fuji-san.ru/japonskie-sladosti/" # url тестируемого сайта

    # Locators

    btn_entrance_start = (By.XPATH,  '//a[@class="auth-popup"]')
    login = (By.XPATH,'//input[@name="login"]')
    password = (By.XPATH,'//input[@name="password"]')
    btn_entrance_finish = (By.XPATH, '//input[@value="Войти"]')
    close_window_authorization = (By.XPATH,'//i[@class="icon-remove"]') # крестик закрытия всплывающего окна об успехе авторизации
    main_word = (By.XPATH, '//span[contains(text(), "Добро")]')

    # Getters

    def get_user_login(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login))

    def get_user_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.password))

    def get_btn_entrance_start(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.btn_entrance_start))

    def get_btn_entrance_finish(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.btn_entrance_finish))

    def get_close_window_authorization(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.close_window_authorization))

    def get_main_word(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.main_word))

    # Actions
    def click_btn_entrance_start(self):
        self.get_btn_entrance_start().click()

    def input_user_login(self,name):
        self.get_user_login().send_keys(name)
        print('Input user name')

    def input_user_password(self,password):
        self.get_user_password().send_keys(password)
        print('Input user password')

    def click_btn_entrance_finish(self):
        self.get_btn_entrance_finish().click()

    def click_close_window_authorization(self):
        self.get_close_window_authorization().click()

    #Methods
    @allure.description('Авторизация')
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_btn_entrance_start()
        self.input_user_login('wolf92rabota@gmail.com')
        self.input_user_password('1')
        self.click_btn_entrance_finish()
        self.click_close_window_authorization()
        self.assert_word(self.get_main_word(),'Добро пожаловать')