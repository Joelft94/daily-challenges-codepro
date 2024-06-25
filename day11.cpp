#include<iostream>

// function to check if a string is palindrome

int main(){
    std::string str;
    std::cout << "Enter a string: ";
    std::cin >> str;
    int n = str.length();
    bool isPalindrome = true;
    for (int i = 0; i < n / 2; i++) {
        if (str[i] != str[n - i - 1]) {
            isPalindrome = false;
            break;
        }
    }
    if (isPalindrome) {
        std::cout << "The string is a palindrome." << std::endl;
    } else {
        std::cout << "The string is not a palindrome." << std::endl;
    }
    
    return 0;
}