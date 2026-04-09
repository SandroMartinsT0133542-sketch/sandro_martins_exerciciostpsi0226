nomes=["da","fa","oi","da"]
posicoes = []

def insert(nomesi:list):
  nomesi.append(input("Insira um nome: "))

def listar(nomesl:list, posicoes:list[int]=None):
  print("-------------------------------- Lista de nomes --------------------------------")
  if(nomes is None):
     print("Nenhum nome encontrado")
  else:
    for i in range(len(nomesl)):
      if posicoes is None:
        print(f"Nome: {nomesl[i]}")
      else:
        if i in posicoes:
          print(f"Nome: {nomesl[i]} - posição {i}")
  print("----------------------------------------------------------------")

def delete(nomesd:list, indice:list[int], callback=None):
  if callback is not None:
    callback()

  index = int(input("Insira o índice do nome a ser apagado: "))
  
  while(index not in indice):
    index = int(input("Insira o índice do nome a ser apagado: "))
    
  nomesd.pop(index)


def procurar(nomesp:list, callback=None):
  posicoes.clear()
  nome=input("Insira o nome de procura: ")

  for i in range(len(nomesp)):
    if nomesp[i] == nome:
      posicoes.append(i)

  if callback is not None:
    if len(posicoes) > 0: 
      callback(nomesp, posicoes)
    else:
      callback(None)

while True:
    print ("1 - Inserir nome")
    print ("2 - Listar nomes")
    print ("3 - Apagar nome")
    print ("4 - procurar nome")
    print ("5 - sair")
    
    opt=input("Escolha Opção: ")

    match opt:
        case "1":
            insert(nomes)
        case "2":
            listar(nomes)
        case "3":
            delete(nomes, posicoes, procurar(nomes, listar))
        case "4":
            procurar(nomes, listar)
        case "5":
            print("fim do programa")
            break
        case _:
            print("nao escolheu a opçao certa")