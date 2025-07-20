# Exercise 002:
# Write a program that reads a person's name and displays a welcome message.
#
# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

# Defining the name variable.  //  Definindo a variável name.
name = input('Enter your name: ')

# Writing the welcome message.  //  Escrevendo a mensagem de boas-vindas.
print('It’s a pleasure to meet you, {}!'.format(name))

# Using {} with the .format() method inserts the values inside the parentheses of .format() into the {} placeholders.
# In this exercise, {} will be replaced by the variable `name`.
#
# Utilizar {} com o método .format() insere os valores dentro dos parênteses do .format() nos espaços reservados {}.
# No caso do exercício, {} será substituído pela variável `nome`.
#
# Note: Other methods for formatting, such as f-strings or % formatting, can also be used.
# Obs: Dá para usar outros métodos de formatação, como f-strings ou a formatação com %.
#
# Note 2: {} acts as a placeholder for the value to be inserted.
# Obs 2: {} funciona como um espaço reservado para o valor a ser inserido.

# Create an empty line at the end of the code to indicate the end of the program.
# Criar uma linha vazia no final do código para indicar o fim do programa.
