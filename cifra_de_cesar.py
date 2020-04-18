alfabeto = 'abcdefghijklmnopqrstuvwxyz'




def encriptar(rotacao, mensagem):
    resultado = ''
    for i in mensagem:
        if i in alfabeto:
            codificar = (alfabeto.index(i) + rotacao)
            resultado += alfabeto[(codificar) % len(alfabeto)]
        else:
            resultado += i 
    print(resultado)


def decriptar(rotacao, mensagem):
    resultado = ''
    for i in mensagem:
        if i in alfabeto:
            decodificar = (alfabeto.index(i) - rotacao)
            resultado += alfabeto[(decodificar) % len(alfabeto)]
        else:
            resultado += i 
    print(resultado)

def decida():
    escolha = int(input(" 1 Encriptar: \n 2 Decriptar: "))
    if escolha == 1:
        rotacao = int(input("Decida a rotação: "))
        mensagem = input('Escreva uma mensagem: ')
        encriptar(rotacao, mensagem)
    elif escolha == 2:
        rotacao = int(input("Decida a rotação: "))
        mensagem = input('Escreva uma mensagem: ')
        decriptar(rotacao, mensagem)

decida()


    
