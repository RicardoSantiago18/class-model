from department import Departamento

class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.departamentos = []

    def adicionarDepartamento(self, departamento):
        if len(self.departamentos) < 5:
            self.departamentos.append(departamento)
        else:
            print("Número máximo de departamentos atingido!")

    def listarDepartamentos(self):
        if self.departamentos:
            for departamento in self.departamentos:
                print(f"Departamento: {departamento.nome}")
        else:
            print("Nenhum departamento cadastrado na universidade.")

    def removerDepartamento(self, departamento):
        if departamento in self.departamentos:
            self.departamentos.remove(departamento)
            print(f"Departamento {departamento.nome} removido da Universidade {self.nome}.")
        else:
            print(f"O Departamento {departamento.nome} não existe na Universidade {self.nome}.")
