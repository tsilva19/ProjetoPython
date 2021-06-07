# encontrar numeros primos
a = int(input('Entre com um valor: '))
for num in range(a+1):
    div = 0
    for x in range(1, num+1):
        resto = num % x
        # print(x, resto)
        if resto == 0:
            # div = div + 1
            div += 1

    if div == 2:
        print('Número {} é primo'.format(num))



     #     for x in range(101):
#    print(x)
