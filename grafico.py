'''
  Modulo grafico
  
  Gráfico dos dados experimentais 
  e da reta de melhor ajuste
  
  funções:
    * reta: cria um relatório gráfico do ajuste linear
'''


import numpy as np
import matplotlib.pyplot as plt

def reta(x, y, m, b, figura='ajuste.png', titulo=None, simbolo='.r', linha='-b', rotulos=['x', 'y'], grid=False, rotulo_dados='dados experimentais', rotulo_linha='ajuste linear', mostra=False):
    '''
        plotreta(x, y, m, b, titulo, simbolo, rotulos, grid)
        exibe gráfico dos dados experimentais e da reta de melhor ajuste
      
        Argumentos:
        - obrigatórios:
            * x (array): array com od dados da variável indepentente
            * y (array): array com od dados da variável depentente
            * m (float): coeficiente linear da reta
            * b (float): coeficiente constante da reta
        - opcionais:
            * figura (str): nome da figura a ser salva (padrão: 'ajuste.png')
            * titulo: titulo do gráfico (padrão: None)
            * grid (bool): exibe linhas auxiliares no gráfico (padrão: False)
            * simbolo (str): símbolo para os pontos em notação do matplotlib (padrão:   '.r')
            * linha (str): estilo da linha em notação do matplotlib (padrão: '-b')
            * rotulos (str): lista com os rótulos dos eixos (padrão: ['x', 'y'])
            * rotulo_dados (str): rótulo a ser exibido na legenda para os pontos (padrão: 'dados experimentais')
            * rotulo_linha (str): rótulo a ser exibido na legenda para a reta de ajuste (padrão: 'ajuste linear')
            * mostra (bool): Mostra ou não a janela gráfica (padrão: False)
    '''

    eq_reta = f'y = {m:.3f} x + {b:.3f}'

    xr = np.array([x.min(), x.max()])  # .min() e .max() são métodos de arrays
    yr = m * xr + b
  
    # Gráfico
    plt.figure()

    ax = plt.axes()
  
    if titulo != None:
        plt.title(titulo)
  
    plt.xlabel(rotulos[0])
    plt.ylabel(rotulos[1])
    
    plt.plot(x, y, simbolo, label=rotulo_dados)
    plt.plot(xr, yr, linha, label=rotulo_linha)
    
    ax.text(.7, .05, eq_reta, transform=ax.transAxes)
    
    plt.legend()
  
    if grid:
        plt.grid()

    plt.savefig(figura, bbox_inches='tight')
    
    if mostra:
        plt.show()
