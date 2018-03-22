idade = int(input('Digite sua idade'))
if idade >= 0 and idade < 12:
    print('Você é criança')
elif idade >= 13 and idade < 17:
    print('Você é adolescente')
elif idade >= 17 and idade <= 50:
    print('Você é adulto')
else:
    print('Está na melhor idade')
