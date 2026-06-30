public class Figura {
    private double x;
    private double y;

    public Figura(double x, double y) {
        this.x = x;
        this.y = y;
        System.out.println("Criando figura");
    }

    public double getX() {
        return x;
    }

    public void setX(double x) {
        this.x = x;
    }

    public double getY() {
        return y;
    }

    public void setY(double y) {
        this.y = y;
    }

    public void desenhar() {
        System.out.println("Desenhando uma figura na posição (" + x + ", " + y + ")");
    }

    @Override
    public String toString() {
        return "Figura na posição (" + x + ", " + y + ")";
    }
}
