# Exercise 014:
# Write a program that converts a temperature entered in °C to °F.
# 
# Escreva um programa que converta uma temperatura digitada em °C para °F.

# Defining the celsius variable.  //  Definindo a variável celsius.
celsius = float(input('Enter the temperature in °C: '))

# Converting the temperature from °C to °F.  //  Convertendo a temperatura de °C para °F.
fahrenheit = (9/5 * celsius) + 32

# Showing the converted temperature.  //  Mostrando a temperatura convertida.
print(f'The temperature of {celsius}°C corresponds to {fahrenheit}°F.')
# With f-strings, it is not necessary to use `.format()` because the string is already formatted.
# Com f-strings não é necessário utilizar o `.format()` pois a string ja está formatada.    

# Create an empty line at the end of the code to indicate the end of the program.
# Criar uma linha vazia no final do código para indicar o fim do programa.
                                      