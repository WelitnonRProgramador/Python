texto = '|   produto   |   Fabricante   |    Valor   |'
print(texto.center(10))
for i in range(len(texto)+3):
    print('-', end='')