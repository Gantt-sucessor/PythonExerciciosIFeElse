# A nota final de um estudante e calculada a partir de três notas atribuídas entre o intervalo de 0
# até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame
# final. A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de
# Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela
# se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 5,9) ou se foi
# aprovado. Crie todas as verificações necessárias.

nota_laboratorio = float(input("Informe sua nota do trabalho do laboratório:"))
avaliacao_semestral = float(input("Informe a nota da sua avaliação semestral:"))
exame_final = float(input("Informe a nota do seu exame final:"))

peso_laboratorio = 2
peso_avaliacao = 3
peso_final = 5

media = (nota_laboratorio * peso_laboratorio + avaliacao_semestral * peso_avaliacao + exame_final * peso_final)/10

if(media > 0 and media <= 2.9):
    print("Aluno reprovado:")
else:
    if (media >=3 and media <= 5.9):
        print("Aluno de recuperação")
    else:
        print("Aluno foi aprovado")