# Exercise 011:
# Create a program that reads the width and height of a wall in meters, calculates its area, and 
# the amount of paint needed to cover it, knowing that each liter of paint covers an area of 2m².
#
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade 
# de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

# Defining the width variable.  //  Definindo a variável width.
width = float(input('Type the width of the wall (in meters): '))

# Defining the height variable.  //  Definindo a variável height.
height = float(input('Type the height of the wall (in meters): '))

# Calculating the area of a wall in square meters.  //  Calculando a área da parede em metros quadrados.
wall_area = width * height

# Calculating the amount of paint needed.  //  Calculando a quantidade de tinta necessária.
liters_of_paint = wall_area / 2

# liters_of_paint é um exemplo de uso da snake_case, uma boa prática para nomear uma variável em Python.
# liters_of_paint is an example of using snake_case, a good practice for naming a variable in Python.

# Showing the wall dimensions and the amount of paint needed.
# Mostrando as dimensões da parede e a quantidade de tinta necessária.
print('Your wall has dimensions of {}x{} and an area of {} square meters. ' 
      'To paint this wall, you will need {} liters of paint.'.format(width, height, wall_area, liters_of_paint)) 
       # Correct way to break a print statement.
       # Jeito correto de quebrar um print.
       
# Create an empty line at the end of the code to indicate the end of the program.
# Criar uma linha vazia no final do código para indicar o fim do programa.
