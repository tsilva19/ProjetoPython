# encontrar numeros primos
a = int(input('Entre com o número: '))

div = 0
for x in range(1, a+1):
    resto = a % x
    print(x, resto)
    if resto == 0:
        # div = div + 1
        div += 1

if div == 2:
    print('Número {} é primo'.format(a))
else:
    print('Número {} não é primo'.format(a))


# for x in range(101):
#    print(x)
