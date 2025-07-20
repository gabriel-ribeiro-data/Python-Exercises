# Exercise 009:
# Write a program that reads an integer and displays its multiplication table on the screen.
#
# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

# Defining the number variable.  //  Definindo a variável number.
number = int(input("Enter a number to see its multiplication table: "))

# Showing the multiplication table of the number.  //  Mostrando a tabuada de number.
print('{} x {:2} = {}'.format(number, 1, number * 1)) # {:2} inside {} makes the number occupy 2 spaces.
print('{} x {:2} = {}'.format(number, 2, number * 2)) # {:2} dentro de {} faz com que o número ocupe 2 casas.
print('{} x {:2} = {}'.format(number, 3, number * 3))
print('{} x {:2} = {}'.format(number, 4, number * 4))
print('{} x {:2} = {}'.format(number, 5, number * 5))
print('{} x {:2} = {}'.format(number, 6, number * 6))
print('{} x {:2} = {}'.format(number, 7, number * 7))
print('{} x {:2} = {}'.format(number, 8, number * 8))
print('{} x {:2} = {}'.format(number, 9, number * 9))

# Create an empty line at the end of the code to indicate the end of the program.
# Criar uma linha vazia no final do código para indicar o fim do programa.
