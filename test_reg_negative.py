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

def test_reg_by_same_email_unsuccess(driver):
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

    time.sleep(3)

    # Проверка что регистрация не прошла, появилось сообщение, что УЗ уже существует
    assert driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div/div/h2').text == 'Учётная запись уже существует'


def test_reg_by_same_phone_unsuccess(driver):
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
    driver.find_element(By.XPATH, '//*[@id="address"]').send_keys('79858789020')

    # Заполнить поле "Пароль"
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Qwerty123!')

    # Заполнить поле "Подтверждение пароля"
    driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys('Qwerty123!')

    # Нажать кнопку "Зареегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(3)

    # Проверка что регистрация не прошла, появилось сообщение, что УЗ уже существует
    assert driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div/div/h2').text == 'Учётная запись уже существует'


def test_reg_empty_name_unsuccess(driver):
    # Перейти на страницу авторизации
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=_0__B9AtVb0')

    # Дождаться появления таба "Номер"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-phone"]')))

    # Нажать на ссылку "Зарегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()

    time.sleep(3)

    # Не заполнять поле "Имя"
    # driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys('  ')

    # Заполнить поле "Фамилия"
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]').send_keys('Иванов')

    # Заполнить поле "Email или телефон"
    driver.find_element(By.XPATH, '//*[@id="address"]').send_keys('79858789020')

    # Заполнить поле "Пароль"
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Qwerty123!')

    # Заполнить поле "Подтверждение пароля"
    driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys('Qwerty123!')

    # Нажать кнопку "Зареегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(3)

    # Проверка что регистрация не прошла, у поля "Имя" появилось сообщение "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    assert driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]').text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


def test_reg_name_EN_letters_unsuccess(driver):
    # Перейти на страницу авторизации
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=_0__B9AtVb0')

    # Дождаться появления таба "Номер"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-phone"]')))

    # Нажать на ссылку "Зарегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()

    time.sleep(3)

    # Заполнить поле "Имя" английскими буквами
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys('Ivan')

    # Заполнить поле "Фамилия"
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]').send_keys('Иванов')

    # Заполнить поле "Email или телефон"
    driver.find_element(By.XPATH, '//*[@id="address"]').send_keys('79858789020')

    # Заполнить поле "Пароль"
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Qwerty123!')

    # Заполнить поле "Подтверждение пароля"
    driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys('Qwerty123!')

    # Нажать кнопку "Зареегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(3)

    # Проверка что регистрация не прошла, у поля "Имя" появилось сообщение "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    assert driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]').text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


def test_reg_name_less2letters_unsuccess(driver):
    # Перейти на страницу авторизации
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=_0__B9AtVb0')

    # Дождаться появления таба "Номер"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-phone"]')))

    # Нажать на ссылку "Зарегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()

    time.sleep(3)

    # Заполнить поле "Имя" одной русской буквой
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys('И')

    # Заполнить поле "Фамилия"
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]').send_keys('Иванов')

    # Заполнить поле "Email или телефон"
    driver.find_element(By.XPATH, '//*[@id="address"]').send_keys('79858789020')

    # Заполнить поле "Пароль"
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Qwerty123!')

    # Заполнить поле "Подтверждение пароля"
    driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys('Qwerty123!')

    # Нажать кнопку "Зареегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(3)

    # Проверка что регистрация не прошла, у поля "Имя" появилось сообщение "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    assert driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]').text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


def test_reg_name_more30letters_unsuccess(driver):
    # Перейти на страницу авторизации
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=_0__B9AtVb0')

    # Дождаться появления таба "Номер"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-phone"]')))

    # Нажать на ссылку "Зарегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()

    time.sleep(3)

    # Заполнить поле "Имя" 32мя русской буквой
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys('ИванИванИванИванИванИванИванИван')

    # Заполнить поле "Фамилия"
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]').send_keys('Иванов')

    # Заполнить поле "Email или телефон"
    driver.find_element(By.XPATH, '//*[@id="address"]').send_keys('79858789020')

    # Заполнить поле "Пароль"
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Qwerty123!')

    # Заполнить поле "Подтверждение пароля"
    driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys('Qwerty123!')

    # Нажать кнопку "Зареегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    time.sleep(3)

    # Проверка что регистрация не прошла, у поля "Имя" появилось сообщение "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    assert driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]').text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'