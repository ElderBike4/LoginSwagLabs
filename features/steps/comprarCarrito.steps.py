import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('Estoy en la página de login')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")

@when('Ingreso credenciales válidas "{username}" "{pwd}"')
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


    except Exception as e:
        print("Error:", e)
@when('Hago click en el botón de inicio de sesion')
def step_impl(context):
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        element.click()
    except Exception as e:
        print("Error:",e)

@then('Se ve la página principal')
def step_impl(context):
    time.sleep(2)

@when('Agrego productos al carrito de compra')
def step_impl(context):
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        element.click()
    except Exception as e:
        print("Error No se encontro:", e)

@then('Se muestra la cantidad de productos agregados al carrito de compra')
def step_impl(context):
    time.sleep(2)


@when('Reviso mi carrito de compra')
def step_impl(context):
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "shopping_cart_container"))
        )
        element.click()
        time.sleep(2)
    except Exception as e:
        print("Error:", e)


@when('Confirmo mis productos agregados')
def step_impl(context):
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        element.click()
        time.sleep(2)
    except Exception as e:
        print("Error:", e)


@when('Agrego mis datos de envío "{name}" "{lastname}" "{zipcode}"')
def step_impl(context,name,lastname,zipcode):
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        element.send_keys(name)

        element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "last-name"))
        )
        element.send_keys(lastname)

        element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "postal-code"))
        )
        element.send_keys(zipcode)
    except Exception as e:
        print("Error:", e)


@when('Confirmo mi orden de compra')
def step_impl(context):
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )
        time.sleep(2)
        element.click()
    except Exception as e:
        print("Error:", e)


@then('Se muestra un mensaje de confirmación de compra')
def step_impl(context):
    time.sleep(2)

