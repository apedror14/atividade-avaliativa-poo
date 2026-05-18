public class Circulo {

    private Double raio;
    private Double coordenadaX;
    private Double coordenadaY;

    public Circulo(Double raio, Double coordenadaX, Double coordenadaY) {
        this.raio = raio;
        this.coordenadaX = coordenadaX;
        this.coordenadaY = coordenadaY;
    }

    public String getCentroDoCirculo() {
        return "(" + coordenadaX + ", " + coordenadaY + ")";
    }

    public Double getRaio() {
        return raio;
    }

    public void inflar(Double valor) {
        if (valor > 0) {
            this.raio += valor;
        }
    }

    public void desinflar(Double valor) {
        if (valor > 0) {
            this.raio -= valor;
        }
        if (this.raio < 0) {
            this.raio = 0.0;
        }
    }

    public void inflar() {
        this.raio += 1.0;
    }

    public void desinflar() {
        this.raio -= 1.0;
        if (this.raio < 0) {
            this.raio = 0.0;
        }
    }

    public void moverCentro() {
        this.coordenadaX = 0.0;
        this.coordenadaY = 0.0;
    }

    public void moverCentro(Double coordenadaX, Double coordenadaY) {
        this.coordenadaX = coordenadaX;
        this.coordenadaY = coordenadaY;
    }

    public Double calcularArea() {
        return raio * raio * 3.14159;
    }

    @Override
    public String toString() {
        return String.format("\n"
                + "raio = %.2f\n"
                + "Centro do Circulo = %s\n"
                + "Area = %.2f", raio, getCentroDoCirculo(), calcularArea());
    }
}
