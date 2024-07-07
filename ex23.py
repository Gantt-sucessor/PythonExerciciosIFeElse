# Escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este
# número. Isto e, janeiro se é 1, fevereiro é 2, e assim por diante.

mes = int (input("Informe um número de 1 a 12:"))

if (mes == 1):
    print("O mês se refere a janeiro!")
else:
    if (mes == 2):
        print("O mês se refere a fevereiro!")
    else:
        if (mes == 3):
            print("O mês se refere a março")
        else:
            if (mes == 4):
                print("O mês se refere a abril")
            else:
                if (mes == 5):
                    print("O mês se refere a maio")
                else:
                    if (mes == 6):
                        print("O mês se refera a junho")
                    else:
                        if (mes == 7):
                            print("O mês se refera a julho")
                        else:
                            if (mes == 8):
                                print ("O mês se refere a agosto")
                            else: 
                                if (mes == 9):
                                    print("O mês se refere a setembro")
                                else:
                                    if (mes == 10):
                                        print("O mês se refere a outubro")
                                    else: 
                                        if (mes == 11):
                                            print("O mês se refera a novembbro")
                                        else: 
                                            if (mes == 12):
                                                print("O mês se refera a dezembro")
                                            else: 
                                                print("Mês não correspondente")