# language: es

@login
Característica: Iniciar sesión

Antecedentes:
    Dado Que estoy en la página de login

  @loginValido
  Esquema del escenario: Iniciar sesión con credenciales válidas
    Cuando Ingreso mis credenciales válidas "<username>" "<password>"
    Y Hago click en el botón de inicio de sesión
    Entonces Se muestra la página principal

    Ejemplos:
      | username                | password     |
      | standard_user           | secret_sauce |


  @loginInvalido
  Esquema del escenario: Iniciar sesión con credenciales inválidas
    Cuando Ingreso mis credenciales inválidas "<username>" "<password>"
    Y Hago click en el botón de inicio de sesión
    Entonces Aparece un mensaje de error

    Ejemplos:
      | username        | password     |
      | locked_out_user | secret_sauce |