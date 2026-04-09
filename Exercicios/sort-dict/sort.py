""" 1. Ordenar uma lista de palavras por ordem alfabética (A → Z)
Objetivo: Reordenar as palavras, comparando carácter por carácter, como se estivesses a fazer o papel da função sorted().
Exemplo:
["banana", "uva", "abacaxi", "laranja"]
Resultado esperado:
["abacaxi", "banana", "laranja", "uva"]
Como fazer:
•	Compara as palavras duas a duas.
•	Usa o código ASCII de cada letra para decidir qual vem antes.
•	Se duas palavras começarem pela mesma letra, continua a comparação na letra seguinte.
•	Se uma palavra for prefixo da outra (como "casa" e "casamento"), a mais curta deve vir primeiro. """

def comes_after(word_a:str, word_b:str):
  min_len = min(len(word_a), len(word_b))

  for index in range(min_len):
    if ord(word_a[index]) > ord(word_b[index]):
      return True
    if ord(word_a[index]) < ord(word_b[index]):
      return False

  # If all compared letters are equal, the longer word comes after.
  return len(word_a) > len(word_b)

def sort_array(arr:list[str]):
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      if comes_after(arr[i], arr[j]):
        arr[i], arr[j] = arr[j], arr[i]
  return arr

print(sort_array(["banana", "uva", "abacaxi", "laranja"]))
print(sort_array(["dados", "Rede", "Casa", "casamento", "Casamento", "casa", "Python", "inteligência", "Aprender", "dados", "Rede"]))


""" 2. Ordenar uma lista de palavras por ordem alfabética inversa (Z → A), ignorando maiúsculas/minúsculas
Objetivo: Reordenar da última letra do alfabeto para a primeira, sem distinguir maiúsculas de minúsculas.
Exemplo:
["Python", "inteligência", "Aprender", "dados", "Rede"]
Resultado esperado:
["Rede", "Python", "inteligência", "dados", "Aprender"]
Como fazer:
•	Compara os caracteres em minúsculas ("A" e "a" passam a ser tratados como iguais).
•	Ordena da última letra para a primeira.
•	A lógica da comparação será invertida: em vez de colocar as menores primeiro, colocas as maiores. """

def sort_array_reverse(arr:list[str]):
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      if arr[i].lower() < arr[j].lower():
        arr[i], arr[j] = arr[j], arr[i]
  return arr  

print(sort_array_reverse(["Python", "inteligência", "Aprender", "dados", "Rede"]))

""" 3. Ordenar os caracteres de uma palavra por ordem alfabética
Objetivo: Pega numa palavra e reorganiza as suas letras da mais "baixa" para a mais "alta", segundo o valor ASCII.
Exemplo:
"algoritmo"
Resultado esperado:
"agilmootr"
Como fazer:
•	Divide a palavra em caracteres.
•	Ordena os caracteres com base no valor de ord().
•	Junta novamente numa string.
Este exercício é útil para aprender como a ordenação funciona mesmo a nível de caracteres, não só de palavras inteiras.
"""

def sort_characters(word:str):
  chars = list(word)
  for i in range(len(chars)):
    for j in range(i + 1, len(chars)):
      if ord(chars[i]) > ord(chars[j]):
        chars[i], chars[j] = chars[j], chars[i]
  return ''.join(chars)

print(sort_characters("algoritmo"))

""" 4. Ordenar uma lista de palavras pela quantidade de letras minúsculas
Objetivo: Contar quantas letras minúsculas há em cada palavra e ordená-las do menor para o maior número.
Exemplo:
["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]
Resultado esperado:
["CÓDIGO", "intELIGENTE", "PYthon", "dados", "banana"]
Como fazer:
•	Conta, para cada palavra, quantos caracteres estão entre 'a' e 'z'.
•	Usa esse número como "peso" para ordenar.
•	Palavras com mais minúsculas vão para o fim da lista.""" 

def count_lowercase(word:str):
  count = 0
  for char in word:
    if 'a' <= char <= 'z':
      count += 1
  return count

def sort_by_lowercase(arr:list[str]):
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      if count_lowercase(arr[i]) > count_lowercase(arr[j]):
        arr[i], arr[j] = arr[j], arr[i]
  return arr

print(sort_by_lowercase(["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]))


""" 5. Agrupar palavras pela letra inicial e ordenar cada grupo por ordem alfabética (A → Z)
Objetivo: Reorganizar as palavras em grupos que comecem com a mesma letra, e depois ordenar cada grupo manualmente.
Exemplo:
["banana", "bola", "abacaxi", "arroz", "uva", "urso"]
Resultado esperado:
{
  'b': ['banana', 'bola'],
  'a': ['abacaxi', 'arroz'],
  'u': ['urso', 'uva']
}
Como fazer:
•	Cria um dicionário onde cada chave é uma letra inicial.
•	Coloca cada palavra no grupo correspondente.
•	Ordena cada grupo individualmente usando comparação com ord().
Este é o exercício mais completo: vais precisar de organizar, comparar e ordenar em dois níveis.
"""

def group_and_sort(arr:list[str]):
  groups = {}
  for word in arr:
    initial = word[0].lower()
    if initial not in groups:
      groups[initial] = []
    groups[initial].append(word)

  for key in groups:
    groups[key] = sort_array(groups[key])
  
  return groups

print(group_and_sort(["banana", "bola", "abacaxi", "arroz", "uva", "urso"]))