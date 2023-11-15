# Desafio 16:
from cmath import asin
from math import trunc
numero = float(input('Digite umnumero real: '))
truncado = trunc(numero)
print('A porçao inteira do numero {} é {}'.format(numero, truncado))

# Desafio 17:
c_oposto = float(input('Tamanho c_oposto: '))
c_adj = float(input('Tamanho c_adj: '))
print('A hipotenusa desse triangulo retangulo será {}'.format(((c_oposto**2) + (c_adj**2))**(1/2)))

# Desafio 18:
from math import sin, cos, tan, radians
angulo = float(input('Digite o valor de um angulo em graus: '))
sen = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))
print('O seno, cosseno e tangente de {:.2f} graus é ,respectivamente, {:.2f}, {:.2f}, {:.2f}'.format(angulo, sen, coss, tang))

# Desafio 19:
import random
nome1 = input('Nome do primeiro aluno: ')
nome2 = input('Nome do segundo aluno: ')
nome3 = input('Nome do terceiro aluno: ')
nome4 = input('Nome do quarto aluno: ')
lista = [nome1,nome2,nome3,nome4]
sorteado = random.choice(lista)
print('O aluno sorteado foi {}'.format(sorteado))

# Desafio 20:
import random
nome1 = input('Nome do primeiro aluno: ')
nome2 = input('Nome do segundo aluno: ')
nome3 = input('Nome do terceiro aluno: ')
nome4 = input('Nome do quarto aluno: ')
lista = [nome1,nome2,nome3,nome4]
random.shuffle(lista)
print('A nova ordem sera {}'.format(lista))

# Desafio 22:
nome  = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiusculas é ', nome.upper())
print('Seu nome em minusculas é ', nome.lower())
print('Seu nome ao todo possui {} letras'.format(len(nome) - nome.count(' ')))
dividindo = nome.split()
primeiro_nome = dividindo[0]
print('Seu primeiro nome é {}, e ele possui {} letras.'.format(primeiro_nome, len(primeiro_nome)))

# Desafio 23:
numero = int(input('Digite um numero: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('unidade: ',unidade)
print('dezena: ',dezena)
print('centena: ',centena)
print('milhar: ', milhar)

# Desafio 24:
city = str(input('Em qual cidade você nasceu? ')).strip()
city_capitalized = city.capitalize()
print(city[:5] == 'Santo')

# Desafio 25:
nome = str(input('Digite o seu nome: ')).strip()
nome_titled = nome.title()
print('Seu nome tem Silva? {}'.format('Silva' in nome_titled))

# Desafio 26:
frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes na frase'.format(frase.lower().count('a')))
print('A primeira letra A aparece na posiçao {}'.format(frase.lower().find('a')+1 ))
print('A ultima letra A aparece na posiçao {}'.format(frase.lower().rfind('a')+1))

# Desafio 27:
nome = str(input('Digite seu nome: ')).strip()
print('Muito prazer em te conhecer {}!'.format(nome))
nome = nome.split()
print('Seu primeiro nome é {}.'.format(nome[0]))
numero_de_nomes = len(nome)
print('Seu ultimo nome é {}.'.format(nome[len(nome)-1]))

# Desafio 28:
from random import randint
numero = int(input('Tente adivinhar o numero que irei sortear de 0 a 5 e digite-o aqui: '))
computador = randint(0,5)
if computador == numero:
    print('VOCE GANHOU!!!')
else:
    print('VOCE PERDEU')

# Desafio 29:
velocidade = float(input('Digite sua velocidade atual em km/h: '))
if velocidade >= 80:
    preço = (velocidade - 80)*7
    print('Atencao!! Voce ultrapassou o limite de velocidade e ira pagar uma multa de {} reais.'.format(preço))
else:
    print('Tenha um bom dia, dirija com segurança!!')

# Desafio 30:
numero = int(input('Digite um numero inteiro: '))
if numero%2 == 0:
    print('O numero {} é par'.format(numero))
else:
     print('O numero {} é impar'.format(numero))
