def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True
 
 
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))
 
#Verifica si se puede formar un triángulo con los lados dados. Para que tres lados formen un triángulo,
#la suma de las longitudes de cualquier par de lados debe ser mayor que la longitud del tercer lado.     