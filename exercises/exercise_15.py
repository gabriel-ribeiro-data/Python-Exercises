# Exercise 015:
# Write a program that asks for the number of kilometers driven by a rented car and the number of days it was rented. 
# Calculate the amount to pay, knowing that the car costs USD 60 per day and USD 0.15 per kilometer driven.
#
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa USD 60 por dia e USD 0.15 por Km rodado.

# Asking for how many days the car was rented.  //  Perguntando por quantos dias o carro foi alugado.
days = int(input('For how many days was the car rented? '))

# Asking how many kilometers were driven.  //  Perguntando por quantos Km foram rodados.
kilometers = float(input('How many kilometers were driven? '))

# Calculating the price based on days rented.  //  Calculando o preço baseado em dias alugados.
price_for_days = days * 60

# Calculating the price based on kilometers driven.  //  Calculando o preço baseado em Km rodados.
price_for_kilometers = kilometers * 0.15

# Calculating the total price.  //  Calculando o preço total.
total_price = price_for_days + price_for_kilometers

# Showing how much will need to be paid.  //  Mostrando quanto será necessário pagar.
print(f'The total amount to be paid is USD {total_price:.2f}.')
# With f-strings, it is not necessary to use `.format()` because the string is already formatted.
# Com f-strings não é necessário utilizar o `.format()` pois a string ja está formatada.    

# Create an empty line at the end of the code to indicate the end of the program.
# Criar uma linha vazia no final do código para indicar o fim do programa.
                                      