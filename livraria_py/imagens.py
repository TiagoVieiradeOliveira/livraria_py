import requests
from PIL import Image
from io import BytesIO
import os
from customtkinter import CTkImage
import re 

CACHE_DIR = "cache_capas"
os.makedirs(CACHE_DIR, exist_ok=True)

PLACEHOLDER = "imagens/livro_nao_encontrado.webp"



def buscar_capa(titulo):
    url="https://openlibrary.org/search.json"

    params={
        "q": titulo,
        "limit": 20
    } 

    resposta=requests.get(url, params=params, timeout=10)

    if resposta.status_code!=200: return None

    dados=resposta.json()

    for livro in dados.get("docs", []):
        cover_id = livro.get("cover_i")
        if cover_id:
            return f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"

    return None

def baixarImagem(url):
    resposta=requests.get(url, timeout=10)
    
    return Image.open(BytesIO(resposta.content))


def formatarImagem(img, lar, alt):
    img_red=img.resize((lar, alt))
    
    return CTkImage(light_image=img_red, size=(lar, alt))
    
def normalizar(texto):
    return re.sub(r"[^a-z0-9]+", "_", texto.lower()).strip("_")


def getCapa(titulo):
    nome = normalizar(titulo) + ".jpg"
    path = os.path.join(CACHE_DIR, nome)

    # 👉 se já existe: carrega local
    if os.path.exists(path):
        img = Image.open(path)
        return formatarImagem(img, 145, 300)

    # 👉 buscar online
    url = buscar_capa(titulo)

    if not url:
        img = Image.open(PLACEHOLDER)
        return formatarImagem(img, 145, 300)

    try:
        resposta = requests.get(url, timeout=10)
        img = Image.open(BytesIO(resposta.content))
        img.save(path)
        return formatarImagem(img, 145, 300)

    except Exception:
        img = Image.open(PLACEHOLDER)
        return formatarImagem(img, 145, 300)
    


