# ---------------------------------------------------------------------------- #
#                                    IMPORTS                                   #
# ---------------------------------------------------------------------------- #
import time
import os

from src.printsEInputs import geraPrint, geraInput
from src.constantes import TITULO, VERSAO, DATA_DE_PUBLICACAO
from src.generateNotebook import generateNotebook
from src.searchForResponse import searchForResponse
# ---------------------------------------------------------------------------- #
#                                     MAIN                                     #
# ---------------------------------------------------------------------------- #
def main():
    geraPrint([TITULO, 'v.' + VERSAO + ' - ' + DATA_DE_PUBLICACAO], centraliza=True)

    token = retornaToken()

    while True:
        geraPrint(['Escolha uma das opções (ou deixe em branco para sair):', '1. Busca dados da API da Let\'s Code', '2. Transforma arquivo response.json em um notebook'])
        res = geraInput()
        if (res == ''):
            break
        elif (res == '1'):
            geraPrint(['Busca os dados da API da Let\'s Code',
                       'Insira o url contendo as questões a serem transformadas abaixo. Exemplos:',
                       'https://class.letscode.com.br/apps/academy/tests/SeuTesteAqui', 'class.letscode.com.br/apps/academy/tests/SeuTesteAqui', 'SeuTesteAqui'])
            url = geraInput()
            retorno = searchForResponse(url.split('/')[-1], token, 'response.json')
            if retorno:
                geraPrint(retorno)
            else:
                geraPrint(['Dados salvos com sucesso no arquivo response.json!'])
            time.sleep(1)
        elif (res == '2'):
            geraPrint(['Transforma arquivo response.json em um notebook', 'Por favor, insira o nome desejado para o notebook (ou deixa em branco para novaAula.ipynb)'])
            arquivo = geraInput()
            generateNotebook(arquivo)
            geraPrint([f'Arquivo {arquivo}.ipynb gerado com sucesso!'])
            time.sleep(1)
        
        
def retornaToken():
    filePath = 'token.txt'
    if (os.path.isfile(filePath)):
        with open(filePath, 'r', encoding='utf-8') as file:
            token = file.readline()
            if token != '':
                return token
    geraPrint(['Insira aqui seu token de autenticação na Let\'s Code. Para obtê-lo:',
                'Caso não saiba como obtê-lo, siga as instruções no arquivo como-obter-meu-token.txt'])
    token = geraInput('Insira seu token: ')
    token = token.replace('"','').replace("'",'')
    
    with open(filePath, 'w', encoding='utf-8') as file:
        
        file.write(token)
        return token
    



# Executa a função principal
main()
