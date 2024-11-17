class Disciplina:
    def __init__(self, nome, codigo, cargaHoraria, creditos):
        self.nome = nome
        self.codigo = codigo
        self.cargaHoraria = cargaHoraria
        self.creditos = creditos
        self.professorResponsavel = None
    def definirProfessor(self, professor):
        self.professorResponsavel = professor

    def obterDetalhes(self):
        return (f"Disciplina: {self.nome}, Código: {self.codigo}, Carga Horária: {self.cargaHoraria}h,"
                f" Créditos: {self.creditos},"
                f" Professor: {self.professorResponsavel.nome if self.professorResponsavel else 'N/A'}")

    def atualizarCargaHoraria(self, novaCarga):
        self.cargaHoraria = novaCarga
