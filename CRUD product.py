from datetime import date

class Fournisseur:
    auto = 0
    def __init__(self, n="", a=""):
        self.__codeF = Fournisseur.auto
        Fournisseur.auto += 1
        self.__nomF = n
        self.__adress = a
        
    @property
    def code(self):
        return self.__codeF

    @property
    def nom(self):
        return self.__nomF
    @nom.setter
    def nom(self, nv):
        self.__nomF = nv

    @property
    def adress(self):
        return self.__adress
    @adress.setter
    def adress(self, nv):
        self.__adress = nv

    def __str__(self):
        return f"code fournisseur : {self.code}, nom : {self.nom}, adress : {self.adress}"

    def __eq__(self, objc):
        return objc.code == self.code and objc.nom == self.nom


class Produit:
    def __init__(self, d="", p=0, datep=None, datee=None, four=None):
        self.__designation = d
        self.__prix = p
        self.__datep = datep
        self.__datee = datee
        self.__fournisseur = four

    @property
    def des(self):
        return self.__designation
    @des.setter
    def des(self, nv):
        self.__designation = nv

    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self, nv):
        self.__prix = nv

    @property
    def datep(self):
        return self.__datep
    @datep.setter
    def datep(self, nv):
        self.__datep = nv

    @property
    def datee(self):
        return self.__datee
    @datee.setter
    def datee(self, nv):
        self.__datee = nv

    @property
    def four(self):
        return self.__fournisseur
    @four.setter
    def four(self, nv):
        self.__fournisseur = nv

    def __str__(self):
        return (f"designation : {self.des}, prix : {self.prix}, "
                f"date production : {self.datep}, date expiration : {self.datee}, "
                f"fournisseur : {self.four}")

    def __eq__(self, objp):
        return objp.des == self.des


# --- Programme principal ---
def safe_date(y, m, d):
    """Vérifie si la date est valide"""
    try:
        return date(y, m, d)
    except ValueError:
        print("⚠️ Date invalide, veuillez réessayer.")
        return None


produits = []

while True:
    choix = int(input("""
1- Liste des produits
2- Ajouter produit
3- Supprimer Produit
4- Trouver un produit par son nom
5- Quitter le programme
Entrez votre choix : """))
    
    if choix == 1:
        if not produits:
            print("Aucun produit trouvé.\n")
        else:
            for i in produits:
                print(i, "\n")

    elif choix == 2:
        ds = input("Entrez la désignation du produit : ")
        pr = float(input("Entrez le prix : "))

        ydatep = int(input("Année de production : "))
        mdatep = int(input("Mois de production : "))
        jdatep = int(input("Jour de production : "))
        ydatee = int(input("Année d'expiration : "))
        mdatee = int(input("Mois d'expiration : "))
        jdatee = int(input("Jour d'expiration : "))

        datep = safe_date(ydatep, mdatep, jdatep)
        datee = safe_date(ydatee, mdatee, jdatee)

        if not datep or not datee:
            continue  # skip ajout si date invalide

        nf = input("Nom du fournisseur : ")
        ad = input("Adresse du fournisseur : ")

        C = Produit(ds, pr, datep, datee, Fournisseur(nf, ad))
        produits.append(C)
        print("✅ Produit ajouté avec succès !\n")

    elif choix == 3:
        ds = input("Entrez la désignation du produit à supprimer : ")
        found = False
        for p in produits:
            if p.des == ds:
                produits.remove(p)
                found = True
                print("🗑️ Produit supprimé avec succès.\n")
                break
        if not found:
            print("❌ Produit introuvable.\n")

    elif choix == 4:
        nm = input("Entrez la désignation du produit à chercher : ")
        found = False
        for p in produits:
            if p.des == nm:
                print("🔍 Produit trouvé :\n", p, "\n")
                found = True
                break
        if not found:
            print("❌ Produit introuvable.\n")

    elif choix == 5:
        print("👋 Au revoir !")
        break

    else:
        print("❌ Choix invalide, veuillez réessayer.\n")
