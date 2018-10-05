def decorador (func): #A,B
    def nueva_funcion():
        print("Vamos a ejecutar la función")
        func()
        print("Se ejecuto la función")

    return nueva_funcion #C

@decorador
def saluda():
    print("Hola mundo")

#A, B, C son funciones
#A recibe como parametro B para poder crear C
def suma():
    print(10 + 20)
suma()