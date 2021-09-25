class obstaculo:
  def __init__(self, name, hp, ap, alive):  #aquí se define el constructor
    self.name = name
    self.hp = hp
    self.ap = ap
    self.alive = alive  #el estado por defecto del enemigo es "vivo", "True"

wolfman = obstaculo("Lucas", 7, 7, True)
vampire = obstaculo("Drácula", 8, 6, True)
