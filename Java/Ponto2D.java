package Questao1;

public class Ponto2D {
    private double coordX;
    private double coordY;

    public Ponto2D(double x, double y) {
        this.coordX = x;
        this.coordY = y;
    }

    public double getX(){
        return coordX;
    }

    public void setX(double x){
        this.coordX = x;
    }

    public double getY() {
        return coordY;
    }

    public void setY(double y) {
        this.coordY = y;
    }

    public void movimentar(double x, double y){
        this.coordX = x;
        this.coordY = y;
    }

    public void movimentar(Ponto2D ponto){
        this.coordX = ponto.getX();
        this.coordY = ponto.getY();
    }

    public double distancia(Ponto2D ponto){
        double horizontal = Math.pow(ponto.getX() - coordX, 2);
        double vertical = Math.pow(ponto.getY() - coordY, 2);
        return Math.sqrt(vertical + horizontal);
    }

    public Ponto2D clonar(){
        return new Ponto2D(coordX, coordY);
    }
}
