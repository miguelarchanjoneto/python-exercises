#Faça um programa que peça a idade do usuário e informe se ele pode votar.

#Requirements
#1 - solicitar idade do usuário 
#2 - estipular idade mínima para votar
#3 - se a idade do usuário for = ou > que a idade mínima, então ele pode votar
#4 - se não, ele não pode votar

#Início 

import sys

idade_usu = int(input('Digite a sua idade: '))

if idade_usu >= 16:
    print('você pode votar')
else:
    print('não pode votar ainda, apenas com 16 anos')


sys.exit(0)