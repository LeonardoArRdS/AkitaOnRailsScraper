
from Processamento import Processamento
from Post import Post, Tag

from util import read_json
from functions import execute_foreach, execute_concurrently

config = read_json("in/config.json")
processamento = Processamento(config)
posts = [Post(post["link"], post["titulo"], post["info"], [Tag(**tag) for tag in post["tags"]]) for post in read_json(config["caminho_dados"])]

execute_concurrently(processamento.processar_post, posts)

processamento.criar_obsidian.criar_sumario()
processamento.site_downloader.relatorio_imagens()
processamento.site_downloader.baixar_imagens()