public class Pessoa {
    private String nome;
    private Pessoa pai;
    private Pessoa mae;

    public Pessoa(String nome, Pessoa pai, Pessoa mae) {
        this.nome = nome;
        this.pai = pai;
        this.mae = mae;
    }

    public Pessoa(String nome) {
        this.nome = nome;
        this.pai = null;
        this.mae = null;
    }

    public String getNome() {
        return nome;
    }

    public boolean verificarIgualdadeSemantica(Pessoa outraPessoa) {
        if (outraPessoa == null) {
            return false;
        }

        boolean mesmoNome = this.nome.equals(outraPessoa.getNome());
        boolean mesmoPai = (this.pai == outraPessoa.pai);
        boolean mesmaMae = (this.mae == outraPessoa.mae);

        return mesmoNome && mesmoPai && mesmaMae;
    }

    public boolean verificarIrmandade(Pessoa outraPessoa) {
        if (outraPessoa == null || this.verificarIgualdadeSemantica(outraPessoa)) {
            return false; 
        }

        boolean mesmoPai = (this.pai != null && this.pai.verificarIgualdadeSemantica(outraPessoa.pai));
        boolean mesmaMae = (this.mae != null && this.mae.verificarIgualdadeSemantica(outraPessoa.mae));

        return mesmoPai || mesmaMae;
    }

    public boolean verificarAncestralidade(Pessoa possivelAncestral) {
        if (possivelAncestral == null) {
            return false;
        }

        if ((this.pai != null && this.pai.verificarIgualdadeSemantica(possivelAncestral)) ||
                (this.mae != null && this.mae.verificarIgualdadeSemantica(possivelAncestral))) {
            return true;
        }

        boolean ancestralPeloPai = (this.pai != null && this.pai.verificarAncestralidade(possivelAncestral));
        boolean ancestralPelaMae = (this.mae != null && this.mae.verificarAncestralidade(possivelAncestral));

        return ancestralPeloPai || ancestralPelaMae;
    }

    @Override
    public String toString() {
        String nomePai = (pai != null) ? pai.getNome() : "desconhecido(a)";
        String nomeMae = (mae != null) ? mae.getNome() : "desconhecido(a)";
        return "Nome: " + nome + ", Pai: " + nomePai + ", Mãe: " + nomeMae;
    }
}
