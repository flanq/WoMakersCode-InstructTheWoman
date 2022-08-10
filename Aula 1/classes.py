#Definicao da classe

class Televisao : 
  def __init__ (self):
    self.ligada = False
    self.canal = 3
    self.canal_min = 1
    self.canal_max = 90
    self.volume = 30
    self.volume_min = 0
    self.volume_max = 100

  def ligar(self):
    self.ligada = True

  def desligar(self):
    self.ligada = False

  def mudar_canal_para_cima(self):
    if not self.ligada:
      return
    if self.canal < self.canal_max:
        self.canal += 1

  def mudar_canal_para_baixa(self):
    if not self.ligada:
      return
    if self.canal > self.canal_min:
        self.canal -= 1

  def aumentar_volume(self):
     if not self.ligada:
      return
     if self.volume < self.volume_max:
        self.volume += 10

  def volume_diminuir(self):
    if not self.ligada:
      return
    if self.volume > self.volume_min:
        self.volume -= 10    

  def __str__(self) -> str:
    return f'Televisao - ligada{self.ligada} - canal {self.canal} - volume {self.volume}'

#Criando instancias da class Televisão
tv_sala =  Televisao()
tv_quarto = Televisao()

#Quando chamamos o método ligar()em uma instância estamos alterando apenas o estado dela. A outra televisão permanece deligada.

tv_sala.ligar()
print('tv_sala_está ligada {}' .format(tv_sala.ligada)) #format é o método ideal de formatação de saida
print('tv_sala_está ligada {}' .format(tv_quarto.ligada))

for _ in range(3):
  tv_sala.aumentar_volume()

print('tv_sala volume: {}' .format(tv_sala.volume))
print('tv_sala volume: {}' .format(tv_quarto.volume))

#Imprirmir conteudo do objeto 
print('tv_sala:', tv_sala)
print('tv_sala:', tv_quarto)