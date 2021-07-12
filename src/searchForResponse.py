import requests
from src.constantes import API_URL

def searchForResponse(url: str, token: str, filePath: str):
    '''
        Mediante a uma token de autorização válida, busca as informações das
        questões na API da Let's Code, e salva num arquivo json. 
    '''


    headers = {
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer ' + token,
        'origin': 'https://class.letscode.com.br',
        'referer': 'https://class.letscode.com.br/',
        'sec-ch-ua': '"Chromium";v="90", "Opera GX";v="76", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.227'
    }

    r = requests.get(
        API_URL + url, headers=headers)

    if('errors' in r.text):
        rJson = r.json()

        erro = [f'Erro! Status {str(rJson["status"])}', rJson["title"]]

        if (rJson['status'] == 400):
            erro.append('Provavelmente a url inserida está incorreta')

        return erro

    if(r.text == ''):
        return ['Erro! Não houve nenhum retorno da consulta', 'Provavelmente você precisa alterar seu token no arquivo altereAqui.py']

    with open(filePath, 'w', encoding='utf-8') as responseFile:
        responseFile.write(r.text)
        return False
