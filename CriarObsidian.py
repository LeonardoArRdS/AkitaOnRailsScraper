import os
from functions import obter_conteudo_md, replace_all
from util import read_file

class CriarObsidian:
    def __init__(self, obsidian_config):
        self.caminho_saida = obsidian_config["caminho_saida"]
        os.makedirs(self.caminho_saida, exist_ok=True)
        self.template = read_file(obsidian_config["caminho_template"])
        self.sumario_saida = obsidian_config["sumario_saida"]
        self.titulos_sumario = []

    def criar_md(self, post):
        tags = " ".join([f"#{tag.tagText}" for tag in post.tags])
        tag_links = "\n".join([f"[{tag.tagText}]({tag.tagLink})" for tag in post.tags])
        conteudo = obter_conteudo_md(post.pagina_html)

        dict_replace = {
            "link" : post.link,
            "titulo" : post.titulo,
            "info" : post.info,
            "tags" : tags,
            "tag_links" : tag_links,
            "conteudo" : conteudo
        }

        path = os.path.join(self.caminho_saida, f"{post.titulo_limpo}.md")
        saida = replace_all(self.template, dict_replace)

        self.titulos_sumario.append(post.titulo_limpo)
        open(path, "w", encoding="utf-8").write(saida)

    def criar_sumario(self):
        saida = "\n".join([f"[[{titulo}]]" for titulo in self.titulos_sumario])
        open(self.sumario_saida, "w", encoding="utf-8").write(saida)