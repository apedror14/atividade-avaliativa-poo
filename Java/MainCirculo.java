public class MainCirculo {
    public static void main(String[] args) {

        Circulo c1 = new Circulo(3.2,5.6,1.5);
        Circulo c2 = new Circulo(5.5,1.8,7.2);

        System.out.println("Circulo 1: " + c1);
        System.out.println("Circulo 2: " +c2);
        System.out.println(" ");

        c1.inflar();
        c2.inflar();

        System.out.println("Circulo 1: " + c1);
        System.out.println("Circulo 2: " +c2);
        System.out.println(" ");

        c1.desinflar();
        c2.desinflar();

        System.out.println("Circulo 1: " + c1);
        System.out.println("Circulo 2: " +c2);
    }
}
