# exercicio encontra o maior e o menor
import random

val1 = random.randint(1, 100)
val2 = random.randint(1, 100)
val3 = random.randint(1, 100)
print("Valor 1:", val1)
print("Valor 2:", val2)
print("Valor 3:", val3)
# encontra o maior
if val1 >= val2 and val1 >= val3:
    maior = val1
elif val2 >= val1 and val2 >= val3:
    maior = val2
else:
    maior = val3
# encontra o menor
if val1 <= val2 and val1 <= val3:
    menor = val1
elif val2 <= val1 and val2 <= val3:
    menor = val2
else:
    menor = val3
print("O maior valor é:", maior)
print("O menor valor é:", menor)
