public class UniversidadeFisica extends Universidade{
    private String campus;

    public UniversidadeFisica(String nome, String campus){
        super(nome);
        this.campus = campus;
    }

    public String getCampus(){
        return this.campus;
    }

    public void setCampus(String campus){
        this.campus = campus;
    }

    public void aplicarAvaliacao(){
        System.out.println("Avaliações presenciais no campus " + getCampus());
    }

    @Override
    public String toString() {
        return super.toString() + " (Física) | Campus: " + campus;
    }
}