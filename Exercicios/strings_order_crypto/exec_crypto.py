""" Cria um programa que criptografe e descriptografe mensagens utilizando a tabela ASCII e uma chave String. 
A chave será uma palavra ou frase fornecida pelo utilizador, e a criptografia será feita com base na soma dos valores ASCII dos caracteres dessa chave.

Funcionamento da Criptografia

1.	O utilizador introduz:
o	Uma mensagem (ex: "Olá Mundo")
o	Uma chave em formato de string (ex: "chave")

2.	O programa:
o	Calcula a chave numérica, somando os valores ASCII de cada letra da chave:
	"chave" → 'c'=99, 'h'=104, 'a'=97, 'v'=118, 'e'=101
Soma: 99 + 104 + 97 + 118 + 101 = **519**

o	Usa essa soma (519) como valor para criptografar cada caractere da mensagem:
	'O' → ord('O') = 79 → 79 + 519 = 598
	'l' → ord('l') = 108 → 108 + 519 = 627
	etc.

3.	Para descriptografar, o programa deve subtrair o mesmo valor (519 neste caso) de cada número para recuperar os caracteres originais.
Requisitos:

1.	O programa deve conter três funções:
o	criptografar(mensagem: str, chave: str) -> List[int]
o	descriptografar(codigos: List[int], chave: str) -> str

o	Listar
2.	Utilizar apenas funções nativas (ord() e chr()).
3.	Manter os espaços, acentos e distinguir entre maiúsculas e minúsculas.
4.	Impede que a chave seja vazia.
5.	Aplica rotação aos caracteres da mensagem encriptada (entre ASCII 32 e 126), para mantê-los dentro deste intervalo.
"""

# Rotate within the Unicode code point interval to preserve every character.
def calculate_interval(value:int):
  UNICODE_MIN = 0
  UNICODE_MAX = 0x10FFFF 
  # Total amount of valid code points in the configured Unicode range.
  interval_size = UNICODE_MAX - UNICODE_MIN + 1 
  return (value - UNICODE_MIN) % interval_size + UNICODE_MIN

def calculate_string_keys(key:str):
  key_value = 0
  for char in key:
    key_value += ord(char)
  return key_value

def encrypt_message(mensagem:str, key:str):
  if not key:
    raise ValueError("A chave não pode ser vazia.")
  
  key_value = calculate_string_keys(key)
  codes_list = []
  
  for char in mensagem:
    encrypted_value = calculate_interval(ord(char) + key_value)
    codes_list.append(encrypted_value)
  
  return codes_list

def decrypt_message(codes:list[int], key:str):
  if not key:
    raise ValueError("A chave não pode ser vazia.")
  
  key_value = calculate_string_keys(key)
  mensagem = ""
  
  for code in codes:
    decrypted_value = calculate_interval(code - key_value)
    mensagem += chr(decrypted_value)
  
  return mensagem

message = "Olá Mundo, espero que funcione este novo projeto de criptografia!"
decryption_key = "chave"

encrypted_codes = encrypt_message(message, decryption_key)

print("---- Criptografia e Descriptografia de Mensagens ----\n")
print("Codigos da Mensagem Criptografada:", encrypted_codes, "\n")

decrypted_message = decrypt_message(encrypted_codes, decryption_key)
print("Mensagem Descriptografada:", decrypted_message, "\n")

failed_decryption = decrypt_message(encrypted_codes, "chave_errada")
print("Tentativa de Descriptografia com Chave Errada:", failed_decryption, "\n")




