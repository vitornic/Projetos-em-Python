salario = float(input('Digite o salario '))
if (salario <= 429):
    cont = (salario * 7.65)/100
elif (salario >= 429.01) and (salario < 540):
    cont = (salario * 8.65)/100
elif (salario >= 540.01) and (salario < 715):
    cont = (salario * 9.00)/100
elif (salario >= 715.01) and (salario < 1430):
    cont = (salario * 11.00)/100
print('INSS: ',float(cont))
