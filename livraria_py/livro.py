from gerenciar import *



class Livro:
    def __init__(self, titulo, autor, paginas, data_inicio, data_termino, arq):
        self.titulo=titulo
        self.autor=autor
        self.paginas=paginas
        self.data_inicio=data_inicio
        self.data_termino=data_termino
        self.arq=arq
        
    def getTitulo(self):

        return self.titulo
    
    def getDados(self):
        dados=[self.titulo, self.autor, self.paginas, self.data_inicio, self.data_termino]

        return dados
    

class Acervo:
    def __init__(self, arq):
        self.arq=arq

    def adicionarLivro(self, dados):
        escreverarq(self.arq, dados)

        return f"Livro {dados[0]} Adicionado com sucesso"
                
    def removerLivro(self, livro):
        livros=converter(self.arq)
        for i, l in enumerate(livros):
            if livro == l[0]:
                del livros[i]

        reescreverarq(self.arq, livros)

        return f"Livro {livro} removido com sucesso"

    def pesquisarLivro(self, titulo):
        livros=converter(self.arq)
        controle=0
        for l in livros:
            if l[0].strip().upper() == titulo.upper().strip():
                mostrarLivro(l)
                controle+=1

        if controle==0:        
            print("Livro não encontrado")

    def visualizarAcervo(self):
        livros=converter(self.arq)
        print("-=-"*50)
        for l in livros:
            print(f"Livro: {l[0]:^60}")


    def visualizarLivro(self, livro):
        mostrarLivro(livro)

a=Acervo("livros.txt")
a.visualizarAcervo()
