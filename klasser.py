class Materiale(object):
    def __init__(self, idnr, titel, antal, antaludlaan, aarstal):

        self.idnr = idnr
        self.titel = titel
        self.anal = antal
        self.antaludlaan = antaludlaan
        self.aarstal = aarstal

class Bog(Materiale):
    def __init__(self, idnr, titel, antal, antaludlaan, aarstal, antalsider, forfatter):
        super().__init__(idnr, titel, antal, antaludlaan, aarstal)
        self.antalsider = antalsider
        self.forfatter = forfatter

class Film(Materiale):
    def __init__(self, idnr, titel, antal, antaludlaan, aarstal, instruktor, laengde):
        super().__init__(idnr, titel, antal, antaludlaan, aarstal)
        self.instruktor = instruktor
        self.laengde = laengde
