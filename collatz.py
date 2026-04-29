
# toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
# si es par, evalúa un nuevo c0 como c0 ÷ 2;
# de lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1;
# si c0 ≠ 1, salta al punto 2.
# La hipótesis dice que, independientemente del valor inicial de c0, el valor siempre tiende a 1.
c0 = int(input("Ingrese un número entero positivo: "))
count = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    count += 1
    print(c0)
print("Número de pasos: ", count)