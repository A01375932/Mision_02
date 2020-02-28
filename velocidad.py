# Autor: Guadalupe Iveth Serrano Hernández, A01375932
# Calcula la distancia de un auto que viaja a 6 y 3.5 hrs, y el tiempo que requiere para recorrer 485 km

# Escribe tu programa después de esta línea.
t1 = 6
t2 = 3.5
d = 485
v = int (input("teclea la velocidad "))
Distancia1 = v*t1
Distancia2 = v*t2
Tiempo = d//v

print ("La distancia que recorre en 6 hrs es: ", Distancia1, "km")
print ("La distancia que recorre en 3.5 hrs es: ", Distancia2, "km")
print ("El tiempo que requiere para recorrer 485 km es: ", Tiempo, "hrs")
