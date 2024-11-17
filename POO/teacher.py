class Professor:
    def __init__(self, nome, id_funcional):
        self.nome = nome
        self.id_funcional = id_funcional
        self.disciplinas = []
        self.departamento = None
        self.ativo = True

    def adicionar_disciplina(self, disciplina):
        if not self.ativo:
            raise Exception("Professor inativo não pode receber disciplinas")
        if len(self.disciplinas) < 5 and disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
            return True
        return False

    def definir_departamento(self, departamento):
        if not self.ativo:
            raise Exception("Professor inativo não pode ser associado a departamento")
        # Remove do departamento anterior se existir
        if self.departamento and self.departamento != departamento:
            self.departamento.remover_professor(self)
        self.departamento = departamento

    def desativar(self):
        self.ativo = False
        # Remove todas as disciplinas
        for disciplina in self.disciplinas[:]:
            disciplina.remover_professor(self)
        # Remove do departamento
        if self.departamento:
            self.departamento.remover_professor(self)

    def __str__(self):
        status = "Ativo" if self.ativo else "Inativo"
        return f"Professor: {self.nome} (ID: {self.id_funcional}) - {status}"