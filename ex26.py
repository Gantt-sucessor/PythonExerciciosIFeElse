# Determine se um determinado ano lido é bissexto. Sendo que um ano e bissexto se for divisível
# por 400 ou se for divisível por 4 e não for divisível por 100. Por exemplo: 1988, 1992, 1996.

ano = int(input("Informe o ano:"))
bissexto = ano%4

if(bissexto == 0):
    print("Esse ano é um ano bissexto!!")
else:
    print("Esse ano não é um ano bissexto!!")
    


