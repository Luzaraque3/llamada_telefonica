# programa para calcular el costo de una llamada telefonica

# Toda llamada que dure 3 minutos o menos  tiene un costo de $300
# Cada minuto adicional cuesta $50 pesos

# input

minutos = int(input("ingrese los minutos de la llamada: "))

# processing

if minutos < 3:
    costo = 300

else:
    costo = (minutos * 50) +300 -150

# ouput

print(" el costo de la llamada es: " + str(costo))
