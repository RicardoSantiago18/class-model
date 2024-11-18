from department import Departamento

class Universidade:
    def __init__(self, nome, endereco, ano_fundacao):
        self.nome = nome
        self.endereco = endereco
        self.ano_fundacao = ano_fundacao
        self.departamentos = []

    def criarDepartamento(self, nome, codigo):
        if len(self.departamentos) < 5:
            novo_departamento = Departamento(nome, codigo)
            self.departamentos.append(novo_departamento)
            return novo_departamento
        else:
            print("Número máximo de departamentos atingido!")
            return None

    def listarDepartamentos(self):
        for departamento in self.departamentos:
            print(f"Departamento: {departamento.nome}, Código: {departamento.codigo}")

    def removerDepartamento(self, departamento):
        if departamento in self.departamentos:
            self.departamentos.remove(departamento)
