public class Veiculo extends Objeto implements Movimento {

    private String cor;

    public Veiculo(String cor) {
        this(cor, 0.0, 0.0);
    }

    public Veiculo(String cor, double x, double y) {
        super(x, y);
        this.cor = cor;
    }

    public String getCor() {
        return cor;
    }

    @Override
    public void mover(double x, double y) {
        setX(x);
        setY(y);
    }

    @Override
    public String toString() {
        return super.toString() +
               "Cor = " + cor;
    }
}
