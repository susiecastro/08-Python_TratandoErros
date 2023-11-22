# Jogo da adivinhação
from random import randint


print('******************************************************')
print('Seja bem-vindo(a) ao jogo de adivinhação')
print('\n')

#Criando variáveis - randint criará um número aleatório de um a 5
numero_secreto = randint(1,5)
numero_escolhido = 0


while True:
    try:
        numero_escolhido = int(input('Escolha um número de 1 a 5: '))
    except:
        print('Você digitou um valor incorreto')
    else:
        if numero_escolhido not in (1, 2, 3, 4, 5):
           print('Número precisa ser de 1 a 5!')
           continue
        elif numero_escolhido == numero_secreto:
            print(f'Parabéns! Você descobriu que o número secreto era o  {numero_secreto}')
            break
        else:
            print('Você errou!')