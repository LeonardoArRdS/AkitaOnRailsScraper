import os
import requests
from util import append_file
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, unquote
from functions import obter_nome_unico, execute_concurrently

class ImagemInfo:
    def __init__(self, img_url, img_filename):
        self.img_url = img_url
        self.img_filename = img_filename

class SiteDownloader:
    def __init__(self, img_download_path, saida_arquivo_imagens):
        self.img_download_path = img_download_path
        self.saida_arquivo_imagens = saida_arquivo_imagens
        os.makedirs(self.img_download_path, exist_ok=True)
        self.lista_imagem_info = []

    def baixar_site(self, url):
        try:
            response = requests.get(url)
            
            if response.status_code == 200:
                html_content = response.text
                self.registrar_imagens(url, html_content)
                return html_content
            else:
                return None
        except Exception:
            return None
    
    def registrar_imagens(self, url, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        img_tags = soup.find_all('img')
        
        for img_tag in img_tags:
            img_src = img_tag['src']
            if str(img_src).startswith("http"):
                img_url = img_src
            else:
                img_url = urljoin(url, img_src)
            
            img_filename = os.path.basename(unquote(urlparse(img_url).path))
            self.lista_imagem_info.append(ImagemInfo(img_url, img_filename))
    
    def relatorio_imagens(self):
        saida = "\n".join(f'"{imgInfo.img_url};{imgInfo.img_filename}' for imgInfo in self.lista_imagem_info)
        open(self.saida_arquivo_imagens, "w", encoding="utf-8").write(saida)
    
    def baixar_imagem(self, imgInfo):
        img_data = requests.get(imgInfo.img_url).content
        img_path = os.path.join(self.img_download_path, imgInfo.img_filename)
            
        img_path = obter_nome_unico(img_path)
        with open(img_path, 'wb') as img_file:
            img_file.write(img_data)

    def baixar_imagens(self):
        execute_concurrently(self.baixar_imagem, self.lista_imagem_info)
        
    def minha_funcao(self, imgInfo):
        img_data = requests.get(imgInfo.img_url).content
        img_path = os.path.join(self.img_download_path, imgInfo.img_filename)
            
        img_path = obter_nome_unico(img_path)
        with open(img_path, 'wb') as img_file:
            img_file.write(img_data)
