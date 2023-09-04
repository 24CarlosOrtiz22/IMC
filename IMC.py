print("Hola, hoy te ayudaremos a conocer tu índice de masa corporal")
Peso = float(input("Ingresa tu peso en Kg: "))
Altura = float(input("Ingresa tu altura en metros: "))
IMC = Peso / (Altura ** 2)
if IMC < 18.5:
    Categoria = "Bajo peso"
elif 18.5 <= IMC < 25:
    Categoria = "Peso normal"
elif 25 <= IMC < 30:
    Categoria = "Sobrepeso"
else:
    Categoria = "Obesidad"
print(f"Tu IMC es: {IMC:.2f}")
print(f"Categoría: {Categoria}")