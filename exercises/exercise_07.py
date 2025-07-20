# Exercise 007:
# Develop a program that reads two grades from a student, calculates, and displays their average.
#
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

# Defining the first_grade variable.  //  Definindo a variável first_grade.
first_grade = float(input("Student's first grade: "))

# Defining the second_grade variable.  //  Definindo a variável second_grade.
second_grade = float(input("Student's second grade: "))

# Defining the average variable.  //  Definindo a variável average.
average = (first_grade + second_grade) / 2

# Showing the student's average.  //  Mostrando a média do estudante.
print('The average between {} and {} is {}.'.format(first_grade, second_grade, average))

# Create an empty line at the end of the code to indicate the end of the program.
# Criar uma linha vazia no final do código para indicar o fim do programa.
