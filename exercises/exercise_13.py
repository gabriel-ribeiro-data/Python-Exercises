# Exercise 013:
# Create an algorithm that reads an employee's salary and shows the new salary with a 15% increase.
#
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# Defining the employee_salary variable.  //  Definindo a variável employee_salary.
employee_salary = float(input("Enter the employee's salary: USD "))

# Defining the new_employee_salary variable.  //  Definindo a variável new_employee_salary.
new_employee_salary = employee_salary * 1.15

print(f'A employee who used to earn USD {employee_salary:.2f}, with a 15% increase, will now earn {new_employee_salary:.2f}.')
# With f-strings, it is not necessary to use `.format()` because the string is already formatted.
# Com f-strings não é necessário utilizar o `.format()` pois a string ja está formatada.    

# Create an empty line at the end of the code to indicate the end of the program.
# Criar uma linha vazia no final do código para indicar o fim do programa.
                                      