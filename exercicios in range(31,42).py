# Desafio 31:         
distancia = float(input('Digite a distancia da sua viagemem km: '))
if distancia <= 200:
    print('O valor da viagem sera de {:.2f}.'.format(distancia*0.50))
else:
    print('O valor da viagem sera de R${:.2f}.'.format(distancia*0.45))

# Desafio 32: 
ano = int(input('Digite o ano que deseja analisar: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto.'.format(ano))
else:
    print('O ano {} não é Bissexto.'.format(ano))

# Desafio 33:         
a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
c = float(input('Terceiro valor: '))
if a<b and a<c:
    menor = a
    if b<c:
        maior = c
    else:
        maior = b
if b<a and b<c:
    menor = b        
    if a<c:
        maior = c
    else:
        maior = a
if c<a and c<b:
    menor = c
    if a<b:
        maior = b
    else:
        maior = a     
print('O menor valor é {}.'.format(menor))
print('O maior valor é {}.'.format(maior))

# Desafio 34: 
salario_atual = float(input('Digite o seu salário atual: '))
if salario_atual <= 1250:
    print('Seu novo salário sera de R${:.2f}'.format(salario_atual*1.15))
else:
    print('Seu novo salário sera de R${:.2f}'.format(salario_atual*1.10))

# Desafio 35:
print('-='*20)
print('Analisador de Triangulos')
print('-='*20)
aresta1 = float(input('tamanho da primeira aresta: '))   
aresta2 = float(input('tamanho da segunda aresta: '))
aresta3 = float(input('tamanho da terceira aresta: '))
if aresta1+aresta2>aresta3 and aresta2+aresta3>aresta1 and aresta1+aresta3>aresta2:
    print('Os segmentos acima podem formar um triangulo!')
else:
    print('Os segmentos acima não podem formar um triangulo!')       

# Desafio 36:
valor_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salario? R$'))
anos = int(input('Em quantos anos pretende pagar? '))
valor_parcela = valor_casa/(anos*12)
valor_possivel = 0.30*salario
if valor_parcela > valor_possivel:
    print('Lamento, porem voce nao podera conseguir seu financeamento.')
else:
    print('O financeamento aceito e a parcela mensal sera de R${}'.format(valor_parcela))

# Desafio 37:
numero = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversao:
[ 1 ] converter para binario
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opçao = int(input('Escolha a opçao que deseja: '))
if opçao == 1:
    print('O numero {} convertido para binario é igual a {}'.format(numero, bin(numero)))
elif opçao == 2:
    print('O numero {} convertido para octal é igual a {}'.format(numero, oct(numero)))
elif opçao == 3:
    print('O numero {} convertido para hexadecimal é igual a {}'.format(numero, hex(numero)))
else:
    print('Opçao invalida.')    

# Desafio 38:
primeiro = int(input('digite um numero: '))
segundo = int(input('Digite outro numero: '))
if primeiro > segundo:
    print('Primeiro é maior')
elif segundo > primeiro:
    print('Segundo é maior')
else:
    print('Os dois sao iguais')

# Desafio 39:
ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = 2022
print('Quem nasceu em {} tem {} anos em {}'.format(ano_nascimento, ano_atual-ano_nascimento, ano_atual))
if ano_atual-ano_nascimento > 18:
    print('Você ja passou pelo processo de alostamento militar.')
elif ano_atual-ano_nascimento == 18:
    print('Seu alistamento militar sera esse ano.')
else:
    print('Ainda faltam {} anos para seu alistamento militar. Seu alistamento sera em {}'.format((ano_nascimento + 18)-ano_atual,ano_nascimento + 18))    

# Desafio 40:
primeira = float(input('Primeira nota: '))
segunda = float(input('Segunda nota: '))
media = (primeira + segunda)/2
if media<5:
    print('Como o aluno obteve a media {}, que é abaixo do esperado, entao ele esta REPROVADO!!'.format(media))
if media >= 5 and media <= 6.9:
    print('Como o aluno obteve a media {}, ele esta de recuperacao',format(media))
if media >= 7.0:
    print('PARABENS!! O aluno foi aprovado com a media {}'.format(media))

# Desafio 41:
anoatual = 2022
nascimento = int(input('Digite seu ano de nascimento: '))
idade = anoatual - nascimento
if idade <= 9:
    print('Sua categoria é mirim.')
if idade <= 14:
    print('Sua categoria é infantil.')
if idade <= 19:
    print('Sua categoria é junior.') 
if idade <= 25:
    print('Sua categoria é senior.')
if idade > 25:
    print('Sua categoria é master.')  

# Desafio 42:
print('-='*20)
print('Analisador de Triangulos')
print('-='*20)
aresta1 = float(input('tamanho da primeira aresta: '))   
aresta2 = float(input('tamanho da segunda aresta: '))
aresta3 = float(input('tamanho da terceira aresta: '))
if aresta1+aresta2>aresta3 and aresta2+aresta3>aresta1 and aresta1+aresta3>aresta2:
    print('Os segmentos acima podem formar um triangulo!')
    if aresta1 == aresta2 == aresta3:
        print('Esse trinagulo é equlatero')
    elif aresta1 == aresta2 or aresta1 == aresta3 or aresta2 == aresta3:
        print('Esse trinagulo é isosceles') 
    else:
        print('Esse triangulo é escaleno')      
else:
    print('Os segmentos acima não podem formar um triangulo!') 

# Desafio 43:




