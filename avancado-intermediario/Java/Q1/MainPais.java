import java.util.ArrayList;
import java.util.List;

public class MainPais {
    public static void main(String[] args) {

        Pais brasil = new Pais("BRA", "Brasil", 8515767.049);
        brasil.setPopulacao(213000000);

        Pais uruguai = new Pais("URY", "Uruguai", 176215.0);
        uruguai.setPopulacao(3473730);

        Pais argentina = new Pais("ARG", "Argentina", 2780400.0);
        argentina.setPopulacao(45376763);

        Pais paraguai = new Pais("PRY", "Paraguai", 406752.0);
        paraguai.setPopulacao(7132538);

        Pais bolivia = new Pais("BOL", "Bolívia", 1098581.0);
        bolivia.setPopulacao(11673021);

        brasil.adicionarFronteira(uruguai);
        brasil.adicionarFronteira(argentina);
        brasil.adicionarFronteira(paraguai);
        brasil.adicionarFronteira(bolivia);

        List<Pais> fronteirasSulCentroOeste = new ArrayList<>();
        fronteirasSulCentroOeste.add(uruguai);
        fronteirasSulCentroOeste.add(argentina);
        fronteirasSulCentroOeste.add(paraguai);
        fronteirasSulCentroOeste.add(bolivia);

        
        System.out.println("--- Países Limítrofes (Sul / Centro-Oeste) do Brasil ---");
        for (Pais pais : fronteirasSulCentroOeste) {
            System.out.printf("Nome: %-10s | Densidade Populacional: %.2f hab/Km²%n",
                    pais.getNome(), pais.getDensidadePopulacional());
        }
    }
}

