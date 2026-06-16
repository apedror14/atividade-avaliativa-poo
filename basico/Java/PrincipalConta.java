public class PrincipalConta {
    public static void main(String[] args) {
        Conta conta1 = new Conta(123, "456789-0");
        Conta conta2 = new Conta(456, "987654-3");

        System.out.println("Conta 1: Banco " + conta1.getBanco() + ", Número " + conta1.getNumero());
        System.out.println("Conta 2: Banco " + conta2.getBanco() + ", Número " + conta2.getNumero());

        conta1.transferir(456, "987654-3", 100.00);
        
        conta1.transferir(conta1, 200.00);
    }
}
