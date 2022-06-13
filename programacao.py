#Juliana Azeredo Hall

def e_primo(numero):
    if numero > 1:
        for i in range(2, numero):
            if (numero % i) == 0:
                return f'O número {numero} não é primo'
        return f'O número {numero} é primo'


print(e_primo(97))

passar = False
lista = [0, 0, 0, 0]

while True:
    entrada = int(input("Digite um número.\n\n> "))
    if entrada > 0:
        passar = True

    if 0 < entrada <= 25:
        lista[0] += 1
    elif 25 < entrada <= 50:
        lista[1] += 1
    elif 50 < entrada <= 75:
        lista[2] += 1
    elif 75 < entrada <= 100:
        lista[3] += 1

    if passar:
        print(f'[0-25]: {lista[0]} \n[26-50]: {lista[1]}\n[51-75]: {lista[2]}\n[76-100]: {lista[3]}\n')

import random

texto = list(input("Digite uma palavra:").lower())
final = texto

index = 0
for letra in final:
    tlndex = random.randint(0, len(texto)-1)
    final[index] = texto[tlndex]
    texto[tlndex] = letra
    index = index + 1

print(''.join(final))
