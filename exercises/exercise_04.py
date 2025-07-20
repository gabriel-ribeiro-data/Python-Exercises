# Exercise 004:
# Create a program that reads something from the keyboard and displays its primitive type
# and all possible information about it.
#
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

# Defining the variable.  //  Definindo a variável.
a = input('Enter something: ')  

# Responding with the primitive type of the variable.  //  Respondendo o tipo primitivo da variável.
print('The primitive type of this value is {}.'.format(type(a)))  

# Responding whether the variable contains only spaces.  //  Respondendo se a variável só tem espaços.
print('Only spaces? {}.'.format(a.isspace()))  

# Responding whether the variable is a number.  //  Respondendo se a variável é um número.
print('Is it a number? {}.'.format(a.isnumeric()))  

# Responding whether the variable is alphabetic.  //  Respondendo se a variável é alfabética.
print('Is it alphabetic? {}.'.format(a.isalpha()))  

# Responding whether the variable is alphanumeric.  //  Respondendo se a variável é alfanumérica.
print('Is it alphanumeric? {}.'.format(a.isalnum()))  

# Responding whether the variable is in uppercase.  //  Respondendo se a variável está somente em letras maiúsculas.
print('Is it in uppercase? {}.'.format(a.isupper()))  

# Responding whether the variable is in lowercase.  //  Respondendo se a variável está somente em letras minúsculas.
print('Is it in lowercase? {}.'.format(a.islower()))  

# Responding whether the variable is capitalized.  //  Respondendo se a variável está capitalizada.
print('Is it capitalized? {}.'.format(a.istitle()))  

# Capitalized means starting with a capital letter and the rest in lowercase, e.g., Banana.   
# Capitalizado significa começar com letra maiúscula e o restante em minúsculas, exemplo: Banana.

# Create an empty line at the end of the code to indicate the end of the program.
# Criar uma linha vazia no final do código para indicar o fim do programa.
