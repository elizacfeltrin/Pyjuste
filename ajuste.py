'''
    Modulo ajuste
    Ajuste de dados pelo método dos minimos quadrados
    
    Funções:
        * reta: determina a reta de melhor ajuste
        
    Consulte também: 
        * grafico.reta
        * relatorio.cria
'''

import numpy as np
import leitura as lt
import grafico as gr
import relatorio as rl

def reta(arquivo, relatorio=None, figura=None, *args, **kwargs):
    '''
        Cálculo da reta de melhor ajuste a dados experimentais
        pelo método dos mínimos quadrados
        
        Argumentos
        - obrigatório:
            * arquivo (str): Nome do arquivo csv com os dados
                o arquivo csv deve conter duas colunas com dados separados por vírgulas. A primeira linha deve conter os rótulos dos dados
        - opcionais:
            * relatorio (str): nome do arquivo para salvar o relatório de cálculo (padrão: None). O relatório é criado pela função relatorio.cria (ver ajuda específica)
            * figura (str): nome do arquivo para salvar o relatório em forma gráfica (padrão: None)
            * args, kwargs: argumentos opcionais a serem fornecidos à função grafico.reta (ver ajuda específica)
    '''
    
    # Entrada de dados
    x, y, rotulos = lt.lerarquivo(arquivo)

    # Ajuste de uma reta
    n = x.size # no. de pontos experimentais
    # size é uma propriedade de arrays
    Sx = x.sum()  # soma de x; .sum() é um método de arrays
    Sy = y.sum()  # soma de y
    Sx2 = Sx * Sx  # (soma de x)²

    Sxy = (x * y).sum()  # soma de xy
    Sxx = (x * x).sum()  # soma de x²

    m = (n * Sxy - Sx * Sy) / (n * Sxx - Sx2)  # coef. linear

    xm = x.mean()  # valor médio dos x; mean() é um método de arrays
    ym = y.mean()  # valor médio dos y; mean() é um método de arrays

    b = ym - m * xm  # coef. const.

    if relatorio != None:
        vars = locals()
        rl.cria(relatorio, vars)

    if figura != None:
        gr.reta(x, y, m, b, figura=figura, rotulos=rotulos, *args, **kwargs)

    return m, b
