# Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triangulo, se
# forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
# • O comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados.
# • Chama-se equilátero o triângulo que tem três lados iguais.
# • Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
# • Recebe o nome de escaleno o triângulo que tem os três lados diferentes

ladoA = int(input("Informe o primeiro lado do triângulo:"))
ladoB = int(input("Informe o segundo lado do triângulo:"))
ladoC = int(input("Informe o terceiro lado do triângulo:"))

if (ladoA > (ladoB + ladoC) and ladoB > (ladoA + ladoC) and ladoC > (ladoA + ladoB)):
    print("Essas medidas podem ser valores de triângulo!")
else:
    if (ladoA == ladoB == ladoC):
        print("O triângulo é equlátero")
    else:
        if (ladoA == ladoB or ladoB == ladoC or ladoA == ladoC):
            print("O triângulo é isósceles")
        else:
             if (ladoA != ladoB and ladoB != ladoC and ladoA != ladoC):
                 print("O triângulo é escaleno")
        

                