# Desafio 01:
nome = input('Qual é o seu nome?')
print('Olá', nome, '!', 'Prazer em te conhecer!')

# Desafio 02:
dia = input('Qual dia você nasceu?')
mês = input('Qual mês você nasceu?')
ano = input('Qual ano você nasceu?')
print('Você nasceu no dia', dia, 'de', mês, 'de', ano, '.', 'Correto?')

# Desafio 03:
N1 = int(input('Digite um numero '))
N2 = int(input('Digite outro numero '))
S = N1 + N2
print('A soma entre {} e {} vale {}'.format(N1, N2, S))

# Desafio 05:
numero_meio = int(input('Digite um numero '))
antecessor = numero_meio - 1
sucessor = numero_meio + 1
print('O antecessor de {} é {} e seu sucessor é {}'.format(
    numero_meio, antecessor, sucessor))

# Desafio 06:
numero = int(input('digite um numero: '))
dobro = numero*2
triplo = numero*3
squared = numero**1/2
print('O dobro, triplo e raiz quadrada de {} é,respectivamente, {}, {}, {}'.format(
    numero, dobro, triplo, squared))

# Desafio 07:
nota1 = int(input('Digite sua primeira nota: '))
nota2 = int(input('Digite sua segunda nota: '))
média = (nota1 + nota2)/2
print('Sua média é: ', média)

# Desafio 08:
Metros = int(input('Digite um valor em metros '))
centimetros = Metros * 10**2
milimetros = Metros * 10**3
print('{} metros em centrimetros é {}'.format(Metros, centimetros))
print('{} metros em milimetros é {}'.format(Metros, milimetros))

# Desafio 09:
numero = int(input('Dgite um numero: '))
for i in range(11):
    numero2 = numero*i
    print(i, "vezes", numero, "é igual a", numero*i)

# Desafio 10:
carteira_atual = int(input('Digite o valor atual em reais da sua carteira: '))
dolar = 5.46
print('Voce pode comprar {:.3f} dolares com o saldo atual da sua carteira'.format(
    carteira_atual/dolar))

# Desafio 11:
largura = int(input('Digite a largura da parede: '))
altura = int(input('Digite a altura da parede: '))
Área = largura*altura
print('A area da parede em questao é de {} metros, e a quantidade de tinta necessaria sera de {:.2f} litros'.format(Área, Área/2))

# Desafio 12:
preço_atual = int(input('Digite o preço atual do produto: '))
preço_futuro = preço_atual*0.95
print('O novo preço com 5 porcento de desconto sera de', preço_futuro)

# Desafio 13:
salario_atual = int(input('especifique seu salario atual: '))
reajuste = 1.15*salario_atual
print('Apos aumento de 15 porcento no seu salario de {}, seu novo salario sera de {}'.format(
    salario_atual, reajuste))

# Desafio 14:
celsius = float(input('Informe a temperatura em Celsius: '))
fahrenait = ((9*celsius)/5)+32
print("A temperatura de {}ºC em fahrenait sera de {}ºF".format(celsius, fahrenait))

# Desafio 15:
km_percorridos = float(input('Digite quantos km rodados o carro teve: '))
dias_alugados = int(input('Digite quantos dias voce alugou esse carro: '))
Preço_total = (60*dias_alugados) + (0.15*km_percorridos)
print('O total a ser pago no aluguel sera: {:.2f}'.format(Preço_total))
