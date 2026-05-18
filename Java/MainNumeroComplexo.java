public class MainNumeroComplexo {
    public static void main(String[] args) {
        NumeroComplexo num1 = new NumeroComplexo(5.0, 3.0);
        NumeroComplexo num2 = new NumeroComplexo(2.0, 1.0);

        System.out.print("Número 1 original: ");
        num1.imprimir();

        System.out.print("Número 2 original: ");
        num2.imprimir();

        System.out.println(" ");

        num1.somar(num2);
        System.out.print("Resultado da Soma (Num1 + Num2): ");
        num1.imprimir();

        System.out.println(" ");

        num1.setParteReal(5.0);
        num1.setParteImaginaria(3.0);

        num1.subtrair(num2);
        System.out.print("Resultado da Subtração (Num1 - Num2): ");
        num1.imprimir();
    }
}