class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []
        self.universidade = None
        self.ativo = True

    def adicionar_professor(self, professor):
        if not self.ativo:
            raise Exception("Departamento inativo não pode receber professores")
        if len(self.professores) < 5 and professor not in self.professores:
            self.professores.append(professor)
            professor.definir_departamento(self)
            return True
        return False

    def remover_professor(self, professor):
        if professor in self.professores:
            self.professores.remove(professor)
            if professor.departamento == self:
                professor.departamento = None

    def definir_universidade(self, universidade):
        self.universidade = universidade

    def desativar(self):
        self.ativo = False
        # Quando um departamento é desativado (por composição com a universidade)
        # todos os seus professores devem ser desativados
        for professor in self.professores[:]:
            professor.desativar()
        self.professores.clear()

    def __str__(self):
        status = "Ativo" if self.ativo else "Inativo"
        return f"Departamento: {self.nome} - {status}"