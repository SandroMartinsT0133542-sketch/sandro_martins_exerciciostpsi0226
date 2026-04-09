try:
  from .utils import calc_operation, print_tabuada, print_client
except ImportError:
  from utils import calc_operation, print_tabuada, print_client

try:
  from .output_constants import *
except ImportError:
  from Exercicios.output_constants import *


# Exercicio 1: Crie um algoritmo que mostre os 30 primeiros numeros impares e pares.
def exec1():
  print(HEADER_EVEN_ODD)
  for i in range(1, 31):
    if i % 2 == 0:
      print(f"{i} e par")
    else:
      print(f"{i} e impar")


# Exercicio 2: Ler 10 numeros, e determinar se o numero par e numero impar.
def exec2():
  print(HEADER_EVEN_ODD)
  for i in range(1, 11):
    numero = int(input(f"Insira o numero {i}: "))
    if numero % 2 == 0:
      print(f"{numero} e par")
    else:
      print(f"{numero} e impar")


# Exercicio 3: Ler a nota de 10 alunos, calcular a media e mostrar essa media.
def exec3():
  print(HEADER_AVERAGE_GRADES)
  sum_notas = 0
  for i in range(1, 11):
    nota = float(input(f"Insira a nota do aluno {i}: "))
    sum_notas += nota
  media = sum_notas / 10
  print(f"A media das notas e: {media}")


# Exercicio 4: Crie um algoritmo que leia um numero inteiro, e diga se ele e primo ou nao.
def exec4():
  print(HEADER_PRIME_NUMBER)
  numero = int(input("Insira um numero inteiro: "))
  if numero > 1:
    for i in range(2, int(numero ** 0.5) + 1):
      if numero % i == 0:
        print(f"{numero} nao e um numero primo.")
        break
    else:
      print(f"{numero} e um numero primo.")


# Exercicio 5: Elabore um programa que escreve os primeiros 10.000 numeros inteiros no ecra.
def exec5():
  print(HEADER_INTEGERS)
  for i in range(1, 10001):
    print(i)


# Exercicio 6: Crie um algoritmo que mostre os 10 primeiros numeros primos.
def exec6():
  print(HEADER_PRIME_NUMBERS)
  contador = 0
  numero = 2
  while contador < 10:
    for i in range(2, int(numero ** 0.5) + 1):
      if numero % i == 0:
        break
    else:
      print(numero)
      contador += 1
    numero += 1


# Exercicio 7: Faca um algoritmo que gere a serie: 10, 20, ... 1000.
def exec7():
  print(HEADER_SERIES_TENS)
  for i in range(10, 1001, 10):
    print(i)


# Exercicio 8: Gera a serie 10..1000 e a serie 15..995 (passo 10).
def exec8():
  print(HEADER_SERIES_TENS)
  for i in range(10, 1001, 10):
    print(i)
  print(HEADER_SERIES_FIFTEENS)
  for j in range(15, 1000, 10):
    print(j)


# Exercicio 9: Solicite um numero ate estar entre 1 e 100.
def exec9():
  print(HEADER_REQUEST_NUMBER_RANGE)
  while True:
    numero = int(input("Insira um numero: "))
    if 1 <= numero <= 100:
      print(f"O numero {numero}, que inseriu, esta entre 1 e 100.")
      break


# Exercicio 10: Leia um numero e escreva quantos divisores ele possui.
def exec10():
  print(HEADER_COUNT_DIVISORS)
  numero = int(input("Insira um numero inteiro: "))
  divisores = 0
  for i in range(1, numero + 1):
    if numero % i == 0:
      divisores += 1
  print(f"O numero {numero} possui {divisores} divisores.")


# Exercicio 11: Produza o output: 1, 22, 333, 4444, 55555.
def exec11():
  print(HEADER_OUTPUT_NUMBERS)
  for i in range(1, 6):
    print(str(i) * i)


# Exercicio 12: Operacoes acumuladas com todos os numeros ate ao valor introduzido.
def exec12():
  print(HEADER_OPERATIONS_NUMBERS)
  numeros = int(input("Quantos numeros quer que se efetue a soma, subtracao, divisao e multiplicacao? "))
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
  print(f"Subtracao: {subtracao}")
  print(f"Divisao: {divisao}")
  print(f"Multiplicacao: {multiplicacao}")
  print(f"Total de operacoes efetuadas: {numeros * 4}")


# Exercicio 13: Leia um numero e mostre a tabuada (1 a 10).
def exec13():
  print(HEADER_TABLE)
  numero = int(input("Insira um numero para mostrar a tabuada: "))
  print_tabuada(numero)


# Exercicio 14: Mostre todas as tabuadas de 1 a 100.
def exec14():
  print(HEADER_TABLE_1_TO_100)
  for j in range(1, 101):
    print_tabuada(j)


# Exercicio 15: Escreve codigo ASCII de 0 a 255, parando de 20 em 20 para confirmar.
def exec15():
  print(HEADER_ASCII)
  for i in range(0, 256, 20):
    for j in range(i, min(i + 20, 256)):
      print(f"{j}: {chr(j)}")
    resposta = input("Deseja continuar? (s/n): ").lower()
    if resposta != "s":
      break


# Exercicio 16: Media de 30 numeros pares, validando entradas entre 1 e 50.
def exec16():
  print(HEADER_EVEN_NUMBERS_AVERAGE)
  min_val, max_val = 1, 50
  soma, pares = 0, 0

  while pares < 30:
    numero = int(input(f"Insira um numero entre {min_val} e {max_val}: "))
    while numero < min_val or numero > max_val:
      numero = int(input(f"Numero invalido. Insira um numero entre {min_val} e {max_val}: "))

    if numero % 2 == 0:
      soma += numero
      pares += 1

  media = soma / pares
  print(f"A media dos numeros pares e: {round(media, 2)}")


# Exercicio 17: Determine os multiplos de 5 que nao sao multiplos de 3 de 1 a 1000.
def exec17():
  print(HEADER_MULTIPLES_5_NOT_3)
  for i in range(1, 1001):
    if i % 5 == 0 and i % 3 != 0:
      print(i)


# Exercicio 18: Leia um valor e indique os numeros perfeitos ate esse valor.
def exec18():
  print(HEADER_PERFECT_NUMBERS)
  numero = int(input("Insira um numero inteiro: "))
  perfeitos = []
  for i in range(1, numero + 1):
    soma_divisores = sum(j for j in range(1, i) if i % j == 0)
    if soma_divisores == i:
      perfeitos.append(i)
  print(f"Numeros perfeitos ate {numero}: {perfeitos}")


# Exercicio 19: Mostre os primeiros 60 numeros da serie de Fibonacci.
def exec19():
  print(HEADER_FIBONACCI_SERIES)
  a, b = 1, 1
  for _ in range(60):
    print(a)
    a, b = b, a + b


# Teste Final (parte 1): Analise de numeros com validacao e pausa de 10 em 10.
def exec20():
  print(HEADER_NUMBER_ANALYSIS)
  while True:
    entrada = int(input("Insira um numero inteiro entre 1 e 30000: "))
    if 1 <= entrada <= 30000:
      for i in range(1, entrada + 1):
        if i > 1:
          for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
              break
          else:
            print(f"{i} e um numero primo.")

        divisores = sum(1 for k in range(1, i + 1) if i % k == 0)
        print(f"{i} possui {divisores} divisores.")

        soma_divisores = sum(l for l in range(1, i) if i % l == 0)
        if soma_divisores == i:
          print(f"{i} e um numero perfeito.")

        if i % 10 == 0:
          resposta = input("Deseja continuar? (s/n): ").lower()
          if resposta != "s":
            break
      break
    else:
      print("Numero invalido. Por favor, insira um numero entre 1 e 30000.")


# Teste Final (parte 2): Calculadora simples (+, -, *, /) com tabuada.
def exec21():
  print(HEADER_SIMPLE_CALCULATOR)
  while True:
    print("1. Soma")
    print("2. Subtracao")
    print("3. Multiplicacao")
    print("4. Divisao")
    print("5. Tabuada")
    print("6. Sair")
    escolha = input("Escolha uma opcao: ")

    match escolha:
      case "1":
        resultado = calc_operation("add")
        print(f"Resultado da soma: {resultado}")
      case "2":
        resultado = calc_operation("sub")
        print(f"Resultado da subtracao: {resultado}")
      case "3":
        resultado = calc_operation("mult")
        print(f"Resultado da multiplicacao: {resultado}")
      case "4":
        resultado = calc_operation("div")
        print(f"Resultado da divisao: {resultado}")
      case "5":
        max_num = int(input("Insira o numero maximo para a tabuada (entre 1 e 1000): "))
        if 1 <= max_num <= 1000:
          for j in range(1, max_num + 1):
            print_tabuada(j)
            if j % 20 == 0:
              resposta = input("Deseja continuar? (s/n): ").lower()
              if resposta != "s":
                break
      case "6":
        print("A sair do programa.")
        break
      case _:
        print("Opcao invalida. Por favor, tente novamente.")


# Teste Final (parte 3): Base de dados de clientes com insercao, listagem e pesquisa por numero.
def exec22():
  print(HEADER_CLIENT_DATABASE)
  db = []
  desconto1 = 0.05
  desconto2 = 0.10
  desconto3 = 0.15

  while True:
    print("1. Inserir cliente")
    print("2. Listar clientes")
    print("3. Procurar por numero de cliente")
    print("4. Sair")

    escolha = input("Escolha uma opcao: ")

    if escolha == "1":
      name = input("Insira o nome do cliente: ")
      address = input("Insira a morada do cliente: ")
      tel = input("Insira o telefone do cliente: ")
      nif = input("Insira o NIF do cliente: ")
      purchase = float(input("Insira o valor da compra: "))

      if purchase < 100:
        discount = 0
      elif 100 <= purchase < 200:
        discount = purchase * desconto1
      elif 200 <= purchase < 500:
        discount = purchase * desconto2
      else:
        discount = purchase * desconto3

      divfin = purchase - discount
      numcli = len(db) + 1
      client = {
        "id": numcli,
        "nome": name,
        "morada": address,
        "tel": tel,
        "nif": nif,
        "compra": purchase,
        "divfin": divfin,
      }
      db.append(client)

    elif escolha == "2":
      for cliente in db:
        print_client(cliente)

    elif escolha == "3":
      numcli_busca = int(input("Insira o numero do cliente para busca: "))
      for cliente in db:
        if cliente["id"] == numcli_busca:
          print_client(cliente)
          break
      else:
        print("Cliente nao encontrado.")

    elif escolha == "4":
      print("A sair do programa.")
      break


def main():
  exec1()
  exec2()
  exec3()
  exec4()
  exec5()
  exec6()
  exec7()
  exec8()
  exec9()
  exec10()
  exec11()
  exec12()
  exec13()
  exec14()
  exec15()
  exec16()
  exec17()
  exec18()
  exec19()
  exec20()
  exec21()
  exec22()


if __name__ == "__main__":
  main()
