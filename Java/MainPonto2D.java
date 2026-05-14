package Questao1;

public class MainPonto2D {
    static void main(String[] args) {
        Ponto2D p1 = new Ponto2D(3,4);
        Ponto2D p2 = new Ponto2D(10,8);

        // Propriedades
        System.out.println("Ponto 1: (" + p1.getX() + "," + p1.getY() + ")");
        System.out.println("Ponto 2: (" + p2.getX() + "," + p2.getY() + ")");

        // Método movimentar
        System.out.println("Distância (p1 - p2): " + p1.distancia(p2));

        // Método clonar
        Ponto2D p3 = p1.clonar();
        System.out.println("Ponto 3: (" + p3.getX() + "," + p3.getY() + ")");

        // Método Movimentar
        p3.movimentar(7,5);
        System.out.println("Ponto 3 Novo: (" + p3.getX() + "," + p3.getY() + ")");
    }
}
