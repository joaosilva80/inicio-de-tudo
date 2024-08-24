#Escreva um programa que peça ao usuário um número e informe se ele é par ou ímpar.
#
n=int(input('Digite um número: '))
if n%2==1:
    print('{} é par'.format(n))
else: print('{} é ímpar'.format(n))
