peso = float(input('Digite o valor do peso '))
altura = float(input('Digite sua altura '))
if (peso / altura ** 2) <= 26:
    print('Situação: Normal')
elif 30 >= (peso / altura ** 2) > 26:
    print('Situação: Acima do peso')
elif (peso / altura ** 2) > 30:
    print('Situação: Obeso')
