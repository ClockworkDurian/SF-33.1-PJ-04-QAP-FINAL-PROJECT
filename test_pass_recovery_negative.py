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

def test_reset_password_by_phone_unsuccess(driver):
    # Перейти на страницу восстановления пароля
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=12zFz9P495Q')

    # Дождаться появления таба "Номер"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-phone"]')))

    # Выбрать таб "Номер"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()

    # Ввести номер телефона
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('79858789020')

    # Ввести капчу
    # Здесь необходимо реализовать задержку для возможности ввести капчу вручную
    time.sleep(15)

    # Нажать кнопку "Продолжить"
    driver.find_element(By.XPATH, '//*[@id="reset"]').click()

    # Дождаться появления формы выбора способа восстановления пароля
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="sms-reset-type"]')))

    # Выбрать радиокнопку "По номеру телефона"
    driver.find_element(By.XPATH, '//*[@id="sms-reset-type"]').click()

    # Нажать кнопку "Продолжить"
    driver.find_element(By.XPATH, '//*[@id="reset-form-submit"]').click()

    # Дождаться появления формы ввода кода из СМС
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="otp"]/div[1]/div[1]/input')))

    # Ввести невалидный код из СМС
    # Здесь необходимо реализовать задержку для возможности ввести код из СМС вручную
    time.sleep(25)

    # Нажать кнопку "Продолжить"
    driver.find_element(By.XPATH, '//*[@id="otp"]/div[2]/button').click()

    # Дождаться появления сообщения об ошибке "Неверный код. Повторите попытку"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]')))

    # Проверка что возникла ошибка "Неверный код. Повторите попытку"
    assert driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]').text == 'Неверный код. Повторите попытку'

def test_reset_password_by_email_unsuccess(driver):
    # Перейти на страницу восстановления пароля
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=12zFz9P495Q')

    # Дождаться появления таба "Почта"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-mail"]')))

    # Выбрать таб "Почта"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()

    # Ввести электронную почту
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('fizi@bk.ru')

    # Ввести капчу
    # Здесь необходимо реализовать задержку для возможности ввести капчу вручную
    time.sleep(15)

    # Нажать кнопку "Продолжить"
    driver.find_element(By.XPATH, '//*[@id="reset"]').click()

    # Дождаться появления формы выбора способа восстановления пароля
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email-reset-type"]')))

    # Выбрать радиокнопку "По e-mail"
    driver.find_element(By.XPATH, '//*[@id="email-reset-type"]').click()

    # Нажать кнопку "Продолжить"
    driver.find_element(By.XPATH, '//*[@id="reset-form-submit"]').click()

    # Дождаться появления формы ввода кода из письма
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="otp"]/div[1]/div[1]/input')))

    # Ввести код из письма
    # Здесь необходимо реализовать задержку для возможности ввести код из письма вручную
    time.sleep(50)

    # Нажать кнопку "Продолжить"
    driver.find_element(By.XPATH, '//*[@id="otp"]/div[2]/button').click()

    # Дождаться появления сообщения об ошибке "Неверный код. Повторите попытку"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]')))

    # Проверка что возникла ошибка "Неверный код. Повторите попытку"
    assert driver.find_element(By.XPATH,'//*[@id="page-right"]/div[1]/div[1]/div[1]').text == 'Неверный код. Повторите попытку'
