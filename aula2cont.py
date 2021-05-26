#Interação com o usuario
a = int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o segundo valor: "))

soma = a + b
sub = a - b
mult = a * b
div = a / b
resto = a % b
print(type(soma))
#convertendo inteiro
soma = str(soma)
print('soma: ' + soma)
#comando format
resultado =('soma: {soma}. \nsubtração: {sub} '
      '\nMultiplicação: {mult}.'
      ' \nDivisão: {div} '
      ' \nResto: {resto} '.format(soma=soma,
                                  sub=sub,
                                  mult=mult,
                                  div=div,
                                  resto=resto))
print(resultado)
print('subtração: ' + str(sub))
print(mult)
#arredondar
print(int(div))
print(div)
print(resto)
# x = '1'
# soma2 = int(x) + 1
# print(soma2)
