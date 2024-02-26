import allure
import pyautogui

def captura_pantalla_allure(context,descripcion):
    print('Captura de pantalla hecha')
    allure.attach(context.driver.get_screenshot_as_png(),descripcion,allure.attachment_type.PNG)

def agregar_screenshot_allure(context, screenshot_path):
    try:
        
        context.driver.save_screenshot(screenshot_path)
        
       
        with open(screenshot_path, 'rb') as png_file:
            png_bytes = png_file.read()
            
            
            allure.attach(
                png_bytes,
                name='captura de pantalla',
                attachment_type=allure.attachment_type.PNG,
            )
            
            
            print(f"Captura de pantalla adjuntada correctamente: {screenshot_path}")
            
    except Exception as e:
        
        print("Error al adjuntar la captura de pantalla a Allure:", e)


def captura_allure(nombre_captura: str):
    if not nombre_captura or not isinstance(nombre_captura, str):
        raise ValueError(
            "El argumento 'nombre' es obligatorio y debe ser de tipo string."
        )
    screenshot_path = f"./reports/{nombre_captura}.png"
    pyautogui.screenshot(screenshot_path)
    # Adjunta la captura de pantalla al informe Allure
    allure.attach.file(
        screenshot_path,
        name="Captura de Pantalla",
        attachment_type=allure.attachment_type.PNG,
    )
