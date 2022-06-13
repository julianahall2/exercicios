from typing import Union, Any, List


def e_primo(numero):
    if numero > 1:
        for i in range(2, numero):
            if (numero % i) == 0:
                return f'{numero} Não é primo'
        return f'{numero} É primo'


print(e_primo(9))

lista = [0, 0, 0, 0]

while True:
    num = int(input("Digite um número:"))
    if num > 0:
        continue
    for num in range[0, 26]:
        lista[0] += 1
    for num in range[26, 51]:
        lista[1] += 1
    for num in range[51, 76]:
        lista[2] += 1
    for num in range[76, 101]:
        lista[3] += 1

    if num[0, 26]:
        valor1 = lista[0]
    if num[26, 51]:
        valor2 = lista[1]
    if num[51, 76]:
        valor3 = lista[2]
    if num[76, 101]:
        valor4 = lista[3]

    print(f'[0-25]: {valor1} \n[26-50]: {valor2}\n[51-75]: {valor3}\n[76-100]: {valor4}\n')
