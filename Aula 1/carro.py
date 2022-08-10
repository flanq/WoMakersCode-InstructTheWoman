
class Carro : 
  def __init__ (self):
    self.ligado = False
    self.cor = 'Amarelo'
    self.modelo = 'Golf'
    self.velocidade = 0
    self.velocidade_max = 250

  def ligar(self):
    self.ligado = True

  def desligar(self):
    self.ligado = False

  def acelerar(self):
    if not self.ligado:
      return
    if self.velocidade < self.velocidade_max:
        self.velocidade += 1

  def desacelerar(self):
    if not self.ligado:
      return
    if self.velocidade > 0:
        self.velocidade -= 1

  def __str__(self) -> str:
    return f' \n Ligado - {self.ligado} \n Modelo - {self.modelo} \n Cor - {self.cor} \n Velocidade - {self.velocidade}km/h'

carro_flavia =  Carro()
carro_flavia.ligar()

for _ in range(50):
  carro_flavia.acelerar()

print('Carro:', carro_flavia)
