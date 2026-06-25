//QUESTÃO 2
//pedido 1 do comando:
public class Pessoa {
    private String nome;
    private Pessoa pai;
    private Pessoa mae;

    //pedido letra a)
    // Construtor i: inicializa nome e ancestrais
    public Pessoa(String nome, Pessoa pai, Pessoa mae) {
        this.nome = nome;
        this.pai = pai;
        this.mae = mae;
    }

    // Construtor ii: inicializa nome sem ancestrais (null)
    public Pessoa(String nome) {
        this.nome = nome;
        this.pai = null;
        this.mae = null;
    }

    //GetNome não pedido explicitamente mas necessário para fazer comparações exigidas na questão
    public String getNome() {
        return nome;
    }

    // Metodo pedido na letra b): verificar igualdade semântica
    public boolean verificarIgualdadeSemantica(Pessoa outraPessoa) {
        if (outraPessoa == null) {
            return false;
        }

        boolean mesmoNome = this.nome.equals(outraPessoa.getNome());
        boolean mesmoPai = (this.pai == outraPessoa.pai);
        boolean mesmaMae = (this.mae == outraPessoa.mae);

        return mesmoNome && mesmoPai && mesmaMae;
    }

    // Metodo pedido na letra c): verificar se são irmãs
    public boolean verificarIrmandade(Pessoa outraPessoa) {
        if (outraPessoa == null || this.verificarIgualdadeSemantica(outraPessoa)) {
            return false; // Não pode ser irmão de si mesmo ou de nulo
        }

        boolean mesmoPai = (this.pai != null && this.pai.verificarIgualdadeSemantica(outraPessoa.pai));
        boolean mesmaMae = (this.mae != null && this.mae.verificarIgualdadeSemantica(outraPessoa.mae));

        return mesmoPai || mesmaMae;
    }

    // Metodo pedido na letra d): verificar se é ancestral
    public boolean verificarAncestralidade(Pessoa possivelAncestral) {
        if (possivelAncestral == null) {
            return false;
        }

        // i) É seu pai ou sua mãe diretos?
        if ((this.pai != null && this.pai.verificarIgualdadeSemantica(possivelAncestral)) ||
                (this.mae != null && this.mae.verificarIgualdadeSemantica(possivelAncestral))) {
            return true;
        }

        // ii) Ou ancestral do pai ou ancestral da mãe (recursão)?
        boolean ancestralPeloPai = (this.pai != null && this.pai.verificarAncestralidade(possivelAncestral));
        boolean ancestralPelaMae = (this.mae != null && this.mae.verificarAncestralidade(possivelAncestral));

        return ancestralPeloPai || ancestralPelaMae;
    }
}
