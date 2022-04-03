#ismaya_ariayani_D0219338
class Data():
    __items = 4 # private
 
    def __init__(self,nama_barang):
        self.nama = nama_barang
 
    def harga_barang(self,harga_barang):
       hasil = self.__items * harga_barang
       return hasil
 
Boneka = Data("Boneka")
print(Boneka.harga_barang(550000))
 
