# Encapsulamentoo

class Pessoa:
  def __init__(self, nome, profissao, identidade):
    self._nome = nome
    self.profissao = profissao
    self.__identidade = identidade

  def __str__(self):
    return f'Nome: {self._nome}, Profissão: {self.profissao}, Identidade: {self.__identidade}'

pessoa1 = Pessoa('Ana', 'Programadora', '123456')
print(pessoa1)


#Ao tentar alterar um atributo público, o valor é alterado
pessoa1.profissao = 'Médica'
print(pessoa1)

#Ao tentar alterar um atributo protegido, vamos conseguir
pessoa1._nome = 'Marta'
print(pessoa1)

#O atributo privado não pode ser alterado 
pessoa1.__identidade = '23659'
print(pessoa1)