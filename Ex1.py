class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

pessoa = Pessoa("João", 30)
print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}")

aluno = Aluno("Maria", 20, "2023-123")
print(f"Nome: {aluno.nome}, Idade: {aluno.idade}, Matrícula: {aluno.matricula}")
