# variáveis

saque = False
deposito = float(input('Insira a quantidade que deseja depositar: '))
saldo = deposito
credito = float(input('Insira o limite de crédito: '))
limiteCredito = credito
valor = float(input('Insira o valor que será sacado: '))

# Codigo adaptado do java

if valor <= saldo:
    saque = True
elif valor <= limiteCredito:
    saque = True

# Traduzindo para usuário final

if saque == True:
    print(f'Seu saque de R$ {valor:.2f} foi realizado com sucesso')
else:
    print(f'Seu saque de R$ {valor:.2f} não foi realizado')