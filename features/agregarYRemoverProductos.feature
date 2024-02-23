# language: es

@agregarYRemoverProductos
Característica: Agregar y remover productos

Antecedentes:
    Dado Que me encuentro en la página de login

  @removerProductos
  Esquema del escenario: Remover productos del carrito de compra
    Cuando Ingreso mis credenciales "<username>" "<password>"
    Y Doy click en el botón de inicio de sesión
    Entonces Se ve el menu principal
    Cuando Agrego productos al carrito de compras
    Y Decido quitar los productos del carrito de compra
    Entonces Se muestra el carrito de compra vacío

    Ejemplos:
      | username      | password     |
      | standard_user | secret_sauce |

  @agregarProductos
  Esquema del escenario: Agregar productos al carrito de compra
    Cuando Ingreso mis credenciales usuario "<username>" contraseña "<password>"
    Y Inicio sesión
    Entonces Se observa la página principal
    Cuando Agrego productos al carrito
    Entonces Se muestra la cantidad de productos agregados al carrito

    Ejemplos:
      | username      | password     |
      | standard_user | secret_sauce |