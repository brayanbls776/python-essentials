print("hola mundo123")
# ===== TIPOS DE VARIABLES EN PYTHON =====

# 1. NÚMEROS (int - enteros)
edad = 25
cantidad = 100
negativo = -50
print(f"Enteros: {edad}, {cantidad}, {negativo}")

# 2. NÚMEROS (float - decimales)
precio = 19.99
altura = 1.75
pi = 3.14159
print(f"Decimales: {precio}, {altura}, {pi}")

# 3. CADENAS DE TEXTO (string)
nombre = "Juan"
apellido = 'García'
mensaje = """Este es un
texto de varias
líneas"""
print(f"Textos: {nombre} {apellido}")

# 4. BOOLEANOS (True/False)
activo = True
disponible = False
es_mayor = edad > 18
print(f"Booleanos: {activo}, {disponible}, {es_mayor}")

# 5. LISTAS (colección ordenada y modificable)
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "plátano", "naranja"]
mixto = [1, "texto", 3.14, True]
print(f"Listas: {numeros}, {frutas}")

# 6. TUPLAS (colección ordenada e inmutable)
coordenadas = (10, 20)
persona_tupla = ("Ana", 30, "Madrid")
print(f"Tuplas: {coordenadas}, {persona_tupla}")

# 7. DICCIONARIOS (pares clave-valor)
persona = {
    "nombre": "Carlos",
    "edad": 28,
    "ciudad": "Barcelona",
    "casado": False
}
print(f"Diccionario: {persona}")

# 8. CONJUNTOS (set - sin orden, sin duplicados)
conjunto = {1, 2, 3, 4, 5}
palabras = {"python", "java", "python"}  # Los duplicados se eliminan
print(f"Conjuntos: {conjunto}, {palabras}")

# 9. NONE (valor vacío/nulo)
valor_none = None
print(f"None: {valor_none}")

# ===== VERIFICAR TIPO DE VARIABLE =====
print("\n--- Verificando tipos ---")
print(f"Tipo de edad: {type(edad)}")
print(f"Tipo de precio: {type(precio)}")
print(f"Tipo de nombre: {type(nombre)}")
print(f"Tipo de activo: {type(activo)}")
print(f"Tipo de numeros: {type(numeros)}")
print(f"Tipo de persona: {type(persona)}")
print(f"Tipo de valor_none: {type(valor_none)}")

# ===== CONVERSIÓN DE TIPOS =====
print("\n--- Conversión de tipos ---")
numero_texto = "123"
numero_convertido = int(numero_texto)
print(f"'{numero_texto}' convertido a int: {numero_convertido}")

texto_numero = str(456)
print(f"456 convertido a string: {texto_numero}")

decimal = float("3.14")
print(f"Convertido a float: {decimal}")


