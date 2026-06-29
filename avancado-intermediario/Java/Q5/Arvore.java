public class Arvore extends Objeto {

    private double altura;

    public Arvore(double altura) {
        this(altura, 0.0, 0.0);
    }

    public Arvore(double altura, double x, double y) {
        super(x, y);
        this.altura = altura;
    }

    public double getAltura() {
        return altura;
    }

    @Override
    public String toString() {
        return super.toString() +
               "Altura = " + altura;
    }
}

