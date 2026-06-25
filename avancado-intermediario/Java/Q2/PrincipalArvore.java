public class PrincipalArvore {
    public static void main(String[] args) {

        // 1. Instanciação usando os diferentes construtores sobrecarregados

        // Avós maternos (sem ancestrais informados)
        Pessoa joaquim = new Pessoa("Joaquim"); // [cite: 247]
        Pessoa ana = new Pessoa("Ana"); // [cite: 248]

        // Avô paterno (sem ancestrais informados)
        Pessoa jaco = new Pessoa("Jacó"); // [cite: 252]

        // Pais (com ancestrais informados ou mistos)
        Pessoa maria = new Pessoa("Maria", joaquim, ana); // [cite: 249]
        Pessoa jose = new Pessoa("José", jaco, null); // [cite: 250]

        // Filho (com ancestrais informados)
        Pessoa jesusCristo = new Pessoa("Jesus Cristo", jose, maria); // [cite: 251]

        // 2. Demonstração dos testes lógicos no terminal

        System.out.println("--- Testes de Ancestralidade ---");
        System.out.println("Joaquim é ancestral de Jesus Cristo? " + jesusCristo.verificarAncestralidade(joaquim)); // [cite: 255]
        System.out.println("Ana é ancestral de Jesus Cristo? " + jesusCristo.verificarAncestralidade(ana)); // [cite: 256]
        System.out.println("Jacó é ancestral de Jesus Cristo? " + jesusCristo.verificarAncestralidade(jaco)); // [cite: 257]
        System.out.println("Maria é ancestral de Jesus Cristo? " + jesusCristo.verificarAncestralidade(maria)); // [cite: 258]
        System.out.println("José é ancestral de Jesus Cristo? " + jesusCristo.verificarAncestralidade(jose)); // [cite: 258]

        System.out.println("\n--- Testes de Irmandade ---");
        System.out.println("Joaquim é irmão de Jacó? " + joaquim.verificarIrmandade(jaco)); // [cite: 258]
        System.out.println("Jesus Cristo é irmão de Maria? " + jesusCristo.verificarIrmandade(maria)); // [cite: 259]
    }
}
