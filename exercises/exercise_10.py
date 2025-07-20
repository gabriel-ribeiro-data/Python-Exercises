# Exercise 010:
# Create a program that reads how much money a person has in their wallet and shows how 
# many dollars they can buy, considering the exchange rate of USD 1.00 = BRL 5.43.
#
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
# dólares ela pode comprar, considere USD 1.00 = BRL 5.43 como cotação.

# Defining the amount_in_brl variable.  //  Definindo a variável amount_in_brl.
amount_in_brl = float(input('How much money do you have in your wallet (in BRL)? '))

# Defining the exchange_rate variable. //  Definindo a variável exchange_rate.
exchange_rate = 5.43

# Calculating the amount in dollars. //  Calculando o valor em dólares.
amount_in_usd = amount_in_brl / exchange_rate

# Showing how many dollars it will be possible to buy.  //  Mostrando quantos dólares será possível comprar.
print('You can buy USD {:.3f}.'.format(amount_in_usd))

# : Begins the format specifier within a formatted string.
# .3f Specifies that the number should be formatted as a floating-point number with exactly 3 decimal places.
#
# : Inicia o especificador de formato dentro de uma string formatada.
# .3f Especifica que o número deve ser formatado como um número de ponto flutuante (decimais) com exatamente 3 casas decimais.

# Create an empty line at the end of the code to indicate the end of the program.
# Criar uma linha vazia no final do código para indicar o fim do programa.
