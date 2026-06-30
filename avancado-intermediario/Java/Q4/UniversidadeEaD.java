public class UniversidadeEaD extends Universidade{
    private String urlPlataforma;

    public UniversidadeEaD(String nome, String urlPlataforma){
        super(nome);
        this.urlPlataforma = urlPlataforma;
    }

    public String getUrlPlataforma(){
        return this.urlPlataforma;
    }

    public void setUrlPlataforma(String urlPlataforma){
        this.urlPlataforma = urlPlataforma;
    }

    public void aplicarAvaliacao(){
        System.out.println("Avaliações Online na " + getUrlPlataforma());
    }

    @Override
    public String toString() {
        return super.toString() + " (EaD) | Plataforma: " + urlPlataforma;
    }
}