'''text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")'''

text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")

x = 1
while x < 11:
    if x % 2 != 0:
        print(x, end=" ")
    x += 1
#Crea un programa con un bucle for y una sentencia break. 
# El programa debe iterar sobre los caracteres en una dirección de correo electrónico, 
# salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea.
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

print("\n")
for digit in "0165031806510":
    if digit == "0":
        print("x",end="")
        continue
    print(digit,end="")