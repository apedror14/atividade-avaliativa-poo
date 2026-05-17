public class Livro {


    private String titulo;
    private String autor;
    private int anoPublicacao;
    private int numPag;
    private double peso;
    private double volume;

    public Livro(String titulo,String autor,int anoPublicacao,int numPag,double peso,double volume) {

        this.titulo = titulo;
        this.autor = autor;
        this.anoPublicacao = anoPublicacao;
        this.numPag = numPag;
        this.peso = peso;
        this.volume = volume;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public int getAnoPublicacao() {
        return anoPublicacao;
    }

    public void setAnoPublicacao(int anoPublicacao) {
        this.anoPublicacao = anoPublicacao;
    }

    public int getNumPag() {
        return numPag;
    }

    public void setNumPag(int numPag) {
        this.numPag = numPag;
    }

    public double getPeso() {
        return peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public double getVolume() {
        return volume;
    }

    public void setVolume(double volume) {
        this.volume = volume;
    }

    public void marcarPagina( int numero) {

        if (numero > 0 && numero <= numPag) {
            System.out.println("Livro marcado na página: " + numero);
        } else {
            System.out.println("Página inválida!");
        }
    }
}
