# Autor: Guadalupe Iveth Serrano Hernández, A01375932
#Calcula el costo total de una comida en un restaurante, incluyendo la propina y el IVA por separado.

# Escribe tu programa después de esta línea.
st = int (input("costo de la comida: "))
p = st*.13
iva = st*.16
t = st + p + iva

print ("El subtotal es: ", st)
print ("Propina: ", p)
print ("IVA: ", iva)
print (" El costo total es: %.02f ") % (t)