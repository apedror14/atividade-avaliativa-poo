public class NumeroComplexo {
        private double parteReal;
        private double parteImaginaria;

        public NumeroComplexo(double parteReal, double parteImaginaria) {
            this.parteReal = parteReal;
            this.parteImaginaria = parteImaginaria;
        }
        public double getParteReal() {
            return parteReal;
        }
        public void setParteReal(double parteReal) {
            this.parteReal = parteReal;
        }
        public double getParteImaginaria() {
            return parteImaginaria;
        }
        public void setParteImaginaria(double parteImaginaria) {
            this.parteImaginaria = parteImaginaria;
        }
        public void somar(NumeroComplexo outro) {
            this.parteReal = this.parteReal + outro.getParteReal();
            this.parteImaginaria = this.parteImaginaria + outro.getParteImaginaria();
        }
        public void subtrair(NumeroComplexo outro) {
            this.parteReal = this.parteReal - outro.getParteReal();
            this.parteImaginaria = this.parteImaginaria - outro.getParteImaginaria();
        }
        public void imprimir() {
            if (this.parteImaginaria >= 0) {
                System.out.println(this.parteReal + " + i" + this.parteImaginaria);
            } else {
                System.out.println(this.parteReal + " - i" + Math.abs(this.parteImaginaria));
            }
        }
    }

