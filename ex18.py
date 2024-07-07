# Crie um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
# utilizando as seguintes formulas (onde h corresponde à altura):
# • Homens: (72.7∗ h)−58
# • Mulheres: (62,1∗ h)−44,7

altura = float(input("Informe sua altura:"))
sexo = str(input("Informe seu sexo:"))
peso_homem = (72 * altura) - 58
peso_mulher = (62.1 * altura) - 44.7

if (sexo == "Homem"):
    print("O peso ideal para ele é:",peso_homem)
else:
    if (sexo == "Mulher"):
        print("O pesso ideal para ela é:",peso_mulher)
