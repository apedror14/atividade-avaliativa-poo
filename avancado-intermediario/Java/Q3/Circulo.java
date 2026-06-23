public class Circulo extends Figura {
    private double raio;

    public Circulo(int x, int y, double raio) {
        super(x, y);
        System.out.println("Criando círculo");
        this.raio = raio;
    }

    public void desenhar() {
        System.out.println(
            "Desenhando um círculo na posição (" + getX() + ", " + getY() + ") com raio de " + raio
        );
    }
}
