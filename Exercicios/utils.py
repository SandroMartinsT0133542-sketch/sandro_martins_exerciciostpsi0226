
"""utils"""

from typing import Literal
from unittest import case

"""Types"""
op = Literal["add", "sub", "mult", "div"]

"""functions"""
def print_client(cliente, sep="\n"):
  print(f"-------------------------------- Cliente {cliente['id']}  --------------------------------")
  print(f"Nome: {cliente['nome']}{sep}Morada: {cliente['morada']}{sep}Telefone: {cliente['tel']}{sep}NIF: {cliente['nif']}{sep}Compra: {cliente['compra']}{sep}Divida Final: {cliente['divfin']}")
  print("-----------------------------------------------------------------------")


def print_tabuada(num):
  print(f"Tabuada do {num}:")
  for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
  print("\n")

def calc_operation(operation: op):
  num1 = float(input("Insira o primeiro número: "))
  num2 = float(input("Insira o segundo número: "))

  match operation:
    case "add":
      return num1 + num2
    case "sub":
      return num1 - num2
    case "mult":
      return num1 * num2
    case "div":
      return num1 / num2 if num2 != 0 else "Divisão por zero não é permitida"