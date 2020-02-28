# Guadalupe Iveth Serrano Hernández, A01375932
# Calcula el número total de alumnos inscritos en una clase y el porcentaje de mujeres y hombres de la clase.

# Escribe tu programa después de esta línea.
mi = int (input("Inserta el número de mujeres inscritas: "))
hi = int (input("Inserta el número de hombres inscritos: "))

ta = mi + hi
pm = (mi*100)/ta
ph = (hi*100)/ta

print ("Son: ", ta, "alumnos en total")
print ("El porcentaje de mujeres es de: ", pm)
print ("El porcentaje de hombres es de: ", ph)