# Seu João precisa fazer um empréstimo automático no aplicativo, o banco aprova a transação de
# acordo com as seguintes condições: Leia o salário de um trabalhador e o valor da prestação de
# um empréstimo. Se a prestação for maior que 20% do salário imprima: Empréstimo não
# concedido, caso contrário imprima: Empréstimo concedido.

salario = float(input("Informe seu salário:"))
valor_emprestimo = float(input("Informe o valor da prestação:"))
emprestimo_pos = salario*0.20
print(emprestimo_pos)

if (valor_emprestimo > emprestimo_pos):
    print("Empréstimo não concedido!")
else:
    print("Empréstimo concedido!")
