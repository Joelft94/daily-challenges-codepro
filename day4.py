entrada = input("Ingrese los numeros: ")

num = [int(i) for i in entrada.split(',')]


lista = list(num)

print(sorted(lista))




# lista = list(map(int, num.split()))

# lista_ascendente = sorted(lista)

# print(lista_ascendente)
