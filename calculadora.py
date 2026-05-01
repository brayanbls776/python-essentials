def suma(a, b):return a + b        
def resta(a, b):return a - b
def multiplicacion(a, b):return a * b
def division(a, b): return a / b if b != 0 else "Error: No se puede dividir por cero."
def obtener_numero(mensaje):
   
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Ingresa un número válido.")
def calculadora():
    opciones = {
        "1": (suma,"+"),
        "2": (resta,"-"),
        "3": (multiplicacion,"*"),
        "4": (division,"/")
    }
    print("Bienvenido a la calculadora")
    while True:
        
        print("Seleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion =input("Ingrese el número de la operación que desea realizar: ")
        
        if opcion == "5":
            print("¡Gracias por usar la calculadora! ¡Hasta luego!")
            break
        
        if opcion in opciones:
            try:
                num1 = obtener_numero("👉Ingrese el primer número: ")
                num2 = obtener_numero("👉Ingrese el segundo número: ")
                
                func, operador = opciones[opcion]
                resultado = func(num1, num2)
                print(f"El resultado de {num1} {operador} {num2} es: {resultado}")
            except ValueError:
                print("Error: Por favor ingrese un número válido.")

        else:
            print("❌Opción no válida. Por favor seleccione una opción del 1 al 5.")  

if __name__ == "__main__":
    calculadora()