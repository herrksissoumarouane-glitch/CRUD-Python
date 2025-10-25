class Client:
    code_client = 0

    def __init__(self, nom, adresse, date_naissance):
        Client.code_client += 1
        self.code_client = Client.code_client
        self.nom = nom
        self.adresse = adresse
        self.date_naissance = date_naissance

    def __str__(self):
        return f"Code client: {self.code_client}, Nom: {self.nom}, Adresse: {self.adresse}, Date de naissance: {self.date_naissance}"

    def est_egal(self, autre_client):
        return self.code_client == autre_client.code_client and self.nom == autre_client.nom


def ajouter_client(liste_clients):
    nom = input("Entrez le nom du client: ")
    adresse = input("Entrez l'adresse du client: ")
    date_naissance = input("Entrez la date de naissance du client: ")
    nouveau_client = Client(nom, adresse, date_naissance)
    liste_clients.append(nouveau_client)
    print("Client ajoute.")


def afficher_clients(liste_clients):
    if liste_clients:
        print("Liste des clients:")
        for client in liste_clients:
            print(client)
    else:
        print("Aucun client enregistre.")


def supprimer_client(liste_clients, nom):
    for client in liste_clients:
        if client.nom == nom:
            liste_clients.remove(client)
            
            return
    print("invalid client.")


def rechercher_client(liste_clients, nom):
    for client in liste_clients:
        if client.nom == nom:
            
            print(client)
            return
    print("invalid client.")


def modifier_adresse(liste_clients, nom):
    for client in liste_clients:
        if client.nom == nom:
            nouvelle_adresse = input("Entrez la nouvelle adresse du client: ")
            client.adresse = nouvelle_adresse
            
            return
    print("invalid client")


if __name__ == "__main__":
    liste_clients = []

    while True:
        print("""
        --Menu:--
    1. Ajouter Client
    2. Afficher tous les clients
    3. Supprimer Client par son nom
    4. Rechercher un client par son nom
    5. Modifier l’adresse d’un client par son nom
    6. Quitter le programme""")

        choix = input("entrez votre choix: ")

        if choix == "1":
            ajouter_client(liste_clients)
        elif choix == "2":
            afficher_clients(liste_clients)
        elif choix == "3":
            nom_client = input("Entrez le nom du client a supprimer: ")
            supprimer_client(liste_clients, nom_client)
        elif choix == "4":
            nom_client = input("Entrez le nom du client a rechercher: ")
            rechercher_client(liste_clients, nom_client)
        elif choix == "5":
            nom_client = input("Entrez le nom du client a modifier: ")
            modifier_adresse(liste_clients, nom_client)
        elif choix == "6":
            print("Programme termine.")
            break
        else:
            print("Choix invalide.")
