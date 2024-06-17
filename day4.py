entrada = input("Ingrese los numeros: ")

num = [int(i) for i in entrada.split(',')]


lista = list(num)

print(sorted(lista))
