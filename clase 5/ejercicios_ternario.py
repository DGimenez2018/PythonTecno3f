# ================================================================
# EJERCICIOS - Operador Ternario, *args y manejo de argumentos
# ================================================================


# ----------------------------------------------------------------
# 1. Calcular el mayor de dos números ingresados por teclado
# ----------------------------------------------------------------
def ejercicio_1():
    try:
        a = int(input("Ingresá el primer número: "))
        b = int(input("Ingresá el segundo número: "))
    except ValueError:
        print("Error: debés ingresar números enteros válidos")
        return
    ## Validacion en el caso de que el usuario ingrese los 2 valores iguales
    if a == b:
        print(f"Los dos números son iguales: {a}")
    else:
        mayor = a if a > b else b
        print(f"El mayor es: {mayor}")


# ------------------------------------------------------------
# 2. Buscar una palabra en una lista ingresada por teclado
# -----------------------------------------------------------
def ejercicio_2(*palabras):
    buscar = input("¿Qué palabra querés buscar? ")

    resultado = "encontrada " if buscar.lower() in [p.lower() for p in palabras] else "no encontrada"

    print(f"La palabra '{buscar}' fue {resultado}")


# -------------------------------------------
# 3. Determinar si un número es par o impar
# -------------------------------------------
def ejercicio_3():
    try:
        numero = int(input("Ingresá un número positivo: "))
        if numero < 0:
            raise ValueError
    except ValueError:
        print("Error: debés ingresar un número entero positivo")
        return

    paridad = "par" if numero % 2 == 0 else "impar"

    print(f"El número {numero} es {paridad}")


# --------------------------------------------------
# 4. Calcular el promedio de una lista de números
# -------------------------------------------------
def ejercicio_4(*numeros):
    promedio = sum(numeros) / len(numeros) if len(numeros) > 0 else 0

    print(f"El promedio es: {promedio:.2f}")


# ----------------------------------------------------------------
# 5. Imprimir un mensaje de error si no se pasan suficientes args
# ----------------------------------------------------------------
def ejercicio_5(**kwargs):
    minimo_requerido = 3

    print(f"Argumentos recibidos: {kwargs}") if len(kwargs) >= minimo_requerido else print(f"Error: se necesitan al menos {minimo_requerido} argumentos, recibiste {len(kwargs)}")


# =============
# EJECUCIÓN
# ===========
if __name__ == "__main__":
    print("\n--- Ejercicio 1: Mayor de dos números ---")
    ejercicio_1()

    print("\n--- Ejercicio 2: Buscar palabra en lista ---")
    ejercicio_2("boca", "river", "independiente", "almagro", "sacachispa")

    print("\n--- Ejercicio 3: Par o impar ---")
    ejercicio_3()

    print("\n--- Ejercicio 4: Promedio de números ---")
    ejercicio_4(44, 111, 22, 59, 72)

    print("\n--- Ejercicio 5: Validación de argumentos ---")

    ejercicio_5(nombre="Diego", apellido="Gimenez")                                    
    ejercicio_5(nombre="Diego", apellido="Gimenez", email="dgimenez@tecno3f.com")      
