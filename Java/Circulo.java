public class Circulo {

    private Double raio;
    private Double coordenadaX;
    private Double coordenadaY;
    private String centroDoCirculo;

    public Circulo(Double coordenadaX, Double coordenadaY, Double raio) {
        this.coordenadaX = coordenadaX;
        this.coordenadaY = coordenadaY;
        this.raio = raio;
        centroDoCirculo = "(" + coordenadaX + ", " + coordenadaY + ")";
    }

    public String getCentroDoCirculo() {
        return centroDoCirculo;
    }

    public Double getRaio() {
        return raio;
    }

    public void inflar(Double valor) {
        if(valor > 0){
            this.raio += valor;
        }
    }

    public void desinflar(Double valor) {
        if(valor > 0){
            this.raio -= valor;
        }
    }

    public void inflar() {
        this.raio += 1;
    }

    public void desinflar() {
            this.raio -= 1;
    }

    public void MoverCentro(){
        this.coordenadaX = 0.0;
        this.coordenadaY = 0.0;
        this.centroDoCirculo = "(0, 0)";
    }

    public void MoverCentro(Double coordenadaX, Double coordenadaY){
        this.coordenadaX = coordenadaX;
        this.coordenadaY = coordenadaY;
        this.centroDoCirculo = "(" + coordenadaX + ", " + coordenadaY + ")";
    }

    public Double Area() {
        return raio * raio * 3.14159 ;
    }

    @Override
    public String toString() {
        return String.format("\n"
                + "raio = " + "%.2f" + "\n"
                + "Centro do Circulo = '" + centroDoCirculo + "\n"
                + "Area = " +  "%.2f",  raio, Area());
    }
}
