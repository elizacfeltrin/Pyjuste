import numpy as np
import ajuste

# Este é o arquivo de interface com o usuário

# Ajuste de reta a dados de arquivo csv
m, b = ajuste.reta('dados-linear.csv')

help(ajuste)

print(m, b)
