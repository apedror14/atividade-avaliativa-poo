public class PrincipalArvore {
    public static void main(String[] args) {

        Pessoa joaquim = new Pessoa("Joaquim"); 
        Pessoa ana = new Pessoa("Ana"); 

        Pessoa jaco = new Pessoa("Jacó"); 

        Pessoa maria = new Pessoa("Maria", joaquim, ana); 
        Pessoa jose = new Pessoa("José", jaco, null); 

        Pessoa jesusCristo = new Pessoa("Jesus Cristo", jose, maria);

        System.out.println("--- Testes de Ancestralidade ---");
        System.out.println("Joaquim é ancestral de Jesus Cristo? " + jesusCristo.verificarAncestralidade(joaquim)); 
        System.out.println("Ana é ancestral de Jesus Cristo? " + jesusCristo.verificarAncestralidade(ana)); 
        System.out.println("Jacó é ancestral de Jesus Cristo? " + jesusCristo.verificarAncestralidade(jaco)); 
        System.out.println("Maria é ancestral de Jesus Cristo? " + jesusCristo.verificarAncestralidade(maria)); 
        System.out.println("José é ancestral de Jesus Cristo? " + jesusCristo.verificarAncestralidade(jose)); 

        System.out.println("\n--- Testes de Irmandade ---");
        System.out.println("Joaquim é irmão de Jacó? " + joaquim.verificarIrmandade(jaco)); 
        System.out.println("Jesus Cristo é irmão de Maria? " + jesusCristo.verificarIrmandade(maria)); 
    }
}
