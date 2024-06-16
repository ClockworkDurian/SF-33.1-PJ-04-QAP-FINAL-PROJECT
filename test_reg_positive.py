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


def test_reg_by_phone_success(driver):
    # Перейти на страницу авторизации
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=_0__B9AtVb0')

    # Дождаться появления таба "Номер"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-phone"]')))

    # Нажать на ссылку "Зарегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()

    time.sleep(3)

    # Заполнить поле "Имя"
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys('Иван')

    # Заполнить поле "Фамилия"
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]').send_keys('Иванов')

    # Заполнить поле "Email или телефон"
    driver.find_element(By.XPATH, '//*[@id="address"]').send_keys('79857777777')

    # Заполнить поле "Пароль"
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Qwerty123!')

    # Заполнить поле "Подтверждение пароля"
    driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys('Qwerty123!')

    # Нажать кнопку "Зареегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    # Дождаться появления формы ввода СМС-кода
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="otp"]/div[1]/div[1]/input')))

    # Ввести валидный СМС-код
    # Здесь необходимо реализовать задержку для возможности ввести СМС-код вручную
    time.sleep(25)

    # Проверка что регистрация прошла успешно
    assert driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div[1]/h2').text == 'Иванов\nИван'

    # Нажать кнопку "Выйти"
    driver.find_element(By.XPATH, '//*[@id="logout-btn"]').click()


def test_reg_by_email_success(driver):
    # Перейти на страницу авторизации
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=_0__B9AtVb0')

    # Дождаться появления таба "Номер"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-phone"]')))

    # Нажать на ссылку "Зарегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()

    time.sleep(3)

    # Заполнить поле "Имя"
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys('Иван')

    # Заполнить поле "Фамилия"
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]').send_keys('Иванов')

    # Заполнить поле "Email или телефон"
    driver.find_element(By.XPATH, '//*[@id="address"]').send_keys('test@test.com')

    # Заполнить поле "Пароль"
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Qwerty123!')

    # Заполнить поле "Подтверждение пароля"
    driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys('Qwerty123!')

    # Нажать кнопку "Зареегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    # Дождаться появления формы ввода кода из почты
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="otp"]/div[1]/div[1]/input')))

    # Ввести валидный код из почты
    # Здесь необходимо реализовать задержку для возможности ввести код из почты вручную
    time.sleep(25)

    # Проверка что регистрация прошла успешно
    assert driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div[1]/h2').text == 'Иванов\nИван'

    # Нажать кнопку "Выйти"
    driver.find_element(By.XPATH, '//*[@id="logout-btn"]').click()
