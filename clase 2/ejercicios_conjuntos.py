# Conjuntos de alumnos
alumnos_python = {"Ana", "Carlos", "Lucía", "Pedro", "Sofía", "Marcos"}
alumnos_base_datos = {"Carlos", "Sofía", "Juan", "Valeria", "Marcos", "Elena"}

print("=" * 50)
print("ALUMNOS PYTHON:    ", alumnos_python)
print("ALUMNOS BASE DATOS:", alumnos_base_datos)
print("=" * 50)

# 1 - UNIÓN: elementos que están en A o en B, o en ambos
union = alumnos_python | alumnos_base_datos
print("\n1. Alumnos en Python O en Base de Datos (o en ambos):")
print("   Unión:", union)

# 2 - INTERSECCIÓN: elementos que están en A y en B
interseccion = alumnos_python & alumnos_base_datos
print("\n2. Alumnos en Python Y en Base de Datos (en ambos):")
print("   Intersección:", interseccion)

# 3 - DIFERENCIA : elementos que están en A o en B, pero no en ambos
dif_simetrica = alumnos_python.symmetric_difference(alumnos_base_datos)
print("\n3. Alumnos en Python O en Base de Datos, pero NO en ambos:")
print("   Diferencia:", dif_simetrica)

# 4 - verificar si A es subconjunto de B
print("\n4. ¿Es el conjunto de alumnos de Python un subconjunto del de Base de Datos?")
es_subconjunto = alumnos_python.issubset(alumnos_base_datos)
print("  ", es_subconjunto)

# Caso extra: subconjunto real para mostrar True
alumnos_seleccionados = {"Carlos", "Sofía"}
es_subconjunto_seleccionados = alumnos_seleccionados.issubset(alumnos_base_datos)
print(f"\n   ¿Es {alumnos_seleccionados} subconjunto de alumnos de Base de Datos?")
print("  ", es_subconjunto_seleccionados)

# 5 - numero de elementos del conjunto PY y DB
print("\n5. Número de elementos en cada conjunto:")
print("   Alumnos en Python:    ", len(alumnos_python))
print("   Alumnos en Base de Datos:", len(alumnos_base_datos))

print("=" * 50)
