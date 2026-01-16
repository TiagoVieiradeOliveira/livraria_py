import os

def criararq():
    if not os.path.exists("dadosl.txt"):
        with open("dadosl.txt", "w") as arquivo:
            arquivo.write("")
    

def getinfototal(arq):
    names=["Titulo", "Autor", "Paginas", "Data Inicio", "Data Termino"]
    arq=open(arq, "rt")
    for linha in arq:
        dado=linha.split(";")
        for i, tipo in enumerate(dado):
            print(f"{names[i]}: {tipo}")

    arq.close()

def escreverarq(arq, thing):
    arq=open(arq, "at")
    for n, i in enumerate(thing):
        if n==0:
            arq.write(f"{i}")
        else: arq.write(f";{i}")
    arq.write("\n")

    arq.close()


criararq()
getinfototal("dadosl.txt")

