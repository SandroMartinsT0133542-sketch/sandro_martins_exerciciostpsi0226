
""" 
1. Tipo de dia
Cria um programa que receba o nome de um dia da semana e diga se é dia útil ou fim de semana.
Exemplo:
Entrada → domingo
Saída → Fim de semana 
"""

print("-------------------------------- Tipo de dia --------------------------------")

dia = input("Digite o nome de um dia da semana: ").lower()
match dia:
  case "segunda-feira" | "terça-feira" | "quarta-feira" | "quinta-feira" | "sexta-feira":
    print("Dia útil")
  case "sabado" | "sábado" | "domingo":
    print("Fim de semana")
  case _:
    print("Dia inválido")



""" 
2. Classificação de nota
Lê uma nota (0–100) e retorna uma classificação:
•	90 ou mais → Excelente
•	70–89 → Bom
•	50–69 → Suficiente
•	Abaixo de 50 → Insuficiente
Exemplo:
Entrada → 70-89
Saída →  Bom 
"""

print("-------------------------------- Classificação de nota --------------------------------")

nota = float(input("Digite uma nota (0-100): "))

match nota:
  case nota if nota >= 90:
    print("Excelente")
  case nota if nota >= 70:
    print("Bom")
  case nota if nota >= 50:
    print("Suficiente")
  case nota if nota >= 0:
    print("Insuficiente")
  case _:
    print("Nota inválida")


""" 
3. Tipo de pedido
Recebe um dicionário com as chaves "tipo" e "valor".

Exibe:
•	“Compra de X€” se tipo for “compra”
•	“Venda de X€” se tipo for “venda”
•	“Pedido desconhecido” caso contrário

Exemplo:
Entrada → {"tipo": "venda", "valor": 250}
Saída → Venda de 250€ 
"""

print("-------------------------------- Tipo de pedido --------------------------------")

pedidos = [{"tipo": "compra", "valor": 100}, {"tipo": "venda", "valor": 250}, {"tipo": "aluguel", "valor": 300}]

for pedido in pedidos:
  match pedido: 
    case {"tipo": "compra", "valor": valor}:
      print(f"Tipo de pedido: compra")
      print(f"Compra de {valor}€")
    case {"tipo": "venda", "valor": valor}:
      print(f"Tipo de pedido: venda")
      print(f"Venda de {valor}€")
    case _:
      print(f"Tipo de pedido: desconhecido")


""" 
4. Tipo de dado
Analisa um valor e retorna o seu tipo:
•	Número inteiro
•	Número decimal
•	String numérica
•	String textual
•	Lista
•	Tipo desconhecido
Exemplo:
Entrada → [10, 20, 30]
Saída → Lista 
"""

print("-------------------------------- Tipo de dado --------------------------------")
valor = input("Digite um valor: ")

match valor:
  case valor if type(valor) == int:
    print("Número inteiro")
  case valor if type(valor) == float:
    print("Número decimal")
  case valor if type(valor) == str and valor.isnumeric():
    print("String numérica")
  case valor if type(valor) == str:
    print("String textual")
  case valor if valor.startswith("[") and valor.endswith("]"):
    print("Lista")
  case valor if valor.startswith("(") and valor.endswith(")"):
    print("Tupla")
  case valor if valor.startswith("{") and valor.endswith("}"):
    print("Dicionário")
  case _:
    print("Tipo desconhecido")

""" 
5. Análise de mensagem
Recebe uma mensagem e retorna:
•	“Saudação” se for “olá” ou “bom dia”
•	“Pergunta” se terminar com “?”
•	“Despedida” se contiver “tchau” ou “adeus”
•	“Mensagem genérica” caso contrário
Exemplo:
Entrada → “Tudo bem?”
Saída → Pergunta 
"""

print("-------------------------------- Análise de mensagem --------------------------------")

mensagem = input("Digite uma mensagem: ").lower()

match mensagem:
  case "ola" | "olá" | "bom dia":
    print("Saudação")
  case mensagem if mensagem.endswith("?"):
    print("Pergunta")
  case mensagem if "tchau" in mensagem or "adeus" in mensagem:
    print("Despedida")
  case _:
    print("Mensagem genérica")

""" 
6. Estado do servidor
Recebe um dicionário com as chaves "status" e "tempo_resposta".
Retorna:
•	“Servidor ativo” se o status for “ok”
•	“Servidor lento” se o status for “ok” e o tempo de resposta for maior que 200 ms
•	“Servidor indisponível” se o status for “erro”
•	“Estado desconhecido” caso contrário
Exemplo:
Entrada → {"status": "ok", "tempo_resposta": 350}
Saída → Servidor lento 
"""

print("-------------------------------- Estado do servidor --------------------------------")
servidores = [{"status": "ok", "tempo_resposta": 150}, {"status": "ok", "tempo_resposta": 350}, {"status": "erro", "tempo_resposta": 0}, {"status": "desconecido", "tempo_resposta": 100}]

for servidor in servidores:
  match servidor:
    case {"status": "ok", "tempo_resposta": tempo} if tempo > 200:
      print("Servidor lento")
    case {"status": "ok"}:
      print("Servidor ativo")
    case {"status": "erro"}:
      print("Servidor indisponível")
    case _:
      print("Estado desconhecido")

""" 
7. Classificação de produto
Recebe um dicionário com as chaves "categoria" e "preco".
Retorna:
•	“Produto de luxo” se categoria for “eletrônico” e preço acima de 1000
•	“Produto comum” se categoria for “eletrônico” e preço até 1000
•	“Produto alimentar” se categoria for “alimento”
•	“Categoria desconhecida” caso contrário
Exemplo:
Entrada → {"categoria": "eletrônico", "preco": 1500}
Saída → Produto de luxo 
"""
print("-------------------------------- Classificação de produto --------------------------------")
produtos = [{"categoria": "eletrônico", "preco": 1500}, {"categoria": "eletrônico", "preco": 800}, {"categoria": "alimento", "preco": 10}, {"categoria": "roupa", "preco": 50}]

for produto in produtos:
  match produto:
    case {"categoria": "eletrônico", "preco": preco} if preco > 1000:
      print("Produto de luxo")
    case {"categoria": "eletrônico", "preco": preco} if preco <= 1000:
      print("Produto comum")
    case {"categoria": "alimento"}:
      print("Produto alimentar")
    case _:
      print("Categoria desconhecida")


""" 
8. Operação matemática
Recebe uma operação (em texto) e dois números.
Operações válidas: "soma", "subtrai", "multiplica", "divide".
Exemplo:
Entrada →
Operação: "divide"
Número 1: 20
Número 2: 4
Saída → 5 
"""

print("-------------------------------- Operação matemática --------------------------------")
operacao = input("Digite a operação (soma, subtrai, multiplica, divide): ").lower()
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

match operacao:
  case "soma":
    resultado = num1 + num2
    print(f"Resultado: {resultado}")
  case "subtrai":
    resultado = num1 - num2
    print(f"Resultado: {resultado}")
  case "multiplica":
    resultado = num1 * num2
    print(f"Resultado: {resultado}")
  case "divide":
    if num2 != 0:
      resultado = num1 / num2
      print(f"Resultado: {resultado}")
    else:
      print("Erro: Divisão por zero")
  case _:
    print("Operação inválida")


""" 
9. Processamento de requisição
Recebe um dicionário com as chaves "metodo" e "conteudo".
Retorna:
•	“Requisição GET recebida” se o método for “GET”
•	“Requisição POST com dados válidos” se o método for “POST” e o conteúdo não estiver vazio
•	“Requisição POST sem dados” se o método for “POST” e o conteúdo estiver vazio
•	“Método não suportado” caso contrário
Exemplo:
Entrada → {"metodo": "POST", "conteudo": ""}
Saída → Requisição POST sem dados 
"""

print("-------------------------------- Processamento de requisição --------------------------------")
requisicoes = [{"metodo": "GET", "conteudo": "dados"}, {"metodo": "POST", "conteudo": "dados"}, {"metodo": "POST", "conteudo": ""}, {"metodo": "PUT", "conteudo": "dados"}] 
for requisicao in requisicoes:
  match requisicao:
    case {"metodo": "GET"}:
      print("Requisição GET recebida")
    case {"metodo": "POST", "conteudo": conteudo} if conteudo:
      print("Requisição POST com dados válidos")
    case {"metodo": "POST", "conteudo": conteudo} if not conteudo:
      print("Requisição POST sem dados")
    case _:
      print("Método não suportado")

""" 
10. Jogo: Pedra, Papel ou Tesoura
Cria um programa que receba duas jogadas:
•	Jogador 1
•	Jogador 2
Usa match para determinar o resultado:
•	Pedra ganha de Tesoura
•	Tesoura ganha de Papel
•	Papel ganha de Pedra
•	Se forem iguais, é Empate
Exemplo:
Entrada →
Jogador 1: pedra
Jogador 2: tesoura
Saída → Jogador 1 venceu 
"""

print("-------------------------------- Jogo: Pedra, Papel ou Tesoura --------------------------------")
jogada1 = input("Jogador 1, digite sua jogada (pedra, papel ou tesoura): ").lower()
jogada2 = input("Jogador 2, digite sua jogada (pedra, papel ou tesoura): ").lower()

match (jogada1, jogada2):
  case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
    print("Jogador 1 venceu")
  case ("tesoura", "pedra") | ("papel", "tesoura") | ("pedra", "papel"):
    print("Jogador 2 venceu")
  case _ if jogada1 == jogada2:
    print("Empate")
  case _:
    print("Jogada inválida")   
