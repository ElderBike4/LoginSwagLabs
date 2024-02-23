# language: es

@comprarCarrito
Característica: Comprar carrito

Antecedentes:
    Dado Estoy en la página de login

  Esquema del escenario: Comprar los productos del carrito
    Cuando Ingreso credenciales válidas "<username>" "<password>"
    Y Hago click en el botón de inicio de sesión
    Entonces Se ve la página principal
    Cuando Agrego productos al carrito de compra
    Entonces Se muestra la cantidad de productos agregados al carrito de compra
    Cuando Reviso mi carrito de compra
    Y Confirmo mis productos agregados
    Y Agrego mis datos de envío "Superman" "Hero" "91000"
    Y Confirmo mi orden de compra
    Entonces Se muestra un mensaje de confirmación de compra

    Ejemplos:
      | username      | password     |
      | standard_user | secret_sauce |