import os

def criararq():
    try:
        if not os.path.exists("livros.txt"):
            with open("livros.txt", "w") as arquivo:
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
        arq=open(arq, "at")
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
        arq=open(arq, "w")
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
        arq=open(arq, "rt")
        for linha in arq:
            for dado in linha.split(";"):
                dados_conv.append(dado)
            arq_conv.append(dados_conv)
            dados_conv=[]
    except OSError as erro:
        print(f"Erro ao abrir o arquivo {erro}")
    arq.close()

    return arq_conv

    

criararq()

