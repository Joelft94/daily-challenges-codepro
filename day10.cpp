#include <iostream>
#include <vector>
#include <algorithm>

// Funcion para extraer los digitos de un numero y guardarlos en un array
std::vector<int> extractDigits(int number) {
    std::vector<int> digits;
    
    // Extrae los digitos y los guarda en un array
    while (number > 0) {
        digits.push_back(number % 10);
        number /= 10;
    }
    
    // Ordena el array
    std::sort(digits.begin(), digits.end());
    
    return digits;
}

// Funcion para imprimir el array
void printArray(const std::vector<int>& array) {
    for (int digit : array) {
        std::cout << digit << " ";
    }
    std::cout << std::endl;
}

int main() {
    int number;
    
    // Agarra el input del usuario
    std::cout << "Enter an integer: ";
    std::cin >> number;
    
    // Se fija si el numero es negativo
    if (number < 0) {
        std::cout << "Please enter a positive integer." << std::endl;
        return 1;
    }

    // Extrae los digitos y los guarda en un array
    std::vector<int> digitsArray = extractDigits(number);
    
    // Imprime el array ordenado
    std::cout << "The sorted digits in the array are: ";
    printArray(digitsArray);

    return 0;
}
