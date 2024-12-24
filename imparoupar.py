#Escreva um programa que classifique um número como par ou ímpar.

#Início

import sys
 
while True:
 numero = int(input('Digite um número: '))
 if numero %1 == 0:
   print(f'O número {numero} é ímpar')
 else:
   print(f'O número {numero} é par')
 
 continuar = input('Gostaria de consultar outro número? sim/não: ')
 if continuar != 'sim':
   print('Encerrado')
   break
   

sys.exit(0)