def sumar(a, b):
    return a + b


def multiplicar(a, b):
    return a * b


def main():
    print("VALIDACION DE COMPILACION CON GITHUB ACTIONS")
    print("Grupo: IDSM41")
    print("Aplicacion ejecutada dentro de Docker")

    suma = sumar(5, 3)
    producto = multiplicar(5, 3)

    print(f"Suma: 5 + 3 = {suma}")
    print(f"Multiplicacion: 5 x 3 = {producto}")

    assert suma == 8, "Error en la suma"
    assert producto == 15, "Error en la multiplicacion"

    print("Pruebas de resultados: CORRECTAS")
    print("Ejecucion terminada correctamente")


if __name__ == "__main__":
    main()
