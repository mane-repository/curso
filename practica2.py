calificacion = int(input("Ingresa la calificación:"))
total = 1
suma = 0
promedio = 0
while calificacion > 0:
    suma = suma + calificacion
    calificacion = int(input("Ingresa la calificación:"))
    total = total + 1

total = total - 1
if total > 0:
    promedio = suma / total

print("RESULTADOS")
print("Total de calificaciones ingresadas: ", total)
print("Promedio de calificaciones:", promedio)
