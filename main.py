from utils import *
import hashlib
import time

global userid

def sha256(texto: str) -> str:
    return hashlib.sha256(texto.encode()).hexdigest()


def main():
    while True:
        clear_terminal()
        print("""Olá, você ainda não entrou em nenhuma conta
              1- Logar
              2- Registrar""")
        opcao = int(input('opção: '))
        if opcao == 1:
            clear_terminal()
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")

            if logar(email=email, senha=sha256(senha)) == None:
                print("Algo está errado ai parcero")
                time.sleep(3)
            else:
                userid = logar(email=email, senha=sha256(senha))
                painel_principal(userid)
                

        elif opcao == 2:
            clear_terminal()
            nome = input('Digite seu nome: ')
            email = input('Digite seu email: ')
            senha = input('Digite sua senha: ')
            
            if procurar_infos(email=email) != None:
                print("Algum erro aconteceu")
                time.sleep(3)
            else:
                clear_terminal()
                criar_conta(nome=nome, email=email, senha=sha256(senha))
                print('Você criou a sua conta com sucesso! Agora é só logar')
                time.sleep(3)
                
        else:
            print("Opção não encontrada!")
            time.sleep(3)


def painel_principal(userid):
    while True:
        nome, dinheiro, emprestimo, pixkey = pegar_infos(userid)
        clear_terminal()
        print(f"""
        Seja bem vindo {nome},
        Seu saldo é de {dinheiro} reais,
        Você pegou um emprestimo de {emprestimo} reais,
        Sua chave pix é {pixkey}

        O que gostaria de fazer?

        1- Transferir
        2- Pegar ou pagar emprestimo
        3- Editar sua chave pix
        4- Ver suas informações completa
        """)

        opcao = int(input("Escolha sua opção: "))
        match opcao:
            case 1:
                clear_terminal()
                print("Em construção ainda")
                painel_principal(userid)
            case 2:
                
                while True:
                    clear_terminal()
                    print(f"""
                    Olá, {nome}
                    Atualmente sua divida é de {emprestimo}
                    1- Pagar emprestimo
                    2- Solicitar emprestimo
                    3- Voltar
                    """)
                    emprop = int(input("Selecione sua opção: "))
                    if emprop == 1:
                        if emprestimo <= 0:
                            clear_terminal()
                            print('Você não tem emprestimos para pagar')
                            time.sleep(3)
                        else:
                            while True:
                                clear_terminal()
                                emprestimocomjuros = (20/100*emprestimo)+emprestimo
                                print(f'Você realmente que pagar o emprestimo?\nO valor debitado será de {emprestimocomjuros}\nDigite Sim ou Não')
                                opt = input("Digite sua resposta: ")
                                if opt.lower() == "sim":
                                    if dinheiro >= emprestimocomjuros:
                                        clear_terminal()
                                        pagar_emprestimo(userid, emprestimocomjuros)
                                        print('Você pagou o emprestimo com sucesso ')
                                        time.sleep(3)
                                    else:
                                        clear_terminal()
                                        print('Você não tem dinheiro suficiente')
                                        time.sleep(3)
                                elif opt.lower() == "não" or opt.lower() == "nao":
                                    break
                                else:
                                    clear_terminal()
                                    print('Essa opção não existe, tente denovo')
                    elif emprop == 2:
                        while True:
                            clear_terminal()
                            valor = int(input('Digite a quantia: '))
                            solicitar_emprestimo(userid, valor)
                            clear_terminal()
                            print("Você pegou um emprestimo, o valor dos juro, será de 20%")
                            time.sleep(3)
                            painel_principal(userid)
                    elif emprop == 3:
                        painel_principal(userid)
                    else:
                        print('Opção invalida')
            case 3:
                while True:
                    clear_terminal()
                    print(f"""
                    Atualmente sua chave Dix é "{pixkey}"
                    1- Mudar Chave Dix
                    2- Voltar
                    """)
                    pixop = int(input('Digite sua opção: '))
                    if pixop == 1:
                        pixn = input("Digite sua nova palavra Dix: ")
                        mudar_pix(pixn, userid)

                        painel_principal(userid)
                    elif pixop == 2:
                        clear_terminal()
                        painel_principal()
                    else:
                        clear_terminal()
                        print("Opção não encontrada!")
                        time.sleep(3)
            case 4:
                print('a')



main()