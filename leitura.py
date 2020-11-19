'''
  Funções para ler dados de arquivos csv
  
  Funções:
    * lerarquivo_np: ler usando numpy.genfromtxt
    * lerarquivo: ler usando pandas
    
    Consulte a ajuda específica
'''

import numpy as np
import pandas as pd

def lerarquivo_np(nomearq):
    '''
        Ler um arquivo de texto com dados separado por vírgulas
        e pulando a primeira linha
        usando numpy.genfromtxt()
        
        Argumentos:
        - obrigatórios:
            * nomearq (str): nome do arquivo a ser lido
    '''
    x, y = np.genfromtxt(nomearq, delimiter=',', skip_header=1, unpack=True)
    return x, y


def lerarquivo(nomearq):
    '''
        Ler um arquivo de texto com dados separado por vírgulas
        e pulando a primeira linha
        usando pandas.read_csv()
        
        Argumentos:
        - obrigatórios:
            * nomearq (str): nome do arquivo a ser lido
    '''
    dados = pd.read_csv(nomearq, comment='#')
    rotulos = dados.columns.values  # extrai os rótulos das colunas
    x, y = dados[rotulos[0]], dados[rotulos[1]]  # salvando os valores das colunas
    return x, y, rotulos
