SA = float(input('Digite seu salário atual '))
if SA < 300:
    VA = (SA * 0.15)
    NS = (SA + VA)
    print('Novo salario :',NS,'Valor de Aumento :',VA)
elif (SA > 300) and (SA <= 600):
    VA = (SA * 0.10)
    NS = (SA + VA)
    print('Novo salario :',NS,'Valor de Aumento :',VA)
elif (SA > 600) and (SA <= 900):
    VA = (SA * 0.05)
    NS = (SA + VA)
    print('Novo salario :',NS,'Valor de Aumento :',VA)
elif SA > 900:
    VA = SA
    print('Novo salario :',NS,'Valor de Aumento :',VA)
