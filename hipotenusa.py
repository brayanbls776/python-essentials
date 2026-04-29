#Crear una función que calcule la hipotenusa de un triángulo rectángulo dados los catetos.
a = float(input("Ingrese el valor del cateto a: "))
b = float(input("Ingrese el valor del cateto b: "))

def calcular_hipotenusa(a, b):
    c = (a**2 + b**2)**0.5
    return c
print("La hipotenusa del triángulo rectángulo es:",  calcular_hipotenusa(a, b))
