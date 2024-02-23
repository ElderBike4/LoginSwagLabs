import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('Que Me encuentro en la página de login')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")

@when('Ingreso mis credenciales "{username}" "{pwd}"')
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

@when('Doy click en el botón de inicio de sesión')
def step_impl(context):
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        element.click()
    except Exception as e:
        print("Error:",e)

@then('Se ve el menu principal')
def step_impl(context):
    time.sleep(2)


@when('Agrego productos al carrito de compras')
def step_impl(context):
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        element.click()

        element = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light"))
        )
        element.click()

        element = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))
        )
        element.click()
    except Exception as e:
        print("Error:", e)

@when('Decido quitar los productos del carrito de compra')
def step_impl(context):
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "shopping_cart_container"))
        )
        element.click()
        element = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))
        )
        element.click()
        element = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "remove-sauce-labs-bike-light"))
        )
        element.click()
        element = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "remove-sauce-labs-bolt-t-shirt"))
        )
        element.click()
        time.sleep(2)
    except Exception as e:
        print("Error:",e)

@then('Se muestra el carrito de compra vacío')
def step_impl(context):
    time.sleep(4)
    context.driver.close()


@when('Ingreso mis credenciales usuario "{username}" contraseña "{pwd}"')
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

@when('Inicio sesión')
def step_impl(context):
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        element.click()
        time.sleep(2)
    except Exception as e:
        print("Error:",e)

@then('Se observa la página principal')
def step_impl(context):
    time.sleep(2)

@when('Agrego productos al carrito')
def step_impl(context):
    try:
        element = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        element.click()

        element = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light"))
        )
        element.click()

        element = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))
        )
        element.click()
    except Exception as e:
        print("Error:", e)

@then('Se muestra la cantidad de productos agregados al carrito')
def step_impl(context):
    time.sleep(4)
