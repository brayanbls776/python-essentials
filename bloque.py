blocks = int(input("Ingresa el número de bloques: "))
height = 0

while blocks > height:
    
    height+=1
    blocks -=height    
print("La altura de la pirámide:",height)
# El programa calcula la altura de una pirámide dada la cantidad de bloques disponibles.