import java.util.ArrayList;
import java.util.List;

public class Pais {
    private String codigoIso;
    private String nome;
    private long populacao;
    private double dimensaoKm2;
    private List<Pais> fronteiras;


    
    public Pais(String codigoIso, String nome, double dimensaoKm2) {
        this.codigoIso = codigoIso;
        this.nome = nome;
        this.dimensaoKm2 = dimensaoKm2;
        this.populacao = 0; 
        this.fronteiras = new ArrayList<>();
    }

    public String getCodigoIso() {
        return codigoIso;
    }

    public void setCodigoIso(String codigoIso) {
        this.codigoIso = codigoIso;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public long getPopulacao() {
        return populacao;
    }

    public void setPopulacao(long populacao) {
        this.populacao = populacao;
    }

    public double getDimensaoKm2() {
        return dimensaoKm2;
    }

    public void setDimensaoKm2(double dimensaoKm2) {
        this.dimensaoKm2 = dimensaoKm2;
    }

    public List<Pais> getFronteiras() {
        return fronteiras;
    }

    public boolean ehMesmoPais(Pais outro) {
        if (outro == null) {
            return false;
        }
        if (this.codigoIso == null) {
            return outro.codigoIso == null;
        }
        return this.codigoIso.equalsIgnoreCase(outro.codigoIso);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null || getClass() != obj.getClass()) {
            return false;
        }
        Pais outro = (Pais) obj;
        return ehMesmoPais(outro);
    }

    @Override
    public int hashCode() {
        return codigoIso != null ? codigoIso.toLowerCase().hashCode() : 0;
    }

    public void adicionarFronteira(Pais pais) {
        if (pais != null && !this.ehMesmoPais(pais) && !this.ehLimitrofe(pais)) {
            this.fronteiras.add(pais);

            if (!pais.ehLimitrofe(this)) {
                pais.adicionarFronteira(this);
            }
        }
    }

    public boolean ehLimitrofe(Pais pais) {
        if (pais == null) {
            return false;
        }
        for (Pais p : this.fronteiras) {
            if (p.ehMesmoPais(pais)) {
                return true;
            }
        }
        return false;
    }

    public double getDensidadePopulacional() {
        if (this.dimensaoKm2 <= 0) {
            return 0.0;
        }
        return (double) this.populacao / this.dimensaoKm2;
    }


    public List<Pais> vizinhosComuns(Pais outro) {
        List<Pais> comuns = new ArrayList<>();
        if (outro == null) {
            return comuns;
        }
        for (Pais p : this.fronteiras) {
            if (outro.ehLimitrofe(p)) {
                comuns.add(p);
            }
        }
        return comuns;
    }

    
    @Override
    public String toString() {
        return "Pais{" +
                "codigoIso='" + codigoIso + '\'' +
                ", nome='" + nome + '\'' +
                ", populacao=" + populacao +
                ", dimensaoKm2=" + dimensaoKm2 +
                ", fronteiras=" + fronteiras.size() + " vizinho(s)" +
                '}';
    }
}
