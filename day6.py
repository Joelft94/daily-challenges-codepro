#convert celsius to farenheit 
def celsius_to_farenheit(celsius):
    return (celsius * 9/5) + 32

temp = float(input("Enter temperature in celsius: "))

print(celsius_to_farenheit(temp))


