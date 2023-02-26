cine = []

for x in range(5): 
    cine.append(input("Agregar pelicula: "+str(x+1)))

print(cine)

eliminar = input("Quitar pelicula")

cine.remove(eliminar)

print(cine)

#Escribir un programa donde ingreses 5 numeros en un arreglo y que se elimine el numero menos
#del arreglo por medio de un input

#9 5 7 8
