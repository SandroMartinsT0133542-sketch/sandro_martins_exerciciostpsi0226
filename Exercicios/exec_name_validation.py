""" Cria um programa que peça ao utilizador para introduzir o seu nome completo. 
O programa deve validar se o nome contém apenas letras e espaços, 
a primeira letra do nome deve ser sempre maiúscula e a seguir ao espaço também, 
usando os códigos ASCII de cada caractere.

Exemplo:
Pedro Pereira 

Se o nome for válido, o programa deve exibir:
"Nome válido!"
Caso contrário, deve exibir:
"Nome inválido: contém caracteres não permitidos."

No caso de o programa encontrar um caractere invalido deve parar a execução.

Exemplos Inválidos:
Miguel PriMo
Luis AnseLmo
Guilherme ramos
"""

def validate_name():
  name = input("Digite seu nome completo: ")

  for char in name:
    if not (char.isalpha() or char.isspace()):
      print("Nome inválido: contém caracteres não permitidos.")
      return False
  words = name.split()
  for word in words:
    if not word[0].isupper():
      print("Nome inválido: a primeira letra de cada palavra deve ser maiúscula.")
      return False
  print("Nome válido!")
  return True

validate_name()
