from customtkinter import *
from livro import *
from imagens import getCapa
from imagens import sem_capa
from gerenciar import *
import os

class Label(CTkLabel):
    def __init__(self, master, img=None, texto=None, cor=None):
        self.img=img
        self.texto=texto
        self.cor=cor
        super().__init__(master,
                         image=self.img,
                         text=self.texto,
                         text_color="#ffffff")


class Frame(CTkFrame):
    def __init__(self, master, lar, alt, cor):
        self.lar=lar
        self.alt=alt
        self.cor=cor
        super().__init__(master,
                         width=self.lar,
                         height=self.alt,
                         fg_color=self.cor)
    def configTexto(self, texto):
        texto.grid(row=0, column=0, sticky="nsew")



class App(CTk):
    def __init__(self, fg_color = "#eaebe0", **kwargs):
        super().__init__(fg_color, **kwargs)

        self.title("Livraria")
        self.geometry("1366x768")
        set_appearance_mode("System")

        self.iconbitmap("imagens/icone_livro.ico")

#config
        self.acervo=Acervo("livros.txt")
        self.telaInicial()
     
        

#widgets principais

    def telaInicial(self):
        self.barra=Frame(self, 0, 60, "#395cfa")
        self.barra.grid(row=0, column=0,columnspan=2 , sticky="ew", padx=10, pady=10)

        

        self.area_livros = CTkScrollableFrame(self,fg_color="#ffffff", scrollbar_button_color="#395cfa", scrollbar_button_hover_color="#2600cc")
        self.area_livros.grid(row=1, column=0, sticky="nsew", padx=(10, 5), pady=10)

        self.visor=Frame(self, 0, 0, "#2600cc")
        self.visor.grid(row=1, column=1, sticky="nsew", padx=(5, 10), pady=10)
#resonsividade dos widgets

        self.grid_rowconfigure(1, weight=1)   

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)

        # self.area_livros.grid_rowconfigure(1, weight=1)
        # self.area_livros.grid_columnconfigure(0, weight=1)

        self.visor.grid_rowconfigure(1, weight=1)
        self.visor.grid_columnconfigure(1, weight=1)

        self.reorganizarCards()
        self.bind("<Configure>", self.reorganizarCards)
#elementos
    def reorganizarCards(self, event=None):

        self.area_livros.update_idletasks()
        largura = self.area_livros.winfo_width()

        if largura < 50:
            return

        card_lar = 260
        novas_colunas = max(1, largura // card_lar)

        # só redesenha se mudou
        if getattr(self, "_colunas_atuais", None) == novas_colunas:
            return

        self._colunas_atuais = novas_colunas
        self.renderizarCards(novas_colunas)

    
    def renderizarCards(self, colunas):

        for widget in self.area_livros.winfo_children():
            widget.destroy()

        livros=converter("livros.txt")
        coluna=line=0



        for i, livro in enumerate(livros):

            self.livro_frame=Frame(self.area_livros, 240, 400, "#4f43dd")
            self.livro_frame.grid_propagate(False)

            self.livro_frame.grid(row=line, column=coluna, padx=25, pady=20, sticky="nw")

            coluna+=1
            
            if coluna>=colunas:
                line+=1
                coluna=0

            self.texto2=Label(self.livro_frame, None, texto=livro[0], cor="#ffffff")
            self.texto2.grid(row=0, column=0, padx=10, pady=10)
            
            self.texto=Label(self.livro_frame, sem_capa, None, None)
            self.texto.grid(row=1, column=0, padx=10, pady=10)


    # def renderizarCapas(self):
    #     criararq("capas.txt")
    #     if not os.path.exists ("capas.txt"):
    #         capas=[]
    #         livros=converter("livros.txt")
    #         for livro in livros:
    #             capas.append(getCapa(livro[0]))
    #         with open("capas.txt", "w") as arquivo:
    #             for capa in capas:
    #                 arquivo.write(f"{capa}")
    #                 arquivo.write(f"\n")





app=App()
app.mainloop()