"""
Enrique Aranda Gutiérrez
Carlos Ariel González Ramírez
Eric Fernando Panas López Dellamary
Juan Pablo Zepeda Orozco

07/10/2025

Dado un número, el programa regresa todos los números primos 
menores o iguales a dicho número.
"""

#Declaraciones
def es_primo(numero):
    if numero > 1:
        primo = True
        x = 2
        while x < numero:
            if numero % x == 0:
                primo = False
                break
            x += 1
    return primo

# Entradas
num = int(input("Ingrese un número entero: "))

# Proceso
indice = 0
primos = []

for numero in range(2,num+1):
    if es_primo(numero):
        primos.append(numero)

primos_salida = str(primos)[1:-1]

# Salidas
print(f'Los números primos menores o iguales a {num} son: {primos_salida}.')