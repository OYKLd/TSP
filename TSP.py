import random
import copy

# Matrice des distances entre les villes (11 villes)
distances = [
    [0, 11, 15, 19, 23, 27, 32, 28, 22, 11, 10],
    [11, 0, 5, 10, 13, 18, 22, 20, 18, 9, 17],
    [15, 5, 0, 5, 10, 19, 17, 14, 14, 8, 18],
    [19, 10, 5, 0, 10, 20, 14, 9, 11, 11, 21],
    [23, 13, 10, 10, 0, 11, 11, 15, 21, 18, 28],
    [27, 18, 19, 20, 11, 0, 19, 25, 32, 26, 34],
    [32, 22, 17, 14, 11, 19, 0, 11, 23, 25, 35],
    [28, 20, 14, 9, 15, 25, 11, 0, 13, 18, 28],
    [22, 18, 14, 11, 21, 32, 23, 13, 0, 12, 18],
    [11, 9, 8, 11, 18, 26, 25, 18, 12, 0, 11],
    [10, 17, 18, 21, 28, 34, 35, 28, 18, 11, 0]
]

nb_villes = len(distances)

def calculer_distance_tour(tour):
    """Calcule la distance totale d'un tour"""
    return sum(distances[tour[i]][tour[(i + 1) % nb_villes]] for i in range(nb_villes))

def afficher_tour(tour, distance, etape):
    """Affiche les détails d'un tour"""
    print(f"\n=== {etape} ===")
    print("Ordre des villes:", " → ".join(str(v) for v in tour))
    print(f"Distance totale: {distance}")
    
    print("\nDétail des distances:")
    for i in range(nb_villes):
        v1, v2 = tour[i], tour[(i + 1) % nb_villes]
        print(f"  Ville {v1} → Ville {v2}: {distances[v1][v2]}")

def trouver_meilleur_voisin(tour):
    """Trouve le meilleur voisin en échangeant deux villes"""
    meilleur_tour = tour.copy()
    meilleure_distance = calculer_distance_tour(tour)
    amelioration = False
    
    print("\n--- Recherche des meilleurs voisins ---")
    echanges_testes = 0
    
    for i in range(nb_villes):
        for j in range(i + 1, nb_villes):
            echanges_testes += 1
            nouveau_tour = tour.copy()
            nouveau_tour[i], nouveau_tour[j] = nouveau_tour[j], nouveau_tour[i]
            
            nouvelle_distance = calculer_distance_tour(nouveau_tour)
            
            if nouvelle_distance < meilleure_distance:
                meilleur_tour = nouveau_tour
                meilleure_distance = nouvelle_distance
                amelioration = True
                print(f"✓ Échange {i}↔{j}: {nouvelle_distance} (amélioration)")
            else:
                print(f"  Échange {i}↔{j}: {nouvelle_distance}")
    
    print(f"\nÉchanges testés: {echanges_testes}")
    print(f"Amélioration trouvée: {'OUI' if amelioration else 'NON'}")
    
    return meilleur_tour, meilleure_distance

def melanger_tour(tour):
    """Mélange aléatoirement un tour"""
    nouveau_tour = tour.copy()
    random.shuffle(nouveau_tour)
    return nouveau_tour

def descente_locale_tsp():
    """Algorithme de descente locale pour le problème du voyageur de commerce"""
    print("=== ALGORITHME DE DESCENTE LOCALE POUR TSP ===\n")
    
    # Créer un tour initial (0, 1, 2, ...)
    tour_initial = list(range(nb_villes))
    tour_actuel = tour_initial.copy()
    distance_actuelle = calculer_distance_tour(tour_actuel)
    
    afficher_tour(tour_actuel, distance_actuelle, "Tour initial")
    
    nb_iterations = 0
    amelioration = True
    
    while amelioration:
        nb_iterations += 1
        print(f"\n--- Itération {nb_iterations} ---")
        
        # Trouver le meilleur voisin
        nouveau_tour, nouvelle_distance = trouver_meilleur_voisin(tour_actuel)
        
        # Vérifier s'il y a eu amélioration
        if nouvelle_distance < distance_actuelle:
            tour_actuel = nouveau_tour
            distance_actuelle = nouvelle_distance
            afficher_tour(tour_actuel, distance_actuelle, f"Meilleur tour (itération {nb_iterations})")
        else:
            amelioration = False
    
    print("\n=== RÉSULTAT FINAL ===")
    print(f"Nombre total d'itérations: {nb_iterations}")
    afficher_tour(tour_actuel, distance_actuelle, "Meilleure solution trouvée")

# Exécuter l'algorithme
if __name__ == "__main__":
    descente_locale_tsp()
