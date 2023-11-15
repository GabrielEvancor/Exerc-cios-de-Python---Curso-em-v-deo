# Desafio 43:
from time import sleep
from random import randint
peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso/(altura**2)
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade morbida')

# Desafio 44:
print('############### LOJAS EVANGELISTA ####################')
preço = float(input('Qual foi o preço das compras? R$ '))
print('''FORMAS DE PAGAMENTO:
[1] A VISTA DINHEIRO/CHEQUE 
[2] A VISTA CARTAO
[3] 2X NO CARTAO
[4] 3X OU MAIS NO CARTAO''')
opçao = int(input('Qual é a opçao? '))
if opçao == 1:
    total = 0.9*preço
elif opçao == 2:
    total = 0.95*preço
elif opçao == 3:
    total = preço
    parcela = total/2
    print('Sua compra sera parcelada em 2x de R${:.2f}.'.format(parcela))
else:
    total = preço*1.2
    nparcelas = int(input('Qual sera o numero de parcelas? '))
    parcela = total/nparcelas
    print('Sua compra sera parcelada em {} vezes de {:.2f}.'.format(nparcelas, parcela))
print('Sua compra de {} vai custar {} no final.'.format(preço, total))

# Desafio 45:
print('''Suas opçoes:
[1] Pedra
[2] Papel
[3] Tesoura''')
jogador = int(input('Qual a sua opçao? '))
print('''JO
KEN
PO!!!!''')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('-='*12)
print('O computador jogou {}.'.format(itens[computador]))
print('O jogador jogou {}.'.format(itens[jogador-1]))
print('-='*12)
if computador == 0:
    if jogador-1 == 0:
        print('Empate')
    elif jogador-1 == 1:
        print('Jogador ganhou!!!')
    elif jogador-1 == 2:
        print('Computador ganhou!!!')
    else:
        print('Jogada invalida!!!')
elif computador == 1:
    if jogador-1 == 0:
        print('Computador ganhou!!!')
    elif jogador-1 == 1:
        print('Empate')
    elif jogador-1 == 2:
        print('Jogador ganhou!!!')
    else:
        print('Jogada invalida!!!')
elif computador == 2:
    if jogador-1 == 0:
        print('Jogador ganhou!!!')
    elif jogador-1 == 1:
        print('Computador ganhou!!!')
    elif jogador-1 == 2:
        print('Empate')
    else:
        print('Jogada invalida!!!')


# Desafio 46:
n = int(input('Digite um numero para contagem regressiva: '))
for i in range(n+1):
    print(n)
    n = n - 1
    sleep(1)
print('BUM!')

# Desafio 47:
n = int(input('Digite um numero: '))
lista = []
# colocar de 2 em 2 ira diminuir em duas vezes o tempo gasto pelo processador
for i in range(0, n+1, 2):
    if i % 2 == 0:
        print(i)
        lista.append(i)
print('No intervalo de 0 ate {}, existem {} numeros pares'.format(n, len(lista)))

# Desafio 48:
n = int(input('Digite um numero: '))
soma = 0
for i in range(n+1):
    if i % 3 == 0:
        soma = soma + i
print(soma)

# Desafio 49
numero_desejado = int(print("Digite um numero para ver sua tabuada: "))
for i in range(11):
    print("{} X {} = {}".format(numero_desejado, i, numero_desejado*i))

# Desafio 50
numero_analisado = int(input("Digite um numero"))
soma_pares = 0
for i in range(numero_analisado+1):
    if numero_analisado % 2 == 0:
        soma_pares = soma_pares + i
    else:
        soma_pares = soma_pares

# Desafio 51
termoInicial = int(input("Digite o termo inicial da sua PA: "))
razaoDaPA = int(input("Digite a razao da sua PA: "))
termoFinal = int(input("Digite o termo final da sua PA: "))
for i in range (termoInicial, termoFinal, razaoDaPA):
    print("{}".format(i), end="-->")
print("ACABOU!!!!")    

# Desafio 52
Numero = int(input("Digite um numero: "))
numero_de_divisoes = int(input())
for i in range (2, Numero):
    if (Numero%i) != 0:
        numero_de_divisoes = numero_de_divisoes + 1
if numero_de_divisoes == 0:
    print("O numero escolhido eh primo!!")
if numero_de_divisoes != 0:
    print("O numero nao eh primo pois ele foi dividido {} vezes".format(numero_de_divisoes))    

Numero = int(input("Digite um numero: "))
numero_de_divisoes = 0
for i in range (1, Numero+1):
    if (Numero%i) == 0:
        print('\33[34m', end='')
        numero_de_divisoes += 1
    else:
        print('\31[m', end='')
    print("{} ".format(i), end='')
print('O numero {} foi divisivel {} vezes'.format(Numero, numero_de_divisoes))   
if numero_de_divisoes == 2:
    print("Por isso, o numero escolhido eh primo")
else:
    print("Por isso, o numero escolhido nao eh primo")       
