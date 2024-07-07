caixaA = int(input("Informe um inteiro: "))
caixaB = int(input("Informe um inteiro: "))
caixaC = int(input("Informe um inteiro: "))

if (caixaA and caixaB and caixaC >= 1 and caixaA and caixaB and caixaC <= 1000):
    if (caixaA < caixaB and caixaA + caixaB <= caixaC):
        print("1")
    else:
         if (caixaA < caixaB and caixaA + caixaB > caixaC):
             print("2")
         else:
              if (caixaA > caixaB and caixaA + caixaB > caixaC):
                  print("3")
              else:
                  if (caixaA > caixaB and caixaA + caixaB < caixaC):
                      print("3")