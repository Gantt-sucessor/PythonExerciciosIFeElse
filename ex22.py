# Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente
# a este número. Isto é, domingo equivale a 1, segunda-feira se 2, e assim por diante.

dia = int(input("Informe um número de 1 a 7:"))

if (dia == 1):
    print("Dia se refere a domingo!")
else:
    if (dia == 2):
        print("Dia se refere a segunda-feira!")
    else:
        if (dia == 3):
            print("Dia se refere a terça-feira!")
        else:
            if (dia == 4):
                print("Dia se refere a quarta-feira!")
            else:
                if (dia == 5):
                    print("Dia se refere a quinta-feira!")
                else:
                    if (dia == 6):
                        print("Dia se refere a sexta-feira!")
                    else:
                        if (dia == 7):
                            print("Dia se refere a sábado!")
                        else:
                            print("Dia não existe!")
