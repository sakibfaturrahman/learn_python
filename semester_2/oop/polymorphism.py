# Satu method, banyak bentuk.
class Hewan:
    def suara(self):
        print("Suara hewan")

class Kucing(Hewan):
    def suara(self):
        print("Meong")

class Anjing(Hewan):
    def suara(self):
        print("Guk")

for h in [Kucing(), Anjing()]:
    h.suara()
