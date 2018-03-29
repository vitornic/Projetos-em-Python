min = float(input('Minutos'))
if (min < 200) and (min < 400):
    print('Isento')
    print('Minutos', min)
    print('Taxa',(min)+31.14)
elif (min >= 200):
    taxa = (min * 0.02) + 31.14
    print('Minutos', min)
    print('Taxa: ',taxa)
elif (min >= 400):
    taxa = (min * 0.01) + 31.14
    print('Minutos', min)
    print('Taxa',taxa)
