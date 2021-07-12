import json
import nbformat as nbf

def generateNotebook(filePath: str = 'novaAula') -> None:
    '''
        A partir de um arquivo json, gera um notebook novaAula.ipynb contendo 
        todas as questões e blocos de código em branco
    '''

    if filePath == '':
        filePath = 'novaAula'

    with open('response.json', encoding="utf8") as jsonFile:
        questoes = json.load(jsonFile)['questions']
        enunciados = [q['title'] for q in questoes]

    nb = nbf.v4.new_notebook()

    cells = []

    for i, v in enumerate(enunciados):
        cells.append(nbf.v4.new_markdown_cell(
            f'<hr>\n\n## Questão {i+1}\n\n{v}'))
        cells.append(nbf.v4.new_code_cell())

    nb['cells'] = cells

    nbf.write(nb, filePath + '.ipynb')
