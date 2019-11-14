from punto import *

Numero = []

while True:
    cantidad = int (raw_input ("digite su cantidad de puntos por calcular la distancia: "))
    if cantidad in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        break

while len (Numero) < cantidad:
    digito = list.append (Punto (self.origen, self.destino))
    if digito not in Numero:
        Numero.append(digito)

x = int (raw_input ("digite su primer punto en x: "))
y = int (raw_input ("digite su primer punto en y: "))
p1 = Punto(x,y)
x = int (raw_input ("digite su segundo punto en x: "))
y = int (raw_input ("digite su segundo punto en x: "))
p2 = Punto(x,y)

distancia = p1.calcular_distancia(p2)
print (distancia)

#int (raw_input ("digite su primer punto: "))
#list.append (Punto (x, y))
