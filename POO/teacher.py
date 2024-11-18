class Professor:
    def __init__(self, nome, id_professor, area):
        self.nome = nome
        self.id_professor = id_professor
        self.area = area
        self.disciplinas = []

    def adicionarDisciplina(self, disciplina):
        if len(self.disciplinas) < 5:
            if disciplina.professor is None:  # Verifica se a disciplina já tem um professor
                self.disciplinas.append(disciplina)
                disciplina.associarProfessor(self)  # Associa o professor à disciplina
            else:
                print(f"A disciplina {disciplina.nome} já está sendo ministrada por outro professor.")
        else:
            print("Número máximo de disciplinas atingido!")

    def listarDisciplinas(self):
        if self.disciplinas:
            for disciplina in self.disciplinas:
                print(f"Disciplina: {disciplina.nome}, Código: {disciplina.codigo}")
        else:
            print("Este professor não ministra nenhuma disciplina.")

    def removerDisciplina(self, disciplina):
        if disciplina in self.disciplinas:
            disciplina.removerProfessor()  # Remove o professor da disciplina
            self.disciplinas.remove(disciplina)
            print(f"Disciplina {disciplina.nome} removida do Professor {self.nome}.")
        else:
            print(f"O Professor {self.nome} não ministra a disciplina {disciplina.nome}.")
