# Exercise 008:
# Write a program that reads a value in meters and displays it converted to centimeters and millimeters.
#
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# Defining the meter variable.  //  Definindo a variável meter.
meter = float(input('Measure in meters: '))

# Defining the centimeter variable.  //  Definindo a variável centimeter.
centimeter = meter * 100

# Defining the millimeter variable.  //  Definindo a variável millimeter.
millimeter = meter * 1000

# Showing the measurement in centimeters and millimeters.  //  Mostrando a medida em centímetros e milímetros.
print('The measurement of {} meters is equivalent to:\n{} centimeters\n{} millimeters.'.format(meter, centimeter, millimeter))

# Create an empty line at the end of the code to indicate the end of the program.
# Criar uma linha vazia no final do código para indicar o fim do programa.
