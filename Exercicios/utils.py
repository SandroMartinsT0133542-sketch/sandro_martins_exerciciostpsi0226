
"""utils"""
def print_client(cliente, sep="\n"):
  print(f"-------------------------------- Cliente {cliente['id']}  --------------------------------")
  print(f"Nome: {cliente['nome']}{sep}Morada: {cliente['morada']}{sep}Telefone: {cliente['tel']}{sep}NIF: {cliente['nif']}{sep}Compra: {cliente['compra']}{sep}Divida Final: {cliente['divfin']}")
  print("-----------------------------------------------------------------------")


def print_tabuada(num):
  print(f"Tabuada do {num}:")
  for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
  print("\n")
