numeros_str = input("Ingresa una serie de números separados por espacios: ")
numeros_str_lista = numeros_str.split()
numeros = []

for numero_str in numeros_str_lista:
    numero = int(numero_str)
    numeros.append(numero)

for i in range(len(numeros)):
    min_index = i
    for j in range(i + 1, len(numeros)):
        if numeros[j] < numeros[min_index]:
            min_index = j
    numeros[i], numeros[min_index] = numeros[min_index], numeros[i]

print("Lista de números ordenados en orden ascendente:")
for numero in numeros:
    print(numero, end=" ")