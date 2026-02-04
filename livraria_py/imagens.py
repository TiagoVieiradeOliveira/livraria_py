import requests
from PIL import Image
from io import BytesIO
from customtkinter import CTkImage

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
    



def getCapa(titulo):
    capa=buscar_capa(titulo)


    if not capa: 
        img=Image.open("imagens/livro_nao_encontrado.webp")   
        return CTkImage(light_image=img, size=(145, 300)) 
    else:
        img=(baixarImagem(capa))
        return formatarImagem(img, 145, 300)
    
print(getCapa("Jogoas Vorazes"))
img=Image.open("imagens/livro_nao_encontrado.webp")   
sem_capa=CTkImage(light_image=img, size=(145, 300)) 