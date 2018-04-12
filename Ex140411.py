preco = float(input('Digite o preço '))
dp = input('Informe seu departamento [a/b/c]')
cor = input('Digite a cor [azul/branca/verde/preta]')
if (dp == 'a'):
    if (cor == 'azul'):
        prec = (preco * 0.06)
    if (cor == 'branca'):
        prec = (preco * 0.07)
    if (cor == 'verde'):
        prec = (preco * 0.08)
    if (cor == 'preta'):
        prec = (preco * 0.09)

if (dp == 'b'):
    if (cor == 'azul'):
        prec = (preco * 6.3)/100
    if (cor == 'branca'):
        prec = (preco * 7.4)/100
    if (cor == 'verde'):
        prec = (preco * 8.2)/100
    if (cor == 'preta'):
        prec = (preco * 9.1)/100
        
if (dp == 'c'):
    if (cor == 'azul'):
        prec = (preco * 5.6)/100
    if (cor == 'branca'):
        prec = (preco * 6.7)/100
    if (cor == 'verde'):
        prec = (preco * 7.8)/100
    if (cor == 'preta'):
        prec = (preco * 10.9)/100
PF = (preco - prec)
print('O produto está com o desconto de: ',prec,'e seu preço é: ',PF)
