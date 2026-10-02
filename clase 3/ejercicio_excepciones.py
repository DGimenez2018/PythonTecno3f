# ========================
# Manejo de excepciones
# Práctico Clase 3 
# ======================
HISTORIAL = "historial.txt"

# ------------
# ValueError
# -------------
def pedir_numero(mensaje):
    """Solicita un número al usuario. Repite hasta obtener un float válido."""
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Error: Debe ingresar un número válido (ej: 5, 3.14).\n")


# ------------------------------------
# Selección de operación con lista
# ------------------------------------
operaciones = ["Sumar", "Restar", "Multiplicar", "Dividir"]

def elegir_operacion():
    """Muestra la lista de operaciones y retorna la opción elegida (1-4)."""
    print("\n  Operaciones disponibles:")
    for i, opciones in enumerate(operaciones, start=1):
        print(f"    [{i}] {opciones}")

    while True:
        try:
            opcion = int(input("\n  Elegí una opción (1-4): "))
            if opcion < 1 or opcion > 4:
                raise ValueError
            return opcion
        except ValueError:
            print("Error: Ingresá un número entre 1 y 4.\n")


# -------------------
# FileNotFoundError
# --------------------
def guardar_historial(entrada):
    """Intenta abrir el archivo historial. Si no existe, lo crea."""
    try:
        with open(HISTORIAL, "r") as f:
            contenido = f.read()
    except FileNotFoundError:
        print(f"El archivo '{HISTORIAL}' no existe. Creándolo...")
        with open(HISTORIAL, "w") as f:
            f.write("=== Historial de operaciones ===\n")
        print(f"Archivo '{HISTORIAL}' creado correctamente.\n")

    # Ahora sí guardamos el registro
    with open(HISTORIAL, "a") as f:
        f.write(entrada + "\n")


# ------------------------------------
# Consigna 1, 2, 3 y 5 — operación
# ------------------------------------
def operar(num1, num2, opcion):
    """
    Ejecuta la operación seleccionada manejando:
      - Consigna 1: ZeroDivisionError al dividir por cero
      - Consigna 2: TypeError al sumar tipos incompatibles
      - Consigna 3: KeyError al acceder a clave inexistente en el diccionario
      - Consigna 5: ZeroDivisionError + ValueError en la división
    """

    # KeyError: el diccionario mapea opcion --> nombre
    ops = {1: "suma", 2: "resta", 3: "multiplicacion", 4: "division"}

    try:
        nombre_op = ops[opcion]   # Si opcion no existe --> KeyError
    except KeyError:
        print(f"Error: La operación con clave '{opcion}' no existe en el diccionario.")
        return None

    resultado = None

    # Consigna 2 — TypeError
    if nombre_op == "suma":
        try:
            # Demostramos TypeError intentando sumar con un tipo incompatible internamente
            valor_invalido = "cadena de texto"
            _ = num1 + valor_invalido   # Esto dispara el TypeError
        except TypeError:
            print("Error de tipo: No se puede sumar un numero con una cadena de texto.")
        # La suma real se hace con los dos números válidos
        resultado = num1 + num2

    elif nombre_op == "resta":
        resultado = num1 - num2

    elif nombre_op == "multiplicacion":
        resultado = num1 * num2

    elif nombre_op == "division":
        try:
            if num2 == 0:
                raise ZeroDivisionError
            resultado = num1 / num2
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero (ZeroDivisionError).")
            return None
        except ValueError:
            print("Error: Uno de los valores no es un numero válido (ValueError).")
            return None

    return resultado


# =================
# Flujo principal
# ================
def main():
    print("=" * 45)
    print("  Práctico Clase 3")
    print("=" * 45)

    fin_ejecucion = True
    while fin_ejecucion:
        print()
        num1 = pedir_numero("  Ingresá el primer número: ")
        num2 = pedir_numero("  Ingresá el segundo número: ")

        # El usuario elige la operación
        opcion = elegir_operacion()

        # Ejecutamos la operación con manejo de excepciones
        resultado = operar(num1, num2, opcion)

        if resultado is not None:
            nombre = operaciones[opcion - 1]
            linea = f"{nombre}: {num1} y {num2} = {resultado}"
            print(f"\n Resultado — {linea}")
            # Guardamos en historial
            guardar_historial(linea)
        fin_ejecucion = False

    print("\n  Fin del programa.")
    print("=" * 45)

 
if __name__ == "__main__":
    main()
