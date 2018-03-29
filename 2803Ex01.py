Kw = input('Digite os kw gastos ')
Kw = float(Kw)
if (Kw <= 100):
    consumo = (Kw * 0.08)
elif (Kw > 100) and (Kw <= 200):
    consumo = (Kw * 0.10)
elif (Kw > 200) and (Kw <= 500):
    consumo = (Kw * 0.12)
else:
    consumo = (Kw * 0.15)
icms = (consumo * 0.18)
total = (consumo + icms)
print('O valor pago ao consumo de energia é: ',consumo)
print('Valor icms: ',icms)
print('Total: ',total)
