import os
import requests
import shutil
import concurrent.futures
from util import append_file
from scrapper import obter_conteudo_pagina, html_to_md

def obter_nome_unico(path_arquivo):
    try_name = path_arquivo
    i = 1
    while True:
        if os.path.exists(try_name):
            nome_arquivo, extensao = os.path.splitext(path_arquivo)
            try_name = f"{nome_arquivo}({i}){extensao}"
            i+=1
        else:
            break
    
    return try_name

def limpar_titulo(titulo):
    caracteres_ilegais = ':/[]#|?"'
    titulo_limpo = ''.join(c for c in titulo if c not in caracteres_ilegais)
    if titulo_limpo.startswith("_"):
        titulo_limpo = titulo_limpo[1:]
    return titulo_limpo

def replace_all(texto, dict_replace):
    for key, value in dict_replace.items():
        texto = texto.replace("[{"+key+"}]", value)
   
    return texto

def obter_html(url):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.text
        else:
            print('Erro ao fazer a requisição:', response.status_code)
            return None
    except Exception as e:
        append_file("log.txt", f"[obter_html][URL: {url}][EX: {str(e)}]")
        return None

def obter_conteudo_md(html):
    html_content = obter_conteudo_pagina(html)
    return html_to_md(html_content)

def copiar_arquivos(origem, destino):
    if not os.path.exists(destino):
        os.makedirs(destino)

    for arquivo in os.listdir(origem):
        if os.path.isfile(os.path.join(origem, arquivo)):
            caminho_origem = os.path.join(origem, arquivo)
            caminho_destino = os.path.join(destino, arquivo)
            shutil.copyfile(caminho_origem, caminho_destino)

def execute_concurrently(funcao, itens, num_threads=16):
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(funcao, itens)

def execute_foreach(funcao, itens):
    for item in itens:
        funcao(item)