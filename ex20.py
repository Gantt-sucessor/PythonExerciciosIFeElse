# Crie um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda
# prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno
# foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos.

n1 = float(input("Informe a primeira nota:"))
n2 = float(input("Informe a segunda nota:"))
n3 = float(input("Informe a terceira nota:"))
prova1 = 1
prova2 = 1
prova3= 2
media = (n1 * prova1 + n2 * prova2 + n3 * prova3)/4
print(media)

if (media >= 6):
    print("Parabéns, você passou!!")
else:
    if (media < 6):
        print("Infelizmente você não passou!")