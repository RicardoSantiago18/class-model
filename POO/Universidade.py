from departamento import Departamento

class Universidade:
    def __init__(self, nome, endereco, fundacao):
        self.nome = nome
        self.endereco = endereco
        self.fundacao = fundacao
        self.listaDepartamentos = []

    def adicionarDepartamento(self, departamento):
        if len(self.listaDepartamentos) < 5:
            self.listaDepartamentos.append(departamento)
        else:
            print("A universidade já possui o número máximo de departamentos (5).")

    def removerDepartamento(self, departamento):
        if departamento in self.listaDepartamentos:
            self.listaDepartamentos.remove(departamento)

    def listarDepartamentos(self):
        for departamento in self.listaDepartamentos:
            print(f"Departamento: {departamento.nome}")

    def obterInformacoes(self):
        return f"Universidade: {self.nome}, Endereço: {self.endereco}, Fundação: {self.fundacao}"

