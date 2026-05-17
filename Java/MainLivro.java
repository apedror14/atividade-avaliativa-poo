public class MainLivro {

    public static void main(String[] args) {
    
    Livro oAutoDaCompadecida = new Livro("O Auto da Compadecida", "Ariano Suassuna", 1942, 100, 0.5, 1.2);

        Livro oExorcista = new Livro("O Auto da Compadecida", "Ariano Suassuna", 1942, 100, 0.5, 1.2);

        System.out.println("Livro 1: " + oAutoDaCompadecida.getTitulo() + " - " + oAutoDaCompadecida.getAnoPublicacao());

        oAutoDaCompadecida.marcarPagina(100);
        
    }
}
