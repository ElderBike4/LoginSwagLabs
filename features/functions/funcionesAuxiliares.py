import allure


def captura_pantalla(context, descripcion):
    allure.attach(context.driver.get_screenshot_as_png(),descripcion,allure.attachment_type.PNG)

def captura_pantalla_allure(context,descripcion):
    print("Captura de pantalla tomada correctamente")
    allure.attach(context.driver.get_screenshot_as_png(),descripcion,allure.attachment_type.PNG)