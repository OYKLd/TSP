# Problème du Voyageur de Commerce (TSP) - Méthode de Descente Locale

Ce projet implémente une solution au problème du voyageur de commerce (TSP) en utilisant une méthode de descente locale. Le but est de trouver le chemin le plus court pour visiter un ensemble de villes données, en passant par chaque ville exactement une fois et en revenant à la ville de départ.

## Auteurs
- OUATTARA YEO KASSAHM Lydie

## Structure du Projet
- `TSP.py` : Script principal contenant l'implémentation de l'algorithme
- `README.md` : Ce fichier de documentation

## Fonctionnalités
- Implémentation de l'algorithme de descente locale pour le TSP
- Calcul de la distance totale d'un tour
- Recherche du meilleur voisin par échange de deux villes
- Affichage détaillé des tours et des distances
- Gestion d'une matrice de distances prédéfinie pour 11 villes

## Prérequis
- Python 3.x
- Aucune bibliothèque externe n'est requise (seules les bibliothèques standards sont utilisées)

## Comment exécuter
1. Assurez-vous d'avoir Python installé sur votre machine
2. Téléchargez ou clonez ce dépôt
3. Exécutez le script avec la commande :
   ```
   python TSP.py
   ```

## Sortie du programme
Le programme affichera :
- Le tour initial avec sa distance totale
- Les itérations de l'algorithme avec les améliorations trouvées
- Le meilleur tour trouvé avec la distance totale minimale
- Le détail des distances entre chaque paire de villes du tour final

## Personnalisation
Vous pouvez modifier la matrice `distances` dans le code pour résoudre le problème avec un ensemble différent de villes et de distances.

## Notes
- Cet algorithme utilise une méthode de recherche locale et peut tomber dans des optima locaux
- La qualité de la solution dépend fortement du tour initial
- Pour de meilleurs résultats, il est recommandé d'exécuter l'algorithme plusieurs fois avec des tours initiaux différents

## Licence
Ce projet est fourni à des fins éducatives dans le cadre du Master 1.
