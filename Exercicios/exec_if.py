""" 
Exercício 1: Converter Segundos em Horas, Minutos e Segundos

Enunciado:
Desenvolva um programa que assuma uma entrada em segundos e a converta para horas, minutos e segundos.

Exemplo:
Entrada: 3665 segundos
Saída esperada: 1 hora, 1 minuto e 5 segundos.

"""
print("-------------------------------- Converter Segundos --------------------------------")

segundos = int(input("Digite o número de segundos: "))
horas = segundos // 3600
resto_segundos = segundos % 3600
minutos = resto_segundos // 60
segundos_restantes = resto_segundos % 60

if(horas > 24):
  dias = horas // 24
  horas = horas % 24

  if(dias > 365):
    anos = dias // 365
    dias = dias % 365
    print(f"{anos} anos, {dias} dias, {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")
  else:
    print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")
else:
  print(f"{horas} horas, {minutos} minutos e {segundos_restantes} segundos.")




""" 
Exercício 2: Encontrar o Maior e o Menor Valor entre 3 Números

Enunciado: Desenvolva um programa que analise 3 valores inteiros e informe qual o maior e qual o menor deles.

Exemplo:
Entrada: num1 = 5, num2 = 2, num3 = 8
Saída esperada:
Maior: 8
Menor: 2 

"""

print("-------------------------------- Encontrar o Maior e o Menor --------------------------------")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if(num1 >= num2 and num1>= num3):
  maior = num1
elif(num2 >= num1 and num2 >= num3):
  maior = num2
else:  maior = num3

if(num1 <= num2 and num1 <= num3):
  menor = num1
elif(num2 <= num1 and num2 <= num3):
  menor = num2
else:  menor = num3

print(f"Maior: {maior}")
print(f"Menor: {menor}")


""" 
Exercício 3: Mostrar Números em Ordem Crescente e Decrescente

Enunciado: 
Crie 2 variáveis (num1 e num2) e leia o valor para cada uma delas. 
Mostre os valores de forma crescente e decrescente.

Exemplo:
Entrada: num1 = 7, num2 = 2
Saída esperada:
Crescente: 2, 7
Decrescente: 7, 2
"""

print("-------------------------------- Mostrar Números em Ordem Crescente e Decrescente --------------------------------")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if(num1 <= num2):
  print(f"Crescente: {num1}, {num2}")
  print(f"Decrescente: {num2}, {num1}")
else:
  print(f"Crescente: {num2}, {num1}")
  print(f"Decrescente: {num1}, {num2}")

""" 
Exercício 4: Verificar se o Cheque Pode Ser Descontado

Enunciado:
Desenvolva um Programa que leia o saldo inicial de um cliente de banco e leia também o valor de um cheque. 
Analise se o cheque pode ser descontado. 
Se o cheque não puder ser descontado, mostre essa informação, caso contrário, desconte o cheque e informe o saldo atualizado.

Exemplo:
Entrada: Saldo = 500, Cheque = 300
Saída esperada:
Cheque descontado, saldo: 200 """

saldo = float(input("Digite o saldo inicial: "))
cheque = float(input("Digite o valor do cheque: "))

if cheque > saldo:
  print("Cheque não pode ser descontado, saldo insuficiente.")
else:
  saldo -= cheque
  print(f"Cheque descontado, saldo atualizado: {saldo:.2f}")



""" 
Exercício 5: Ler 3 Valores e Exibir em Ordem Crescente e Decrescente
Enunciado:
Ler 3 valores inteiros e apresentar os valores dispostos em ordem crescente e decrescente.

Exemplo:
Entrada: num1 = 4, num2 = 9, num3 = 2
Saída esperada:
Crescente: 2, 4, 9
Decrescente: 9, 4, 2
"""

print("-------------------------------- Ler 3 Valores e Exibir em Ordem Crescente e Decrescente --------------------------------")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if(num1 <= num2 and num1 <= num3):
  menor = num1
  if(num2 <= num3):
    meio = num2
    maior = num3
  else:
    meio = num3
    maior = num2
elif(num2 <= num1 and num2 <= num3):
  menor = num2
  if(num1 <= num3):
    meio = num1
    maior = num3
  else:
    meio = num3
    maior = num1
else:
  menor = num3
  if(num1 <= num2):
    meio = num1
    maior = num2
  else:
    meio = num2
    maior = num1

print(f"Crescente: {menor}, {meio}, {maior}")
print(f"Decrescente: {maior}, {meio}, {menor}")



""" 
Exercício 6: Desconto de Compra

Enunciado:
Uma loja oferece descontos de acordo com o valor da compra:
10% para compras até 200,00€.
15% para compras entre 200,01€ e 500,00€.
20% para compras acima de 500,00€.
Desenvolva um Programa que leia o nome do cliente e o valor da compra e mostre o valor do desconto e o valor total a pagar.

Exemplo:
Entrada: Cliente: João, Compra: 350
Saída esperada:
Nome: João
Compra: 350,00€
Desconto: 52,50€
Total a pagar: 297,50€
"""

print("-------------------------------- Desconto de Compra --------------------------------")

nome = input("Digite o nome do cliente: ")
compra = float(input("Digite o valor da compra: "))

if compra <= 200:
  desconto = compra * 0.10
elif compra <= 500:
  desconto = compra * 0.15  
else:  desconto = compra * 0.20
total_a_pagar = compra - desconto

print(f"Nome: {nome}")
print(f"Compra: {compra:.2f}€")
print(f"Desconto: {desconto:.2f}€")
print(f"Total a pagar: {total_a_pagar:.2f}€")

""" 
Exercício 7: Calcular a Média de Notas com Pesos

Enunciado:
O sistema de avaliação de uma disciplina tem três provas com pesos diferentes. 
A primeira tem peso 2, a segunda tem peso 3, e a terceira tem peso 5. Crie
um programa para calcular a média final de um aluno e mostrar se ele está APROVADO (nota >= 6) ou REPROVADO (nota < 6).

Exemplo:
Entrada: Nota1 = 7, Nota2 = 6, Nota3 = 9
Saída esperada:
Média: 7.4
Aprovado 
"""

print("-------------------------------- Calcular a Média de Notas com Pesos --------------------------------")

nota1 = float(input("Digite a nota da primeira prova (peso 2): "))
nota2 = float(input("Digite a nota da segunda prova (peso 3): "))
nota3 = float(input("Digite a nota da terceira prova (peso 5): "))
media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

print(f"Média: {media:.1f}")

if media >= 6:
  print("Aprovado")
else: print("Reprovado")



""" 
Exercício 8: Calcular a Média de 10 Notas e informar notas iguais ou acima da media 
Enunciado:
Crie um programa que leia a nota de 10 alunos (notas de 0 a 20), calcule a média das notas e mostre a média. 
Além disso, informe quantos alunos ficaram com a nota igual ou acima da média. 
"""

print("-------------------------------- Calcular a Média de 10 Notas e informar notas iguais ou acima da media --------------------------------")

notas = []
for i in range(10):
  nota = float(input(f"Digite a nota do aluno {i+1} (0 a 20): "))
  while nota < 0 or nota > 20:
    print("Nota inválida. Digite uma nota entre 0 e 20.")
    nota = float(input(f"Digite a nota do aluno {i+1} (0 a 20): "))
  notas.append(nota)
media = sum(notas) / len(notas)
print(f"Média: {media:.1f}")
contador = 0
for nota in notas:
  if nota >= media:
    contador += 1
print(f"Alunos com nota igual ou acima da média: {contador}")


""" 
Exercício Switch: Exibir Nome do Mês

Enunciado:
Leia um número inteiro de 1 a 12 e mostre o nome do mês correspondente. Caso o número não seja válido, mostre uma mensagem de erro.

Exemplo:
Entrada: 5
Saída esperada: Maio 

"""

print("-------------------------------- Exibir Nome do Mês --------------------------------")
mes_numero = int(input("Digite um número de 1 a 12 para o mês: "))

match mes_numero:
  case 1:
    print("Janeiro")
  case 2:
    print("Fevereiro")
  case 3:
    print("Março")
  case 4:
    print("Abril")
  case 5:
    print("Maio")
  case 6:
    print("Junho")
  case 7:
    print("Julho")
  case 8:
    print("Agosto")
  case 9:
    print("Setembro")
  case 10:
    print("Outubro")
  case 11:
    print("Novembro")
  case 12:
    print("Dezembro")
  case _:
    print("Número inválido. Digite um número entre 1 e 12.")


""" 
Exercício Loop: Identificar Números Pares e Ímpares
Enunciado:
Leia 10 números e determine quantos são pares e quantos são ímpares.

Exemplo:
Entrada: 2, 3, 5, 6, 8, 9, 10, 12, 14, 15
Saída esperada:
Pares: 6
Ímpares: 4

"""

print("-------------------------------- Identificar Números Pares e Ímpares --------------------------------")

pares = 0
impares = 0

for i in range(10):
  numero = int(input(f"Digite o número {i+1}: "))
  if numero % 2 == 0:
    pares += 1
  else:
    impares += 1

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")