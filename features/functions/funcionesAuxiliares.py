import allure


def captura_pantalla(context, descripcion):
    allure.attach(context.driver.get_screenshot_as_png(),descripcion,allure.attachment_type.PNG)