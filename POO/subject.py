class Disciplina:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.professor = None

    def associarProfessor(self, professor):
        if not self.professor:
            self.professor = professor
            print(f"Disciplina {self.nome} agora está associada ao Professor {professor.nome}.")
        else:
            print(f"Disciplina {self.nome} já está associada ao Professor {self.professor.nome}.")

    def removerProfessor(self):
        if self.professor:
            print(f"Removendo Professor {self.professor.nome} da Disciplina {self.nome}.")
            self.professor = None
        else:
            print(f"A Disciplina {self.nome} não está associada a nenhum Professor.")
