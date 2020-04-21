import requests

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
url_requisito = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=0ae42f373d8243a613858a0d58bef7ecd3799228'
url_resposta = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=0ae42f373d8243a613858a0d58bef7ecd3799228'
answer = 'C:\\Users\\Barbara\\Desktop\\codenation\\codenation\\answer.json'

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
    escolha = int(input(" 1 Encriptar: \n 2 Decriptar: \n 3 Requisição: \n 4 Enviar: "))
    if escolha == 1:
        rotacao = int(input("Decida a rotação: "))
        mensagem = input('Escreva uma mensagem: ')
        encriptar(rotacao, mensagem)
    elif escolha == 2:
        rotacao = int(input("Decida a rotação: "))
        mensagem = input('Escreva uma mensagem: ')
        decriptar(rotacao, mensagem)
    elif escolha == 3:
        requisito(url_requisito)
    elif escolha == 4:
        enviar(url_resposta)

def requisito(url_requisito):
    resposta = requests.get(url_requisito)
    with open(answer, 'w+') as arquivo:
        arquivo.write(resposta.text) 
        print('status: ', resposta.status_code)

def enviar(url_resposta):
    arquivo = {'answer': ('answer.json', open(answer, 'rb'))}
    resposta = requests.post(url_resposta, files=arquivo)
    print('status: ', resposta.status_code)

decida()