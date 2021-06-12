'''
Vamos jogar?

Faça uma função que recebe duas strings, correspondentes à escolha de cada jogador: "pedra","papel" ou "tesoura". 
A função deve devolver o jogador vencedor, sendo que este é reconhecido pela ordem dos argumentos fornecidos à função. 
Assim, o primeiro argumento se refere ao jogador "um" e o segundo ao jogador "dois".

Por exemplo, caso os argumentos fornecidos sejam ("pedra", "papel"), a função deve retornar: "dois".

Caso ocorra um empate, a função deve retornar a string "empate"

Se a entrada for uma palavra diferente do esperado, a função deve devolver a mensagem: "Escolha pedra, papel ou tesoura para jogar"

Você pode considerar que apenas duas pessoas jogarão por partida e que os argumentos fornecidos à função são sempre strings.

O nome da sua função deve ser pedra_papel_tesoura
'''

def pedra_papel_tesoura(um, dois):
    escolhas_possiveis = ['papel', 'pedra', 'tesoura']
    # Caso quando um ou dois for invalido
    if (um not in escolhas_possiveis) or (dois not in escolhas_possiveis):
        return "Escolha pedra, papel ou tesoura para jogar"

    # Caso do empate
    if um == dois:
        return 'empate'

    # Caso em que alguém ganha
    if (um == 'pedra' and dois == 'tesoura') or (um == 'tesoura' and dois == 'papel') or (um == 'papel' and dois == 'pedra'):
        return 'um'
    return 'dois'

'''def pedra_papel_tesoura(um, dois):
    # Caso quando um ou dois for invalido
    if (um != 'papel' and um != 'pedra' and um != 'tesoura') or (dois != 'papel' and dois != 'pedra' and dois != 'tesoura'):
        return "Escolha pedra, papel ou tesoura para jogar"

    # Caso do empate
    if um == dois:
        return 'empate'

    # Caso em que alguém ganha
    if um == 'pedra' and dois == 'tesoura':
        return 'um'
    elif um == 'tesoura' and dois == 'papel':
        return 'um'
    elif um == 'papel' and dois == 'pedra':
        return 'um'
    return 'dois'
'''
