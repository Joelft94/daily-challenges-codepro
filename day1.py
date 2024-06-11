word = input("Ingrese la palabra: ")[::-1]
print(word)

# Otra forma

word2 = input("Ingrese la palabra: ")

for i in range(len(word2)-1, -1, -1):
    print(word2[i], end="") # end="" para que no haga salto de linea
    


