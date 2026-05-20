'''
Decorador para imprimir antes y despues
Crea un decorador que imprima un mensaje antes y despues de ejecutar una funcion.
Probalo con una funcion que imprima “Hola mundo”.
'''
def imprimir(funcion):
    def nose():
        print("antes...")
        funcion()
        print("después...")
    return nose

@imprimir
def palabra():
    print("Hola Mundo")

palabra()

