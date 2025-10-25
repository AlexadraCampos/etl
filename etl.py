
import pandas as pd

#extrai os dados
dados = pd.read_csv('dados.csv')

#trnasfoma os dados
dados = dados.dropna()  # remove linhas com valores nulos
dados[ 'coluna'] = dados['coluna'].astype(str) 


dados.to_csv('dados_processados.csv', index=False)  # carrega os dados processados