public class Personagem extends Objeto implements Movimento {

    private String nome;

    public Personagem(String nome) {
        this(nome, 0.0, 0.0);
    }

    public Personagem(String nome, double x, double y) {
        super(x, y);
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    @Override
    public void mover(double x, double y) {
        setX(x);
        setY(y);
    }

    @Override
    public String toString() {
        return super.toString() +
               "Nome = " + nome;
    }
}
