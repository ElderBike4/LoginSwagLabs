import time
import allure
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functions.funciones_auxiliares import(
    captura_pantalla_allure,
    agregar_screenshot_allure,
    captura_allure
)

@given('Que estoy en la página de login')
def step_impl(context):
    try:
        context.driver = webdriver.Chrome()
        context.driver.get("https://www.saucedemo.com/")
        screenshot_path = f"./reports/inicio.png"
        #agregar_screenshot_allure(context,screenshot_path)
        captura_allure("login")
    except Exception as e:
        print("Error:", e)
    
    

@when('Ingreso mis credenciales válidas "{username}" "{pwd}"')
def step_impl(context, username, pwd):
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        element.send_keys(username)

        element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        element.send_keys(pwd)
        #agregar_screenshot_allure(context=context,screenshot_path=screenshot_path)
        captura_allure("credenciales")
    except Exception as e:
        print("Error:", e)

@when('Hago click en el botón de inicio de sesión')
def step_impl(context):
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        element.click()
    except Exception as e:
        print("Error:", e)

@then('Se muestra la página principal')
def step_impl(context):
    time.sleep(2)
    captura_allure("menu")
    time.sleep(2)
    context.driver.close()


@when('Ingreso mis credenciales inválidas "{username}" "{pwd}"')
def step_impl(context,username,pwd):
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        element.send_keys(username)

        element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        element.send_keys(pwd)
        captura_allure("Credenciales inválidas")
    except Exception as e:
        print("Error:", e)


@then('Aparece un mensaje de error')
def step_impl(context):
    captura_allure("Mensaje de error")
    time.sleep(2)
    context.driver.close()
