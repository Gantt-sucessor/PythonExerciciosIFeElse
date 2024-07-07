imc = float(input("Informe seu imc:"))

if (imc < 18.5):
    print("Abaixo do peso")
else:
    if (imc >= 18.6 and imc <= 24.9):
        print("Saudável")
    else:
        if (imc >= 25 and imc <= 29.9):
            print("Peso em excesso")
        else:
            if (imc >= 30 and imc <= 34.9):
                print("Obesidade Grau 1")
            else:
                if (imc >= 35 and imc <= 39.9):
                    print("Peso em grau 2 (severa)")
                else:
                    if (imc >= 40):
                        print("Obesidade em grau 3 (mórbida)")