#Média de Notas: Peça ao usuário para inserir cinco notas de alunos. Calcule a média das notas e exiba se o aluno foi aprovado (média maior ou igual a 7), em recuperação (média entre 5 e 6.9) ou reprovado (média menor que 5).

#REQUIREMENTS
#1 - solicitar a primeira nota ao usuário
#2 - solicitar a segunda nota ao usuário
#3 - solicitar a terceira nota ao usuário
#4 - solicitar a quarta nota ao usuário
#5 - solicitar a quinta nota ao usuário
#6 - avaliar se aprovou ou recuperação ou reprovou
#7 - mostrar o resultado

nota_1 = int(input("Insira a primeira nota: "))
nota_2 = int(input("Insira a segunda nota: "))
nota_3 = int(input("Insira a terceira nota: "))
nota_4 = int(input("Insira a quarta nota: "))
nota_5 = int(input("Insira a quinta nota: "))
media = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5) / 5
if media > 7:
    print(f"Aprovado, com a media {media}")
elif media < 5:
    print(f"Reprovado, com a media {media}")
else:
    print(f"Ficou de recuperação, com a media {media}")