from customtkinter import *
from livro import *
from imagens import getCapa
from imagens import formatarImagem
from gerenciar import *
import os

class Label(CTkLabel):
    def __init__(self, master, img=None, texto=None, cor=None, w=220):
        self.img=img
        self.texto=texto
        self.cor=cor
        self.w=w
        super().__init__(master,
                         image=self.img,
                         text=self.texto,
                         text_color="#ffffff",
                         font=("Open Sans", 18, "bold"),
                         wraplength=self.w)

class MaisInfo(CTkButton):
    def __init__(self, master, app, img=None, livro=None, frame_dados=None, frame_capas=None, img_original=None):
        self.img=img
        self.app=app
        self.livro=livro
        self.frame1=frame_dados
        self.frame2=frame_capas
        self.original=img_original
        super().__init__(master,
                         width=150,
                         height=310,
                         image=self.img,
                         fg_color="#FAD52A",
                         hover_color="#CAAB1F",
                         text="",
                         command=self.acao)
        
    def acao(self):
        self.app.livro_ativo= self
        for widget in self.frame1.winfo_children():
            widget.destroy()

        cont=10
        names=["Título:", "Autor:", "Páginas:", "Início:", "Término:"]
        for i, dado in enumerate(self.livro):
            info = Label(self.frame1,texto=dado, w=300)
            param= Label(self.frame1, texto=names[i])
            info.place(x=150, y=cont)
            param.place(x=20, y=cont)
            cont+=50


#imagem no visor
        self.desenharImagem()
    def desenharImagem(self):

        visor = self.frame2
        visor.update_idletasks()

        lar = visor.winfo_width()
        alt = visor.winfo_height()

        if lar < 100 or alt < 100:
            lar = visor.winfo_reqwidth()
            alt = visor.winfo_reqheight()

        if lar >= 360 and alt >= 520:
            img = self.original
        else:
            img = self.img

        # cria uma vez
        if not hasattr(self.app, "label_imagem_visor") or self.app.label_imagem_visor is None:

            self.app.label_imagem_visor = Label(
                visor,
                img=img
            )
            self.app.label_imagem_visor.place(relx=20, y=40)

        else:
            self.app.label_imagem_visor.configure(image=img)
            self.app.label_imagem_visor.img = img

        


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
        self.cache_imagens={}
        self.cache_imagens_visor={}
        self.livro_ativo=None
        self._resize_job = None
        self.label_imagem_visor=None
        self.telaInicial()
     

#widgets principais

    def telaInicial(self):
        self.barra=Frame(self, 0, 60, "#395cfa")
        self.barra.grid(row=0, column=0,columnspan=2 , sticky="ew", padx=10, pady=10)

        

        self.area_livros = CTkScrollableFrame(self,fg_color="#ffffff", scrollbar_button_color="#395cfa", scrollbar_button_hover_color="#2600cc")
        self.area_livros.grid(row=1, column=0, sticky="nsew", padx=(10, 5), pady=10)

        self.visor=Frame(self, 30, 0, "#2600cc")
        self.visor.grid_propagate(False)
        self.visor.grid(row=1, column=1, sticky="nsew", padx=(5, 10), pady=10)

        self.dados=Frame(self.visor, 450, 250, "#395cfa")
        self.dados.grid(row=1, column=1, sticky="se", padx=10, pady=10)

        self.imgs_visor=Frame(self.visor, 0, 0, "#395cfa")
        self.imgs_visor.grid(row=0, column=1, sticky="nsew", padx=(10), pady=10)
#resonsividade dos widgets

        self.grid_rowconfigure(1, weight=1)   

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)

        self.visor.grid_rowconfigure(0, weight=1)
        self.visor.grid_columnconfigure(1, weight=0)

        self.dados.grid_rowconfigure(1, weight=1)
        self.dados.grid_columnconfigure(1, weight=1)

        self.imgs_visor.grid_rowconfigure(1, weight=1)
        self.imgs_visor.grid_columnconfigure(1, weight=1)

        self.reorganizarCards()
        self.bind("<Configure>", self.reorganizarTela)
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

        self.after(80, lambda:self.renderizarCards(novas_colunas))

    def reorganizarTela(self, event=None):

        if self._resize_job:
            self.after_cancel(self._resize_job)

        self._resize_job = self.after(150, self._aplicarResize)

    def _aplicarResize(self):

        self.reorganizarCards()

        if self.livro_ativo and self.livro_ativo.winfo_exists():
            self.livro_ativo.desenharImagem()

    def renderizarCards(self, colunas):
        self.livro_ativo=None

        for widget in self.area_livros.winfo_children():
            widget.destroy()

        livros=converter("livros.txt")
        coluna=line=0



        for i, livro in enumerate(livros):

            self.livro_frame=Frame(self.area_livros, 240, 400, "#4f43dd")
            self.livro_frame.grid_rowconfigure(0, weight=1)
            self.livro_frame.grid_rowconfigure(1, weight=3)

            self.livro_frame.grid_columnconfigure(0, weight=1)
            self.livro_frame.grid_propagate(False)

            self.livro_frame.grid(row=line, column=coluna, padx=25, pady=20, sticky="nw")

            coluna+=1
            
            if coluna>=colunas:
                line+=1
                coluna=0

            self.texto2=Label(self.livro_frame, None, texto=livro[0], cor="#ffffff")
            self.texto2.grid(row=0, column=0, padx=10, pady=10, sticky="n")

            if livro[0] not in self.cache_imagens:
                self.cache_imagens[livro[0]]=getCapa(livro[0])
                self.cache_imagens_visor[livro[0]]=getCapa(livro[0], 300, 450)

            img=self.cache_imagens[livro[0]]
            img_visor=self.cache_imagens_visor[livro[0]]
            self.mais_info=MaisInfo(master=self.livro_frame,app=self, img=img, livro=livro, frame_dados=self.dados, frame_capas=self.imgs_visor, img_original=img_visor)
            self.mais_info.grid(row=1, column=0, padx=10, pady=10, sticky="n")

        
app=App()
app.mainloop()