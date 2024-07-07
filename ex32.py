# Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes
# categorias:

idade = int(input("Informe sua idade:"))


if (idade >= 5 and idade <= 12):
    print("Nadador é da categoria infantil")
else:
    if (idade > 12 and idade <= 17):
        print("Nadador é da categoria Juvenil")
    else:
        if (idade >= 18):
            print("Nadador é da categoria Sênior")