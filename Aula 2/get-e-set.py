# Getter = retornar o valor 
# Setter = definir ou atualizar

class Retangulo:
  def __init__(self, medida):
    self.altura = medida 
    self.largura = medida

  @property 
  def altura(self):
    return self.__medida

  @altura.setter
  def altura(self, valor):
   self.__medida = valor 

  @property
  def largura(self):
    return self.__medida

  @largura.setter
  def largura(self, valor):
    self.__medida = valor

  def area(self):
    return self.largura * self.altura

retangulo = Retangulo()
retangulo.altura = 3
retangulo.largura = 2