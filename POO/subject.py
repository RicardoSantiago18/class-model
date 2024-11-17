class Disciplina:
    def init(self, nome, codigo, cargaHoraria, creditos):
        self.nome = nome
        self.codigo = codigo
        self.cargaHoraria = cargaHoraria
        self.creditos = creditos
        self.professorResponsavel = None  # Associação (1 Disciplina é lecionada por 1 Professor)

    def definirProfessor(self, professor):
        self.professorResponsavel = professor

    def obterDetalhes(self):
        return f"Disciplina: {self.nome}, Código: {self.codigo}, Carga Horária: {self.cargaHoraria}h, Créditos: {self.creditos}"

    def atualizarCargaHoraria(self, novaCarga):
        self.cargaHoraria = novaCarga