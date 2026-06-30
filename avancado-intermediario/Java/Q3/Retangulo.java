public class Retangulo extends Figura {
    private double base;
    private double altura;

    public Retangulo(double x, double y, double base, double altura) {
        super(x, y);
        System.out.println("Criando retângulo");
        this.base = base;
        this.altura = altura;
    }

    @Override
    public void desenhar() {
        System.out.println("Desenhando um retângulo na posição (" + getX() + ", " + getY() + ") com base " + base + " e altura " + altura);
    }

    @Override
    public String toString() {
        return "Retângulo na posição (" + getX() + ", " + getY() + ") com base " + base + " e altura " + altura;
    }
}
