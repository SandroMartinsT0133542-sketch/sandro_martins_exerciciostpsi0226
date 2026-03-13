
from utils import calc_operation, print_tabuada, print_client

""" Exercício 1: Crie um algoritmo que mostre os 30 primeiros números ímpares e pares. """
print("-------------------------------- Números pares e ímpares --------------------------------")
for i in range(1, 31):
  if i % 2 == 0:
    print(f"{i} é par")
  else:
    print(f"{i} é ímpar")

""" Exercício 2: Ler 10 números, e determinar se o número par e número impar. """
print("-------------------------------- Números pares e ímpares --------------------------------")
for i in range(1, 11):
  numero = int(input(f"Insira o número {i}: "))
  if numero % 2 == 0:
    print(f"{numero} é par")
  else:
    print(f"{numero} é ímpar")

""" Exercício 3: Ler a nota de 10 alunos, calcular a media e mostrar essa média. """
print("-------------------------------- Média de notas --------------------------------")
sum_notas = 0
for i in range(1, 11):
  nota = float(input(f"Insira a nota do aluno {i}: "))
  sum_notas += nota
media = sum_notas / 10
print(f"A média das notas é: {media}")


""" Exercício 4: Crie um algoritmo que leia um número inteiro, e diga se ele é um número primo ou não. """
print("-------------------------------- Número primo --------------------------------")
numero = int(input("Insira um número inteiro: "))
if numero > 1:
  for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
      print(f"{numero} não é um número primo.")
      break
  else:
    print(f"{numero} é um número primo.")

""" Exercício 5: Elabore um programa que escreve os primeiros 10.000 números inteiros no ecrã. """
print("-------------------------------- Números inteiros --------------------------------")
for i in range(1, 10001):
  print(i)



""" Exercício 6: Crie um algoritmo que mostre os 10 primeiros números primos. """
print("-------------------------------- Números primos --------------------------------")
contador = 0
numero = 2
while contador < 10:
  for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
      break
  else:
    print(numero)
    contador += 1
  numero += 1

""" Exercício 7: Faça um algoritmo que gere a seguinte série: 10, 20, 30, 40, ..... 980, 990, 1000. """
print("-------------------------------- Série de 10 em 10 --------------------------------")
for i in range(10, 1001, 10):
  print(i)



""" Exercício 8: Faça um algoritmo que gere a seguinte série: 10, 20, 30, 40, ..... 980, 990, 1000.e outro a fazer 15, 25, 35, 985, 995.(dois ciclos) """
print("-------------------------------- Série de 10 em 10 --------------------------------")
for i in range(10, 1001, 10):
  print(i)
print("-------------------------------- Série de 15 em 10 --------------------------------")
for j in range(15, 1000, 10):
  print(j)

""" Exercício 9: Escreva um programa que solicite um número ao utilizador até que o valor deste esteja entre os valores 1 e 100.(Use o ciclo do ... while) """
print("-------------------------------- Solicitar número entre 1 e 100 --------------------------------")
while True:
  numero = int(input("Insira um número"))
  if 1 <= numero <= 100:
    print(f"O número {numero}, que inseriu, está entre 1 e 100.")
    break
  else:
    numero = int(input("Insira um número"))

""" Exercício 10: Elabore um programa que lê um número e escreve quantos divisores ele possui. """
print("-------------------------------- Contar divisores --------------------------------")
numero = int(input("Insira um número inteiro: "))
divisores = 0
for i in range(1, numero + 1):
  if numero % i == 0:
    divisores += 1
print(f"O número {numero} possui {divisores} divisores.")


""" Exercício 11: Elabore um ciclo for para produzir o seguinte output.
	1
	22
	333
	4444
	55555
"""
print("-------------------------------- Output de números --------------------------------")
for i in range(1, 6):
  print(str(i) * i)
  

""" Exercício 12: Elabore um programa que leia quantos números quer que se efetue 
a soma, subtrações, divisões, multiplicações 
e no fim por meio de um acumulador diga quantas operações foram efetuadas. 
Exemplo introduzindo o número 60 o programa deve apresentar 
60 a somar, dividir multiplicar e subtrair por todos os números menores que ele. """

numeros = int(input("Quantos números quer que se efetue a soma, subtração, divisão e multiplicação? "))
soma = 0
subtracao = 0
divisao = 0
multiplicacao = 0

for i in range(1, numeros + 1):
  soma += numeros + i
  subtracao += numeros - i
  divisao += numeros / i
  multiplicacao += numeros * i

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Divisão: {divisao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Total de operações efetuadas: {numeros * 4}")


""" Exercício 13: Elabore um programa que leia um número e mostre a tabuada. (multiplicar de 1 a 10) """
print("-------------------------------- Tabuada --------------------------------")
numero = int(input("Insira um número para mostrar a tabuada: "))
print_tabuada(numero)


""" Exercício 14: Altere o programa anterior para que mostre todas as tabuadas de 1 a 100. (ciclos for). """
print("-------------------------------- Tabuada de 1 a 100 --------------------------------")
for j in range(1, 101):
    print_tabuada(j)
  

""" Exercícios 15: Elabore um programa que escreva no ecrã todas as linhas de código ASCII(0 a 255) e o código correspondente. Dispor de 20 em 20 com a condição de continuação ou saída do programa. """
print("-------------------------------- Código ASCII --------------------------------")
for i in range(0, 256, 20):
  for j in range(i, min(i + 20, 256)):
    print(f"{j}: {chr(j)}")
  resposta = input("Deseja continuar? (s/n): ").lower()
  if resposta != 's':
    break

""" Exercícios 16: Elabore um programa que constitua a média de 30 números pares que sejam introduzidos. Validando a entrada de números inteiros entre 1 e 50. """

print("-------------------------------- Média de números pares --------------------------------")
MIN_PAIR = 30
min, max, soma, pares, media  = 1, 50, 0, 0, 0

while pares < MIN_PAIR:
  numero = int(input(f"Insira um número {min} e {max}: "))
  while numero < min or numero > max:
    numero = int(input(f"Número inválido. Por favor, Insira um número entre {min} e {max}: "))
  if numero % 2 == 0:
    soma += numero
    pares += 1
  else:
    numero = int(input(f"Insira um número {min} e {max}: "))

media = soma / pares

print(f"A média dos números pares é: {round(media, 2)}")


""" Exercícios 17: Elabore um programa que determine os múltiplos de 5 mas não múltiplos de 3 …. De 1 a 1000 deve ser a sequência. """
print("-------------------------------- Múltiplos de 5 mas não múltiplos de 3 --------------------------------")
for i in range(1, 1001):
  if i % 5 == 0 and i % 3 != 0:
    print(i)


""" Exercícios 18: Elabore um programa que leia uma entrada e diga quantos números perfeitos existem. Exemplo de numero perfeito em que somando todos os divisores ele da o numero inicial.
6=3+2+1 . """

print("-------------------------------- Números perfeitos --------------------------------")
numero = int(input("Insira um número inteiro: "))
perfeitos = []
for i in range(1, numero + 1):
  soma_divisores = sum(j for j in range(1, i) if i % j == 0)
  if soma_divisores == i:
    perfeitos.append(i)
print(f"Números perfeitos até {numero}: {perfeitos}")



""" Exercícios 19:Escreva um programa que mostre os primeiros 60 números da serie bonatchi.
1, 1, 2, 3, 5, 8, 13, 21.
Como se constrói. 1+1=2    1+2=3        2+3=5 """
print("-------------------------------- Série de Fibonacci --------------------------------")
a, b = 1, 1
for _ in range(60):
  print(a)
  a, b = b, a + b


""" 
Teste Final: Elabore um programa que leia um valor de entrada e mostre para cada valor até ao 1 (se é número Primo, Quantos divisores e números perfeitos) 
o Programa deve validar entradas entre 1 e 30.000, e parar de 10 em 10 valores com instrução para parar ou continuar. 
No mesmo programa use um menu e Elabore uma calculadora simples (+,-,*,/) com a função extra tabuada. 
Validar entradas de 1 a 1000 (nota a tabuada deve apresentar todas as multiplicações de 1 ate ao máximo introduzido) deve parar de 20 em 20 valores. 
"""

print("-------------------------------- Programa de análise de números --------------------------------")
entrada = int(input("Insira um número inteiro entre 1 e 30000: "))
if 1 <= entrada <= 30000:
  for i in range(1, entrada + 1):
    if i > 1:
      for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
          break
      else:
        print(f"{i} é um número primo.")
    
    divisores = sum(1 for k in range(1, i + 1) if i % k == 0)
    print(f"{i} possui {divisores} divisores.")
    
    soma_divisores = sum(l for l in range(1, i) if i % l == 0)
    if soma_divisores == i:
      print(f"{i} é um número perfeito.")
    
    if i % 10 == 0:
      resposta = input("Deseja continuar? (s/n): ").lower()
      if resposta != 's':
        break

print("-------------------------------- Calculadora simples --------------------------------")
while True:
  print("1. Soma")
  print("2. Subtração")
  print("3. Multiplicação")
  print("4. Divisão")
  print("5. Tabuada")
  print("6. Sair")
  escolha = input("Escolha uma opção: ")

  match escolha:
    case"1":
      resultado = calc_operation("add")
      print(f"Resultado da soma: {resultado}")
    case"2":
      resultado = calc_operation("sub")
      print(f"Resultado da subtração: {resultado}")
    case"3":
      resultado = calc_operation("mult")
      print(f"Resultado da multiplicação: {resultado}")
    case"4":
      resultado = calc_operation("div")
      print(f"Resultado da divisão: {resultado}")
    case"5":
      max_num = int(input("Insira o número máximo para a tabuada (entre 1 e 1000): "))
      if 1 <= max_num <= 1000:
        for j in range(1, max_num + 1):
          print_tabuada(j)
          if j % 20 == 0:
            resposta = input("Deseja continuar? (s/n): ").lower()
            if resposta != 's':
              break
    case"6":
      print("A sair do programa.")
      break
    case _: print("Opção inválida. Por favor, tente novamente.")   


""" 
Teste Final: Elabore uma base de dados de clientes de uma fábrica de materiais. 
O programa deverá possibilitar inserção e listagem dos clientes bem como as compras por eles efetuadas( Númcli(Automático), NomCli, morada, tel, nif, compra, Divfin ). 
Divida final=compra – desconto, valor do desconto se compra for entre 100 e 200 é 5%, se for superior a 200 e inferior a 500 é 10% se superior a 500 é 15%. 
O programa deve validar todas as entradas e na listagem deve parar cliente a cliente e ser possível busca direta por número de cliente. 
"""

print("-------------------------------- Base de dados de clientes --------------------------------")

db = []
DESCONTO1 = 0.05
DESCONTO2 = 0.10
DESCONTO3 = 0.15

while True:
  print("1. Inserir cliente")
  print("2. Listar clientes")
  print("3. Procurar por nome de cliente")
  print("4. Sair")

  escolha = input("Escolha uma opção: ")

  if escolha == '1':
    name = input("Insira o nome do cliente: ")
    address = input("Insira a morada do cliente: ")
    tel = input("Insira o telefone do cliente: ")
    nif = input("Insira o NIF do cliente: ")
    purchase = float(input("Insira o valor da compra: "))
    
    if purchase < 100:
      discount = 0
    elif 100 <= purchase < 200:
      discount = purchase * DESCONTO1
    elif 200 <= purchase < 500:
      discount = purchase * DESCONTO2
    else:
      discount = purchase * DESCONTO3
    
    divfin = purchase - discount
    numcli = len(db) + 1
    client = {"id": numcli, "nome": name, "morada": address, "tel": tel, "nif": nif, "compra": purchase, "divfin": divfin}

    db.append(client)
  
  elif escolha == '2':
    for cliente in db:
      print_client(cliente)
  
  elif escolha == '3':
    numcli_busca = int(input("Insira o número do cliente para busca: "))
    for cliente in db:
      if cliente["id"] == numcli_busca:
        print_client(cliente)
        break
    else:
      print("Cliente não encontrado.")
  
  elif escolha == '4':
    print("A sair do programa.")
    break


