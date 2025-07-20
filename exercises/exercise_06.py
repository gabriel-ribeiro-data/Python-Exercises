# Exercise 006:
# Create an algorithm that reads a number and shows its double, triple, and square root.
#
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# Defining the number variable.  //  Definindo a variável number.
number = int(input('Enter a number: '))

# Defining the double variable.  //  Definindo a variável double.
double = number * 2

# Defining the triple variable.  //  Definindo a variável triple.
triple = number * 3

# Perform the calculation with spaces, as in (number * 3). //  Fazer a conta espaçada como em (number * 3).

# Defining the square_root variable. //  Definindo a variável square_root.
square_root = pow(number, 0.5) # The square root of a number is the number raised to the power of 0.5 (e.g., √4 = 4^0.5).

# Use _ as a space, as in square_root.  //  Usar _ como espaço como em square_root.

# Always leave a space after the comma if you are going to type something else.
# Depois da vírgula sempre pule espaço se for digitar mais alguma coisa.

# Showing the double of number.  //  Mostrando o dobro de number.
print('The double of {} is {}.'.format(number, double))

# Showing the triple of number. //  Mostrando o triplo de number.
print('The triple of {} is {}.'.format(number, triple))

# Showing the square root of number.  //  Mostrando a raiz quadrada de number.
print('The square root of {} is {}.'.format(number, square_root))

# Create an empty line at the end of the code to indicate the end of the program.
# Criar uma linha vazia no final do código para indicar o fim do programa.
