
"""

escreva um algoritimo que permita cadastrar esse jogos
informando o nome e qual video game ele pertença
*Exigencia
para isso, crie um menu de opções contendo:
cadastrar novo iten, listar tudo que foi cadastrado e sair

para resolver o exercicio, crie pelo menos uma função 
para cada  item do menu

Alen disso, armazene todos os dados em um arquivo de texto
que deve ser salvo em disco e manter os dados cadastrados
-

"""

#*Valida inteiro
def valida_int(pergunta,mim,max):
    """
    Função Vaz um Pergunta que é passada e retoran um numero inteiro
    dentro de um intervalo predefinido
    valida_int(Pergunta,numero minumo=mim, numero Maximo=Max)
    """
    try:
        x = int(input(pergunta))
        while x<mim or x>max:
            x = int(input(pergunta))    
        return x

    except ValueError:
        valida_int(pergunta,mim,max)


#*verifica se o arquivo existe
def existrArquivo(nomeArquivo):
    """
    Função responsalve para localizar o arquivo e 
    retorna se o mesmo existe passar o nome do arquivo corretamente
    """
    try:
        arquivo = open(nomeArquivo, 'rt')#abre o arquivo sigla r para leitura e t para arquivo txt
        arquivo.close()#Fecha o Arquivo
    except FileNotFoundError:
        return False
    else:
        return True 


#*Função responsavel por criar o arquivo caso não exista
def criaArquivo(nomeArquivo):
    try:
        arquivo = open(nomeArquivo, 'wt+') #abre o arquivo sigla w para escrever no Arquivo e Sigla t para arquivos do tipo txt Sigla de + para caso o arquivo não exista
        arquivo.close()
    except:
        print('Erro na Criação do Arquivo')
    else:
        print(f'arquivo {nomeArquivo} foi criado com sucesso!')


#*Função responsavel por cadastrar o jogo e videogame
def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        print('entro1')
        arquivo = open(nomeArquivo, 'at')#Abre o Arquivo Sigla A para esctrever no arquivo e caso ja tenha la não ecrever por cima Letra t Arquivo do tipo txt
        
    except:
        print('erro ao abrir o arquivo')
    else:
        arquivo.write(f'Jogo \033[32m{nomeJogo}\033[m, Video Game \033[35m{nomeVideogame}\033[m\n')#escreve o nome do jogo e o nome do videogame
    finally:    #executa de qualquer maneira para finalizar o arquivo
        arquivo.close()       


#*Função responsavel por Listar os iten da lista
def listarArquivo(nomeArquivo):
    try:
        arquivo=open(nomeArquivo, 'rt')#abre o arquivo sigla r para leitura e t para arquivo txt
    except:
        print('Erro ao ler o arquivo')
    else:
        print(arquivo.read()) #abre o arquivo e mostra na tela as informação  
    finally:    #executa de qualquer maneira para finalizar o arquivo
        arquivo.close()          



arquivo = 'game.txt'
if existrArquivo(arquivo):
    print('Arquivo Localizado')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)    

while True:
    print('----MENU----')
    print('1 - Cadastrar novo item')
    print('2 - Listar Cadrastro')
    print('3 - SAIR')

    op = valida_int('Escolha a opção desejada: ', 1,3)

    if op == 1:
        print('Opção de cadastrar novo Item')
        novo_jogo = input('Informa o None do Jogo; ')
        nome_videogame = input('Informa o Nome do Videogame: ')
        cadastrarJogo(arquivo, novo_jogo, nome_videogame)

    elif op == 2:
        print('Listar Produto')
        listarArquivo(arquivo)

    else:
        print('SAIR')
        break        