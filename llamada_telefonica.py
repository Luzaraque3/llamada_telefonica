# programa para calcular el costo de una llamada telefonica

# Toda llamada que dure 3 minutos o menos  tiene un costo de $300
# Cada minuto adicional cuesta $50 pesos

print("-----------------------------------")
print("----------INGRESAR NUMERO----------")
print("-----------------------------------")

# input
x = int(input("INGRESE UN MUMERO: "))

# processing

if x >4:
    y = 300

else:
    y = (x * 50) + 50

# ouput
print("---------------------------------")
print("-------------RESULTADO-----------")
print("---------------------------------")

print ("los gastos totales son " + str(y))
