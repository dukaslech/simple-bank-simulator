from utils import *
import hashlib


def sha256(texto: str) -> str:
    return hashlib.sha256(texto.encode()).hexdigest()


def main():
    print("Olá, digite 1 para logar e 2 para registrar")
    opcao = int(input('opção: '))
    if opcao == 1:
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

        if logar(email=email, senha=sha256(senha)) == None:
            print("Algo está errado ai parcero")
        else:
            print("Logado")
            

    elif opcao == 2:
        nome = input('Digite seu nome: ')
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')
        
        if procurar_infos(email=email) != None:
            print("Algum erro aconteceu")
        else:
            criar_conta(nome=nome, email=email, senha=sha256(senha))


main()