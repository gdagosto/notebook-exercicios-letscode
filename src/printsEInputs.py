from typing import List

def geraPrint(linhas: List[str], centraliza: bool = False, fechado: bool = False):
    tam = len(max(linhas, key=len)) + 4
    titulo = []

    if (fechado):
        titulo.append('┏' + ('━'*(tam+4)) + '┓')
        titulo.append('┃ ┌' + '─'*tam + '┐ ┃')
    else:
        titulo.append('┃ ┌' + '─'*tam + '┐')

    for l in linhas:
        
        if (centraliza):
            conteudo = l.center(tam, ' ')
        else:
            conteudo = ' ' + l + ' '*(tam-len(l)-1)

        if (fechado):
            titulo.append('┠─┤' + conteudo + '├─┨')
            titulo.append('┃ │' + ' '*tam + '│ ┃')
        else:
            titulo.append('┠─┤' + conteudo + '│')
            titulo.append('┃ │' + ' '*tam + '│')
        

    titulo.pop()
    if (fechado):
        titulo.append('┃ └' + '─'*tam + '┘ ┃')
        titulo.append('┗' + ('━'*(tam+4)) + '┛')
    else:
        titulo.append('┃ └' + '─'*tam + '┘')



    print("\n".join(titulo))

def geraInput(texto = '   >'):
    print('┃')


    res = input('┃ ' + texto + ' ')
    print('┃')
    return res





# ---------------------------------------------------------------------------- #
#                                      OLD                                     #
# ---------------------------------------------------------------------------- #
def geraPrintOld(linhas: List[str], centraliza: bool = False, fechado: bool = False):
    tam = len(max(linhas, key=len)) + 4
    titulo = []

    if (fechado):
        titulo.append('┏' + ('━'*(tam+4)) + '┓')
    titulo.append('┃ ┌' + '─'*tam + '┐ ┃')

    for l in linhas:
        if (centraliza):
            titulo.append('┠─┤' + l.center(tam, ' ') + '├─┨')
        else:
            titulo.append('┠─┤ ' + l + ' '*(tam-len(l)-1) + '├─┨')
        titulo.append('┃ │' + ' '*tam + '│ ┃')

    titulo.pop()
    titulo.append('┃ └' + '─'*tam + '┘ ┃')
    if (fechado):
        titulo.append('┗' + ('━'*(tam+4)) + '┛')

    print("\n".join(titulo))
