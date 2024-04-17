from geopy.distance import geodesic

def distance_entre_points(depart, arrivee):
    """
    Calcule la distance en kilomètres entre deux points GPS.

    Args:
        depart (tuple): Coordonnées GPS du point de départ (latitude, longitude).
        arrivee (tuple): Coordonnées GPS du point d'arrivée (latitude, longitude).

    Returns:
        float: Distance en kilomètres entre les deux points.
    """
    distance = geodesic(depart, arrivee).kilometers
    return distance

if __name__ == "__main__":
    # Entrée des coordonnées du point de départ depuis l'invite de commande
    latitude_depart = float(input("Latitude du point de départ : "))
    longitude_depart = float(input("Longitude du point de départ : "))

    # Entrée des coordonnées du point d'arrivée depuis l'invite de commande
    latitude_arrivee = float(input("Latitude du point d'arrivée : "))
    longitude_arrivee = float(input("Longitude du point d'arrivée : "))

    coord_depart = (latitude_depart, longitude_depart)
    coord_arrivee = (latitude_arrivee, longitude_arrivee)

    distance = distance_entre_points(coord_depart, coord_arrivee)
    print("Distance entre les deux points :", distance, "kilomètres")
