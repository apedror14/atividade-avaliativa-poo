from Livro import Livro

livro1 = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 264, 0.4, 1.2)

livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1178, 1.2, 3.5)

print("Título: " + livro1.getTitulo())
print("Ano de publicação: " + str(livro1.getAnoDePublicacao()))
livro1.marcarPagina(50)

print("")

print("Título: " + livro2.getTitulo())
print("Ano de publicação: " + str(livro2.getAnoDePublicacao()))
livro2.marcarPagina(1500) 
