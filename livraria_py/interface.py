from customtkinter import *
from livro import *
from imagens import getCapa

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

#widgets

        self.barra=Frame(self, 0, 60, "#395cfa")
        self.barra.grid(row=0, column=0,columnspan=2 , sticky="ew", padx=10, pady=10)

        

        self.area_livros=Frame(self, 0, 0, "#ffffff")
        self.area_livros.grid(row=1, column=0, sticky="nsew", padx=(10, 5), pady=10)

        self.visor=Frame(self, 0, 0, "#2600cc")
        self.visor.grid(row=1, column=1, sticky="nsew", padx=(5, 10), pady=10)
#configurações dos widgets

        self.grid_rowconfigure(1, weight=1)   

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)

        self.area_livros.grid_rowconfigure(1, weight=1)
        self.area_livros.grid_columnconfigure(0, weight=1)

        self.visor.grid_rowconfigure(1, weight=1)
        self.visor.grid_columnconfigure(1, weight=1)

        self.livro_frame=Frame(self.area_livros, 240, 400, "#4f43dd")
        self.livro_frame.grid_propagate(False)

        self.livro_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")

        self.texto=Label(self.livro_frame, getCapa("O Mágico de Oz"), None, None)
        self.texto.grid(row=0, column=0, padx=10, pady=10)

        self.texto2=Label(self.livro_frame, None, texto="O Mágico de Oz", cor="#ffffff")
        self.texto2.grid(row=1, column=0, padx=10, pady=10)



app=App()
app.mainloop()