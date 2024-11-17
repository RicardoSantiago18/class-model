class Disciplina:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.professores = []  # Lista de professores que ministram a disciplina
        self.ativo = True

    def adicionar_professor(self, professor):
        if not self.ativo:
            raise Exception("Disciplina inativa não pode receber professores")
        if len(self.professores) < 5 and professor not in self.professores:
            self.professores.append(professor)
            if self not in professor.disciplinas:
                professor.adicionar_disciplina(self)
            return True
        return False

    def remover_professor(self, professor):
        if professor in self.professores:
            self.professores.remove(professor)
            professor.disciplinas.remove(self)

    def desativar(self):
        self.ativo = False
        # Remove todas as referências de professores
        for professor in self.professores[:]:  # Usa uma cópia da lista para evitar problemas durante a iteração
            self.remover_professor(professor)

    def __str__(self):
        status = "Ativa" if self.ativo else "Inativa"
        return f"Disciplina: {self.nome} (Código: {self.codigo}) - {status}"