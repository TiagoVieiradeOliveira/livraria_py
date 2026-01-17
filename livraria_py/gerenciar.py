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
        arq=open(arq, "rt")
        for linha in arq:
            dado=linha.split(";")
            for i, tipo in enumerate(dado):
                print(f"{names[i]}: {tipo}")

    except OSError as erro:
        print(f"Erro ao abrir o arquivo {erro}")

    except FileNotFoundError:
        print("Arquivo não encontrado")

    except IndexError:
        print("Erro nos dados do arquivo")

    arq.close()


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


def converter(arq):
    dados_conv=[]
    arq_conv=[]
    arq=open(arq, "rt")
    for linha in arq:
        for dado in linha.split(";"):
            dados_conv.append(dado)
        arq_conv.append(dados_conv)
        dados_conv=[]
    
    return arq_conv



criararq()

print(converter("livros.txt"))
