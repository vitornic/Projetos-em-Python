SalMed = float(input('Digite seu salário '))
if SalMed > 400:
    SalMed = (SalMed * 0.30)
    print('Crédito :', SalMed)
elif 300 <= SalMed >= 400:
    SalMed = (SalMed * 0.25)
    print('Crédito : ', SalMed)
elif 200 <= SalMed >= 300:
    SalMed = (SalMed * 0.20)
    print('Crédito :', SalMed)
elif SalMed <= 200:
    SalMed = (SalMed * 0.15)
    print('Crédito :', SalMed)
