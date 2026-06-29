public class Retangulo extends Figura {
    private double base;
    private double altura;

    public Retangulo(double x, double y, double base, double altura) {
       System.out.println("Criando retângulo");
      super(x, y);
        this.base = base;
        this.altura = altura;
    }

    @Override
    public void desenhar() {
        System.out.println("Desenhando um retângulo na posição (" + getX() + ", " + getY() + ") com base " + base + " e altura " + altura);
    }
}
