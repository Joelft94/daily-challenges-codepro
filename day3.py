word = input('Ingrese una palabra: ')

word = word.lower()
counter = 0

for i in range(len(word)):
    if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u':
        counter += 1
    
print(f'La palabra {word} tiene {counter} vocales')

    
    
