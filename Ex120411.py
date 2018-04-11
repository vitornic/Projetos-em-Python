Sal = float(input('Digite seu salario'))
Tp = int(input('Digite seu tempo de empresa'))
Set = int(input('Informe seu setor [1/2]'))
if (Sal < 850) and (Tp < 3) and (Set == 1):
    DesC = (Sal * 0.05)
    Desc = (Sal - DesC)
elif (Tp < 3) and (Set == 2):
    DesC = (Sal * 0.06)
    Desc = (Sal - DesC)
if (Sal < 850) and (Tp > 3) and (Set == 1):
    DesC = (Sal * 5.5)/100
    Desc = (Sal - DesC)
elif (Tp > 3) and (Set == 2):
    DesC = (Sal * 6.5)/100
    Desc = (Sal - DesC)
    
if (Sal > 850) and (Tp < 3) and (Set == 1):
    DesC = (Sal * 0.07)
    Desc = (Sal - DesC)
elif (Tp < 3) and (Set == 2):
    DesC = (Sal * 0.08)
    Desc = (Sal - DesC)
if (Tp > 3) and (Set == 1):
    DesC = (Sal * 7.5)/100
    Desc = (Sal - DesC)
elif (Tp > 3) and (Set == 2):
    DesC = (Sal * 8.5)/100
    Desc = (Sal - DesC)
    
print('Salário Liq : ',Desc,'valor de desconto : ',DesC)
