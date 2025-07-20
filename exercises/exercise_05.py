# Exercise 005:
# Write a program that reads an integer and displays its successor and predecessor on the screen.
# 
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

# Defining the number variable.  //  Definindo a variável number.
number = int(input('Enter a number: '))

# Defining the successor and predecessor variables.  //  Definindo as variáveis successor e predecessor.
successor = number + 1
predecessor = number - 1

# Writing the final message.  //  Escrevendo a mensagem final.
print('Analyzing the value {}, its predecessor is {} and its successor is {}.'.format(number, predecessor, successor))

# Create an empty line at the end of the code to indicate the end of the program.
# Criar uma linha vazia no final do código para indicar o fim do programa.
