public class Livro {


    private string titulo;
    private string autor;
    private int anoPublicacao;
    private int numPag;
    private double peso;
    private double volume;

    public Livro(titulo, autor, anoPublicacao, numPag, peso, volume) {

        this.titulo = titulo;
        this.autor = autor;
        this.anoPublicacao = anoPublicacao;
        this.numPag = numPag;
        this.peso = peso;
        this.volume = volume;
    }

    public string getTitulo() {
        return titulo;
    }

    public void setTitulo(titulo) {
        this.titulo = titulo;
    }

    public string getAutor() {
        return autor;
    }

    public void setAutor(autor) {
        this.autor = autor;
    }

    public int getAnoPublicacao() {
        return anoPublicacao;
    }

    public void setAnoPublicacao(anoPublicacao) {
        this.anoPublicacao = anoPublicacao;
    }

    public int getNumPag() {
        return numPag;
    }

    public void setNumPag(numPag) {
        this.numPag = numPag;
    }

    public double getPeso() {
        return peso;
    }

    public void setPeso(peso) {
        this.peso = peso;
    }

    public double getVolume() {
        return volume;
    }

    public void setVolume(volume) {
        this.volume = volume;
    }

    public void marcarPagina(numero) {

        if (numero > 0 && numero <= numPag) {
            System.out.println("Livro marcado na página: %d/n", numero);
        } else {
            System.out.println("Página inválida!");
        }
    }
}
