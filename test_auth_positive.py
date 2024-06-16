import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='module')
def driver():
    service = Service('D:/Python/PycharmProjects/QAP_Selenium_mod_33_final/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_login_by_phone_success(driver):
    # Перейти на страницу авторизации
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=_0__B9AtVb0')

    # Дождаться появления таба "Номер"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-phone"]')))

    # Выбрать таб "Номер"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()

    # Ввести номер телефона
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('79858789020')

    # Ввести пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('A12345678$a')

    # Нажать кнопку "Войти"
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()

    time.sleep(3)
    # Проверка что авторизация прошла успешно
    assert driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div[1]/h2').text == 'Гречко\nРоман'

    # Нажать кнопку "Выйти"
    driver.find_element(By.XPATH, '//*[@id="logout-btn"]').click()


def test_login_by_email_success(driver):
    # Перейти на страницу авторизации
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=_0__B9AtVb0')

    # Дождаться появления таба "Почта"
    WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-mail"]')))

    # Выбрать таб "Почта"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()

    # Ввести почту
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('fizi@bk.ru')

    # Ввести пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('A12345678$a')

    # Нажать кнопку "Войти"
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()

    time.sleep(3)
    # Проверка что авторизация прошла успешно
    assert driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div[1]/h2').text == 'Гречко\nРоман'

    # Нажать кнопку "Выйти"
    driver.find_element(By.XPATH, '//*[@id="logout-btn"]').click()


def test_login_by_login_success(driver):
    # Перейти на страницу авторизации
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=_0__B9AtVb0')

    # Дождаться появления таба "Логин"
    WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-login"]')))

    # Выбрать таб "Логин"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-login"]').click()

    # Ввести Логин
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('rtkid_1718395075325')

    # Ввести пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('A12345678$a')

    # Нажать кнопку "Войти"
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()

    time.sleep(3)
    # Проверка что авторизация прошла успешно
    assert driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div[1]/h2').text == 'Гречко\nРоман'

    # Нажать кнопку "Выйти"
    driver.find_element(By.XPATH, '//*[@id="logout-btn"]').click()


def test_login_by_ls_success(driver):
    # Перейти на страницу авторизации
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=_0__B9AtVb0')

    # Дождаться появления таба "Лицевой счёт"
    WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-ls"]')))

    # Выбрать таб "Лицевой счёт"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-ls"]').click()

    # Ввести номер Лицевого счёта
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('876010365652')

    # Ввести пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('A12345678$a')

    # Нажать кнопку "Войти"
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()

    time.sleep(3)
    # Проверка что авторизация прошла успешно
    assert driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div[1]/h2').text == 'Гречко\nРоман'

    # Нажать кнопку "Выйти"
    driver.find_element(By.XPATH, '//*[@id="logout-btn"]').click()