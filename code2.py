# Variáveis

taxa = 0
buy_value = float(input('Insira o valor da compra: '))
client_type = input('Insira o tipo do cliente. Ex: Bronze, Prata ou Ouro:')
first_buy = input('É a sua primeira compra? Ex: S ou N: ')

# Código adaptado do Java
if buy_value >= 500 or client_type == 'ouro':
    taxa = 15
else:
    if (client_type == 'prata' or first_buy == 'S' or buy_value >= 400):
        taxa = 10
    else:
        if (buy_value>= 200 or client_type == 'bronze'):
            taxa = 5
print(taxa)