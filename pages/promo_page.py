import allure
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import re


class PromoPage(Base):
    """ Класс содержащий локаторы и методы для страницы Акции"""

    def __init__(self, driver):
        super().__init__(driver)
        self.product_catalog = {}

    # Locators

    price_filter_min = (By.XPATH,'//input[@name="price_min"]') # минимальная цена в настройках фильтра
    price_filter_max = (By.XPATH, '//input[@name="price_max"]')  # максимальная цена в настройках фильтра
    to_table_view =(By.XPATH, '//i[@class="icon-th-list"]') # переключатель на  табличный вид отображения
    sorted_lst = (By.XPATH, '//div[@class="sorting-selection"]') # раскрывающийся список фильтров
    btn_sorted_desc = (By.XPATH, '//ul[@class="menu-v sorting"]//a[contains(@href, "sort=price")]') # фильтр цены в списке фильтров
    all_product_name = (By.XPATH, '//span[@itemprop="name"]')  # название всех продуктов на странице
    all_product_sale_price = (By.XPATH, '//span[@class="price nowrap"]') # цена всех продуктов на странице со скидкой
    btn_submit = (By.XPATH, '//input[@value="В корзину"]') # кнопка добавления товаров в корзину
    all_product_cart = ('//li[@itemscope]')




    # Getters
    def get_btn_submit(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.btn_submit))

    def get_price_filter_min(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.price_filter_min))

    def get_price_filter_max(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.price_filter_max))

    def get_table_view(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.to_table_view))

    def get_sorted_lst(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.sorted_lst))

    def get_btn_sorted_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.btn_sorted_desc))

    def get_all_product_name(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.all_product_name))




    def get_all_product_sale_price(self):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.all_product_sale_price))
        non_empty_elements = [el for el in elements if el.text.strip()]
        return non_empty_elements

    def get_btn_sorted_desc(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.btn_sorted_desc))

    def get_all_product_cart(self):
        return self.driver.find_elements(By.XPATH,self.all_product_cart)


    # Actions
    def switch_to_table_view(self):
        self.get_table_view().click()


    def input_min_price(self,price):
        self.get_price_filter_min().send_keys(f"{price}{Keys.ENTER}")

    def input_max_price(self,price):
        self.get_price_filter_max().send_keys(f"{price}{Keys.ENTER}")

    def parsing_all_product_name(self):
        list_name = []
        base_name = self.get_all_product_name()
        for i in base_name:
            list_name.append(i.text)
        return list_name

    def parsing_all_product_sale_price(self):
        list_name = []
        base_name = self.get_all_product_sale_price()
        for i in base_name:
            list_name.append(i.text)
        return list_name



    def click_btn_sorted_desc(self):
        self.get_btn_sorted_desc().click()




    def move_to_sorted_lst(self):
        sorting_element = self.get_sorted_lst()
        ActionChains(self.driver).move_to_element(sorting_element).perform()

    def click_btn_submit(self):
        self.get_btn_submit().click()




    #Methods
    @allure.step("Фильтр по цене от мин до макс")
    def filter_by_price(self,price_min = 0,price_max = 9999):
        self.get_current_url()
        self.input_min_price(price_min)
        self.input_max_price(price_max)
        print(f"Применили фильтр по цене {price_min} до {price_max}")

    @allure.step("Переключение на плиточный вид отображения")
    def change_to_table_view(self):
        self.switch_to_table_view()
        print('Вид отображения изменён на табличный')

    @allure.step("Сортировка товара по цене")
    def  sort_by_price(self):
        self.move_to_sorted_lst()
        try:
            self.get_btn_sorted_desc().click()

        except StaleElementReferenceException:
            # Если элемент стал устаревшим, находим его заново
            self.get_btn_sorted_desc().click()



    """Получить словарь название товара : цена"""
    def sorted_product_catalog(self):
        key = self.parsing_all_product_name()
        value =  self.parsing_all_product_sale_price()
        for num in range(len(key)):
            self.product_catalog[key[num]] = int(re.sub(r"[^\d]", "", value[num]))

        return self.product_catalog

    """Товар с минимальной ценой"""
    def min_price_product(self):
        min_price = min(self.sorted_product_catalog(),key=self.product_catalog.get)
        return f'{min_price} : {self.product_catalog[min_price]}'

    @allure.step("Добавляем товар в корзину")
    def move_product_to_cart(self):
        self.click_btn_submit()









