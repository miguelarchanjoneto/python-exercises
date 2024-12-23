#Crie um programa que determine se um número é positivo, negativo ou zero

#Requiriments:
#1 - input número do usuário
#2 - identificar se o número é positivo, negativo ou zero
#3 - mostrar o resultado da análise 

#Início 

while True:
 try:
  num_usu = int(input('Digite um número: '))
  if num_usu < 0:
   print(f'O número {num_usu} é negativo')
  elif num_usu == 0:
   print(f'O número é zero')
  else:
   print(f'O número {num_usu} é positivo')

  continuar = input('Gostaria de ver outro número? (sim/não): ')
  if continuar != "sim":
   print('encerrado')

 except ValueError:
  print('erro, digite um número válido')


