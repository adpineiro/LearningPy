"""Esta es un aplicación de consola para practicar python
Consta de una calculadora
Da la fecha y hora del sistema
Crea matrices aleatorias
Crea matrices a partir de datos del usuario"""


# import calculadora

def calculo():
    print("Modo calculadora")
    print("1: Suma\n2:Resta\n3:Multiplicacion\n4:Division")

def calendario():
    print("Modo calendario")

def random_matrix():
    print("Modo matriz aleatoria")

def user_matrix():
    print("Modo matriz del usuario")

def exit_func():
    print("Desea salir?")

def inicio():
    print("Inicio: Seleccione la acción\n")
    print("1: Calculadora\n2:Calendario\n3:Matriz aleatoria\n4:Matriz usuario\n5:Salir")
    seleccion=int(input())
    if seleccion == 1:
        calculo()
    elif seleccion == 2:
        calendario()
    elif seleccion == 3:
        random_matrix()
    elif seleccion == 4:
        user_matrix()
    elif seleccion == 5:
        exit_func()
    else:
        print("Selección incorrecta, intentelo de nuevo")


while True :
    inicio()

