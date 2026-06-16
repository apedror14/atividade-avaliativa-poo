public class Conta {
    private int banco;
    private String numero;

    public int getBanco() {
        return banco;
    }
    public void setBanco(int banco) {
        this.banco = banco;
    }

    public String getNumero() {
        return numero;
    }
    public void setNumero(String numero) {
        this.numero = numero;
    }    

    public Conta(int banco, String numero) {
        this.banco = banco;
        this.numero = numero;
    }

    public void transferir(int banco, String numero, double valor) {
        System.out.println("Transferindo " + valor + " para conta Banco: " + banco + ", Numero: " + numero);
    }
    
    public void transferir(Conta conta, double valor) {
        System.out.println("Transferindo " + valor + " para conta Banco: " + conta.getBanco() + ", Numero: " + conta.getNumero());
    }
}
