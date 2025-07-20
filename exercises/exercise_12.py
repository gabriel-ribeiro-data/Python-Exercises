# Exercise 012:
# Create an algorithm that reads the price of a product and shows its new price with a 5% discount.
#
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

# Defining the product_price variable.  //  Definindo a variável product_price.
product_price = float(input('What is the price of the product? USD '))  # Do not round input values.
                                                                        # Não aproximar valores de entrada.

# Defining the new_product_price variable.  //  Definindo a variável new_product_price.
new_product_price = product_price * 0.95

# Showing the new price with the discount applied.  //  Mostrando o novo preço com o desconto aplicado.
print('The product that used to cost USD {:.2f} will cost USD {:.2f} with a 5% discount.'.format(product_price, new_product_price))

# : Begins the format specifier within a formatted string.
# .2f Specifies that the number should be formatted as a floating-point number with exactly 2 decimal places.
#
# : Inicia o especificador de formato dentro de uma string formatada.
# .2f Especifica que o número deve ser formatado como um número de ponto flutuante (decimais) com exatamente 2 casas decimais.

# Create an empty line at the end of the code to indicate the end of the program.
# Criar uma linha vazia no final do código para indicar o fim do programa.
