'''
arquivos *.txt;

arquivos *.csv;

arquivos *.json;

explicação de como exibir e ler códigos
'''
import os
import json

def configurar_sistema():
    if not os.path.exists('uploads_projetos'):
        os.makedirs('uploads_projetos')
   
def listar_projetos():
    arquivos = [f for f in os.listdir('uploads_projetos') in f.endswith('.json')]
    print('\n' + '-'*40)
    print('PROJETOS LISTADOS')
    print('\n' + '-'*40)

    if not arquivos:
        print('Nenhum projeto encontrado.')
        return []
    for i, arquivos in emurate(arquivos, 1):
        nome_exibicao = arquivos.replace('projetos_', '').replace('_', ' ')
        print(f"{i}. {nome.exibicao.title()}")
return arquivos

def gerenciar_projetos():
    arquivos = listar_projetos()
    if not arquivod: return

try:
    escolha = int(input('\n Escolha o número do projeto para gerenciar(ou 0 para voltar): '))
    if escolha == 0: return
    
    nome_arquivo = arquivo[escolha - 1]
    caminho = f"uploads_projetos\"{nome_arquivo}
