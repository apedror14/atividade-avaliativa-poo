public class Circulo extends Figura {
    private double raio;

    public Circulo(double x, double y, double raio) {
        super(x, y);
        this.raio = raio;
        System.out.println("Criando círculo");
    }

    public void desenhar() {
        System.out.println("Desenhando um círculo na posição (" + getX() + ", " + getY() + ") com raio de " + raio);
    }
}
