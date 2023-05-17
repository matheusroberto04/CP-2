#MATHEUS ROBERO - 98581
#LUCAS ANTUNES -551670
print("Bem vindo a calculadora Python!")
# Introduzindo variaveis
n = int(input('''Selecione a operação desejada
[1] -> Adição
[2] -> Subtração
[3] -> Divisão
[4] -> Multiplicação 
 '''))
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

#Seleção de operação
match n:
    case 1:
        adição = n1 + n2
        print('Adição: ',adição)
    case 2:
        subtração = n1 - n2
        print('Subtração: ',subtração)
    case 3:
        divisão = n1/n2
        print('Divisão: ',divisão)
    case 4:
        multiplicação = n1*n2
        print('Multiplicação: ',multiplicação)
    case _: 
        print('Nenhuma opção!')
maior = 0
menor = 0
if n1>0:
    maior = n1
    print("Maior: ", maior)
elif n1<0:
    menor = n1
    print("Menor: ", menor)
if n2>0:
    maior = n2 
    print("Maior: ", maior)
elif n2<0:
    menor = n2    
    print("Menor: ", menor)

# Professor queria fazer uma observação, de que no fim do programa esta descrito o Maior e Menos numero, porem por algum motivo ele aparece duas vezes a palavra Maior!