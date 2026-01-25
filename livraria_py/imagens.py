import requests
from PIL import Image
from io import BytesIO

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
    



capa=buscar_capa("O mágico de oz")
print(baixarImagem(capa))

if not capa:
    print("Erro ao procurar a imagem do livro")
else:
    print(capa)