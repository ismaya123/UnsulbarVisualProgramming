class Smartphone:
    def __init__(self, inputMerk, inputHarga, inputTahun):
        self.merk = inputMerk
        self.harga = inputHarga
        self.tahun = inputTahun

hp1 = Smartphone("Oppo", 1000000, 2015)
hp2 = Smartphone("Vivo", 4000000, 2019)

print (hp1.merk)
