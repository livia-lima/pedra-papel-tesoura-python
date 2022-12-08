import random

# apresenta as opções
print('Você tem 3 opções: p (pedra), a (papel), t (tesoura)')

# pergunta qual opção será escolhida e a guarda numa variável,
# para que seja usada depois

escolha = str(input('Qual opção você escolhe? '))

# definindo a escolha do computador
escolha_computador = random.choice(['p', 'a', 't'])

# situações onde o jogador ganha
if (escolha == 'p' and escolha_computador == 't') or (escolha == 'a' and escolha_computador == 'p') or (escolha == 't' and escolha_computador == 'a'):
    print(
        f'Você escolheu {escolha} e o oponente, {escolha_computador}. Você ganhou')

# situações onde o jogador perde
if (escolha == 'p' and escolha_computador == 'a') or (escolha == 't' and escolha_computador == 'p') or (escolha == 'a' and escolha_computador == 't'):
    print(
        f'Você escolheu {escolha} e o oponente, {escolha_computador}. Você perdeu.')

# situação de empate
if escolha == escolha_computador:
    print(f'Você e o oponente escolheram {escolha}. Houve um empate.')
