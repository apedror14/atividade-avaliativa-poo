import java.util.ArrayList;
import java.util.List;

public class MainUniversidade{
    public static void main(String[] args) {
        List<Universidade> lista = new ArrayList<>();
        
        Universidade o1 = new UniversidadeEaD("UFRA EaD", "https://www.ufra.edu.br/avaliacoes");
        Universidade o2 = new UniversidadeEaD("UFPA EaD", "https://www.UFPA.edu.br/avaliacoes");

        Universidade o3 = new UniversidadeFisica("UEPA", "Ananindeua");
        Universidade o4 = new UniversidadeFisica("IFPA", "Belém");

        lista.add(o1);
        lista.add(o2);
        lista.add(o3);
        lista.add(o4);

        for(Universidade o : lista){
            System.out.println("Nome: " + o.getNome());
            o.aplicarAvaliacao();
            System.out.print("\n");
        }
    }
}