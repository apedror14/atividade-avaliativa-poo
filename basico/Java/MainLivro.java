public class MainLivro {

    public static void main(String[] args) {
    
    Livro oAutoDaCompadecida = new Livro("O Auto da Compadecida", "Ariano Suassuna", 1955, 120, 0.3, 1.2);

        Livro oExorcista = new Livro("O Exorcista", "William Blatty", 1971, 366, 0.9, 3.0);

        System.out.println("Livro 1: " + oAutoDaCompadecida.getTitulo() + " - " + oAutoDaCompadecida.getAnoPublicacao());
        System.out.println("Livro 2: " + oExorcista.getTitulo() + " - " + oExorcista.getAnoPublicacao());


        oAutoDaCompadecida.marcarPagina(150);
        oExorcista.marcarPagina(100);
        
    }
}
