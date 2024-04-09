from CriarObsidian import CriarObsidian
from CriarPaginaHtml import CriarPaginaHtml
from SiteDownloader import SiteDownloader
from functions import limpar_titulo
from util import append_file

class Processamento:
    def __init__(self, config):
        img_caminho_saida = config["img_caminho_saida"]
        relatorio_arquivo_imagens = config["relatorio_arquivo_imagens"]
        self.criar_pagina_html = CriarPaginaHtml(config["pagina_html"])
        self.criar_obsidian = CriarObsidian(config["obsidian"])
        self.site_downloader = SiteDownloader(img_caminho_saida, relatorio_arquivo_imagens)

    def processar_post(self, post):
        try:
            post.titulo_limpo = limpar_titulo(post.titulo)
            post.pagina_html = self.site_downloader.baixar_site(post.link)
            print(post.titulo_limpo)
            self.criar_pagina_html.criar_html(post)
            self.criar_obsidian.criar_md(post)
        except Exception as e:
            append_file(f"[main][FILE: {post.titulo_limpo}][EX: {str(e)}]\n")