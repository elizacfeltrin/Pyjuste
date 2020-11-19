'''
    Relatório de ajuste linear
    Os dados vêm da função ajuste.reta (ver ajuda específica)
    
    Funções:
        * cria: cria relatório do ajuste
        
    Consulte a ajuda específica
'''

def cria(arquivo, dados):
    '''
        Relatório de ajuste linear
        Os dados vêm da função ajuste.reta (ver ajuda específica) e a função cria_relatorio é chamada a partir dela
        
        Argumentos:
        - obrigatórios:
            * arquivo (str): nome do arquivo para salvar o relatório
            * dados (dict): dados para a criação do relatório
    '''

    with open(arquivo, 'w') as arq:  
        # 'w': write (escrever) em arquivo. 
        # se arquivo existir, será sobrescrito!

        arq.write(' Relatório do ajuste '.center(60, '#')+'\n')
        arq.write(f'Arquivo: {dados["arquivo"]}\n')
        arq.write(f'Rótulos: {dados["rotulos"]}\n')
        arq.write(f'Número de pontos: {dados["n"]}\n')
        arq.write(f'Soma dos valores de x (Sx): {dados["Sx"]}\n')
        arq.write(f'Soma dos valores de y (Sy): {dados["Sy"]}\n')
        arq.write(f'Soma dos valores de x² (Sxx): {dados["Sxx"]}\n')
        arq.write(f'Soma dos valores de x*y (Sxy): {dados["Sxy"]}\n')
        arq.write(f'Média dos valores de x (xm): {dados["xm"]}\n')
        arq.write(f'Média dos valores de y (ym): {dados["ym"]}\n')
        
        eq_reta = f'y = {dados["m"]:.3f} x + {dados["b"]:.3f}'
        
        arq.write(f'Equação da reta de melhor ajuste: {eq_reta}\n')
        arq.write('#'*60+'\n')
