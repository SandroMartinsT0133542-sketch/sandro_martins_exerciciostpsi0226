
""" 
Exercício 1: Criar um dicionário simples
Cria um dicionário chamado alunos que receba nome, idade e curso de cada aluno:
1-	Inserir
2-	Listar
O mesmo deve imprimir cada elemento do dicionário no seguinte formato por cada aluno:
Exemplo:
nome: Maria
idade: 20
curso: Engenharia
"""

def print_student_info(alunos:dict):

  print("-------------------------------- Lista de alunos --------------------------------")
  if(len(alunos) == 0):
    print("Nenhum aluno encontrado.")
    print("----------------------------------------------------------------")

  else:
    for aluno in alunos:
      for nome, info in aluno.items():
        print('----------------------------------------------------------------')
        print(f"Nome: {nome}")
        print(f"Idade: {info['idade']}")
        print(f"Curso: {info['curso']}\n")
        print("----------------------------------------------------------------")

def add_student(alunos:dict):
  nome = input("Insira o nome do aluno: ")
  idade = int(input("Insira a idade do aluno: "))
  curso = input("Insira o curso do aluno: ")

  alunos.append({nome: {"idade": idade, "curso": curso}})

def students_dict():
  alunos = []
  while True:
    print("1.Inserir dados do aluno:")
    print("2.Listar alunos:")
    print("3.Sair")
    opt = input("Escolha uma opção: ")
    match opt:
      case "1":
        add_student(alunos)
      case "2":
        print_student_info(alunos)
      case "3":
        print("Saindo do programa.")
        break
      case _:
        print("Opção inválida. Tente novamente.")

students_dict()

"""
Exercício 2: Aceder a valores no dicionário dado o seguinte dicionário:
carro = {'marca': 'Toyota', 'modelo': 'Corolla', 'ano': 2020}
Escreve uma linha de código que imprima apenas o modelo do carro.
"""
def print_car_model(item :dict):
  print(item['modelo'])

print_car_model({'marca': 'Toyota', 'modelo': 'Corolla', 'ano': 2020})

"""
Exercício 3: Cria um dicionário vazio chamado produto. Em seguida:
1.	Adiciona os seguintes pares chave-valor:
o	nome: "Telemóvel"
o	preço: 1500
o	stock: 30
2.	Remove a chave stock do dicionário.
3.	Imprime o dicionário final.
"""
def remove_key(d:dict, key:str):
  if key in d:
    del d[key]

print(remove_key({'nome': "Telemóvel", 'preço': 1500, 'stock': 30}, 'stock'))

"""
Exercício 4: Verificar se uma chave existe
Dado o dicionário:
utilizador = {'nome': 'Carlos', 'idade': 28}
Escreve um código que verifique se a chave email está presente no dicionário e imprima uma mensagem adequada, por exemplo: "Email não encontrado."
"""
def check_key(d:dict, key:str):
  if key in d:
    print(f"{key} encontrado: {d[key]}")
  else:
    print(f"{key} não encontrado.")

check_key({'nome': 'Carlos', 'idade': 28}, 'email')

"""
Exercício 5: Contar letras numa palavra
Pede ao utilizador que introduza uma palavra. Em seguida, cria um dicionário onde cada letra da palavra é uma chave e o seu valor é o número de vezes que essa letra aparece.
Exemplo de entrada: "banana"
Resultado esperado: {'b': 1, 'a': 3, 'n': 2}
# Saída: {'b': 1, 'a': 3, 'n': 2}
"""

def count_letters(word:str):
  letter_count = {}
  for char in word:
    if char in letter_count:
      letter_count[char] += 1
    else:
      letter_count[char] = 1
  return letter_count

print(count_letters("banana"))

"""
Exercício 6: Somar valores de um dicionário
Dado o seguinte dicionário com os valores de vendas por mês:
vendas = {'Janeiro': 1000, 'Fevereiro': 1500, 'Março': 1200}
Calcula o total de vendas do trimestre e imprime o resultado.
"""

def sum_sales(sales:dict):
  total = 0
  for month, value in sales.items():
    total += value
  return total
  
sales_calendar = {
  'Janeiro': 1000, 'Fevereiro': 1500, 'Março': 1200, 
  'Abril': 1200, 'Maio': 1300, 'Junho': 1100, 'Julho': 1400, 
  'Agosto': 1600, 'Setembro': 1250, 'Outubro': 1350, 
  'Novembro': 1450, 'Dezembro': 1550, 
  }

print(f"Total de vendas: {sum_sales(sales_calendar)}")
print(f"Total de vendas do trimestre: {sum_sales({month: sales_calendar[month] for month in ['Janeiro', 'Fevereiro', 'Março']} )}")

"""
Exercício 7: Inverter chaves e valores
Tens o seguinte dicionário:
d = {'a': 1, 'b': 2, 'c': 3}
Cria um novo dicionário que tenha os valores como chaves e as chaves como valores. Resultado esperado:
{1: 'a', 2: 'b', 3: 'c'}
"""

def invert_dict(d:dict):
  inverted = {}
  for key, value in d.items():
    inverted[value] = key
  return inverted

print(invert_dict({'a': 1, 'b': 2, 'c': 3}))


"""
Exercício 8: Juntar dois dicionários
Dado os seguintes dicionários:
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
Cria um novo dicionário que contenha os pares chave-valor dos dois dicionários juntos.
"""
def merge_dicts(d1:dict, d2:dict):
  merged = { **d1, **d2 }
  return merged

print(merge_dicts({'a': 1, 'b': 2}, {'c': 3, 'd': 4}))


"""
Exercício 9: Notas dos alunos
Cria um dicionário com o nome dos alunos e as suas respetivas listas de notas:
notas = {
    'João': [7, 8, 9],
    'Maria': [10, 9, 8],
    'Ana': [6, 7, 8]
}
Calcula e imprime a média de cada aluno, com o seguinte formato:
João: 8.0
Maria: 9.0
Ana: 7.0
"""

def calculate_average(grades:dict):
  for student, marks in grades.items():
    average = sum(marks) / len(marks)
    print(f"{student}: {average:.1f}")

calculate_average({
    'João': [7, 8, 9],
    'Maria': [10, 9, 8],
    'Ana': [6, 7, 8]
})

"""
Exercício 10: Contar palavras numa frase
Pede ao utilizador para introduzir uma frase. Cria um dicionário que contenha cada palavra da frase como chave e o número de vezes que ela aparece como value.
Exemplo de entrada:
"hoje é um bom dia e hoje o sol está a brilhar"
Resultado esperado:
{'hoje': 2, 'é': 1, 'um': 1, 'bom': 1, 'dia': 1, 'e': 1, 'o': 1, 'sol': 1, 'está': 1, 'a': 1, 'brilhar': 1}
"""
def count_words(phrase:str):
  word_count = {}
  words = phrase.split()
  for word in words:
    if word in word_count:
      word_count[word] += 1
    else:
      word_count[word] = 1
  return word_count

print(count_words("hoje é um bom dia e hoje o sol está a brilhar"))
