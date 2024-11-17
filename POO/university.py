class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.departamentos = []
        self.ativo = True

    def adicionar_departamento(self, departamento):
        if not self.ativo:
            raise Exception("Universidade inativa não pode receber departamentos")
        if len(self.departamentos) < 5:
            self.departamentos.append(departamento)
            departamento.definir_universidade(self)
            return True
        return False

    def remover_departamento(self, departamento):
        if departamento in self.departamentos:
            self.departamentos.remove(departamento)
            departamento.desativar()  # Por ser composição, desativa o departamento

    def desativar(self):
        self.ativo = False
        # Quando a universidade é desativada, por ser composição,
        # todos os departamentos devem ser desativados
        for departamento in self.departamentos[:]:
            self.remover_departamento(departamento)

    def __str__(self):
        status = "Ativa" if self.ativo else "Inativa"
        return f"Universidade: {self.nome} - {status}"