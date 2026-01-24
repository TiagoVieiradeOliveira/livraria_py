def mostrarLivro(livro):
    print("-=-"*20)
    print(f"{livro[0]:^60}")
    print("-=-"*20)

    names=["Titulo:", "Autor:", "Paginas:", "Data Inicio:", "Data Termino:"]
    for i, dado in enumerate(livro):
                print(f"{names[i]:<15} {dado:^50}")

livro=["Jogos vorazes Circulo de fogo", "nao sei", "123", "23/10/2013", "23/10/2023"]
