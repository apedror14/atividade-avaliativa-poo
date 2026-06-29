public abstract class Objeto {

    private double x;
    private double y;

    public Objeto() {
        this(0.0, 0.0);
    }

    public Objeto(double x, double y) {
        this.x = x;
        this.y = y;
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

    @Override
    public String toString() {
        return "X = " + x +
               "\nY = " + y + "\n";
    }
}
