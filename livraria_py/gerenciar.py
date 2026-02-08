import os

def criararq(nome):
    try:
        if not os.path.exists(nome):
            with open(nome, "w", encoding="utf-8") as arquivo:
                arquivo.write("")
        return True
    except OSError as erro:
        print(f"Erro ao abrir o arquivo {erro}") 
        return False


def getinfototal(arq):
    names=["Titulo", "Autor", "Paginas", "Data Inicio", "Data Termino"]
    try:
        livros=converter(arq)
        for livro in livros:
            for i, dado in enumerate(livro):
                print(f"{names[i]}: {dado}")

    except OSError as erro:
        print(f"Erro ao abrir o arquivo {erro}")

    except FileNotFoundError:
        print("Arquivo não encontrado")

    except IndexError:
        print("Erro nos dados do arquivo")


def escreverarq(arq, dados):
    try:
        arq=open(arq, "at", encoding="utf-8")
        for n, i in enumerate(dados):
            if n==0:
                arq.write(f"{i}")
            else: arq.write(f";{i}")
        arq.write("\n")

    except OSError as erro:
        print(f"Erro ao abrir o arquivo {erro}")
    arq.close()


def reescreverarq(arq, lista):
    try:
        arq=open(arq, "w", encoding="utf-8")
        for l in lista:
            for n, i in enumerate(l):
                if n==0:
                    arq.write(f"{i}")
                else:
                    arq.write(f";{i}")
    except OSError as erro:
        print(f"Erro ao abrir o arquivo {erro}")
    arq.close()


def converter(arq):
    dados_conv=[]
    arq_conv=[]
    try:
        arq=open(arq, "rt", encoding="utf-8")
        for linha in arq:
            for dado in linha.split(";"):
                dados_conv.append(dado)
            arq_conv.append(dados_conv)
            dados_conv=[]
    except OSError as erro:
        print(f"Erro ao abrir o arquivo {erro}")
    arq.close()

    return arq_conv


def mostrarLivro(livro):
    print("-=-"*20)
    print(f"{livro[0]:^60}")
    print("-=-"*20)

    names=["Titulo:", "Autor:", "Paginas:", "Data Inicio:", "Data Termino:"]
    str_dados=[]
    for i, dado in enumerate(livro):    
        str_dados.append(f" {dado}")

    str_livro=f"{str_dados[0]} {str_dados[1]} {str_dados[2]} {str_dados[3]} {str_dados[4]}"

    return str_livro

