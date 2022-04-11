class tari:
  def __init__(self, nama_tari, daerah):
    self.nama_tari = nama_tari
    self.daerah = daerah
 
  def printname(self):
    print('Tarian' ,self.nama_tari, 'Berasal dari Daerah' ,self.daerah)

class sulawesi(tari):
  pass

daerah1 = sulawesi("Sayyang Pattu'du", "Sulawesi Barat")
daerah1.printname()
daerah1 = sulawesi("Pakarena", "Sulawesi Selatan")
daerah1.printname()
