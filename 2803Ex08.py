min = float(input('Minutos'))
if (min < 200):
    print('Isento')
    print('Minutos', min)
    print('taxa 31.14')
elif (min >= 200):
    taxa = (min * 0.02)
    print('Minutos', min)
    print('Taxa: ',taxa)
elif (min >= 400):
    taxa = (min * 0.01)
    print('Minutos', min)
    print('Taxa',taxa)
