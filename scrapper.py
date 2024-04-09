from util import append_file
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, unquote
import html2text

def obter_conteudo_pagina(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        div_text = soup.find('div', class_='excerpt')
        div_text2 = soup.find('div', class_='text')
        last_h4_tags = div_text2.find_all('h4')[-1]
        last_h4_tags.extract()
        if div_text:
            div_html = div_text.prettify()
            div_html += div_text2.prettify()
            return div_html
        else:
            return None
    except Exception as e:
        append_file("log.txt", f"[obter_conteudo_pagina][EX: {str(e)}]")
        return None

def html_to_md(html_content):
    converter = html2text.HTML2Text()

    converter.body_width = 0
    converter.ignore_images = False
    converter.ignore_links = False

    markdown_content = converter.handle(html_content)
    return markdown_content