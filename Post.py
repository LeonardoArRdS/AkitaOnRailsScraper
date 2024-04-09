import json
from dataclasses import dataclass
from typing import List

@dataclass
class Tag:
    tagLink: str
    tagText: str

@dataclass
class Post:
    link: str
    titulo: str
    info: str
    tags: List[Tag]
    titulo_limpo: str = ""
    pagina_html: str = ""