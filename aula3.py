
a = int(input('Primeiro Valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print("o maior número é {}".format(a))
elif b > a and b > c:
    print("o maior numero é {}".format(b))
else:
    print('o maior numero é {}'.format(c))
print('final do programa')
