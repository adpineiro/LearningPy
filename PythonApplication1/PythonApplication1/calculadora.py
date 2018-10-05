def saluda():
    """Función que devuelve un hola mundo
Este es un comentario de ejemplo para crear un docstring"""
    print("Hola mundo")


# A, B, C son funciones
# A recibe como parametro B para poder crear C
saluda()
documentacion = saluda.__doc__
print(documentacion)
nombre = saluda.__name__
print(nombre)
