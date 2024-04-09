import os
from functions import limpar_titulo

class CriarPaginaHtml:
    def __init__(self, pagina_html_config):
        self.caminho_saida = pagina_html_config["caminho_saida"]
        os.makedirs(self.caminho_saida, exist_ok=True)

    def criar_html(self, post):
        caminho_arquivo = os.path.join(self.caminho_saida, f"{post.titulo_limpo}.html")
        open(caminho_arquivo, "w", encoding="utf-8").write(post.pagina_html)