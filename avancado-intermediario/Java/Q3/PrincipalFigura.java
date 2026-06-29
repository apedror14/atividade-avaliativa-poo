public class PrincipalFigura {
    public static void main(String[] args) {
        
        Figura figura = new Figura(1.0, 0.0);
        Circulo circulo = new Circulo(0.0, 1.0, 4.0);
        Retangulo retangulo = new Retangulo(2.0, 0.0, 3.0, 5.0);
        
        figura.desenhar();
        circulo.desenhar();
        retangulo.desenhar();

        Figura variavelFigura;

        variavelFigura = circulo;
        variavelFigura.desenhar();

        variavelFigura = retangulo;
        variavelFigura.desenhar();
    }
}
