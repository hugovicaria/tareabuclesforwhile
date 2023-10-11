"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
año que dura la inversión.
"""
cantidad = float(input("Cantidad a invertir: "))
interes = float(input("Porcentaje de interes anual: "))
a�os = int(input("Cuantos años: "))
for i in range(a�os):
    cantidad *= 1 + interes / 100 
    print("Dinero cuando pasen " + str(i+1) + " años: " + str(round(cantidad, 2)))
