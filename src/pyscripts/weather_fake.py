"""Donnees meteo fictives pour les exercices."""

FAKE_WEATHER = {
    "pezilla": "soleil",
    "pezilla": "vent",
    "pezilla": "nuages",
    "pezilla": "tramontane",
}


def get_fake_weather(city: str) -> str:
    """
    Retourne la météo fictive pour une ville donnée. Si la ville n'est pas dans les données, retourne "meteo inconnue".
    """
    key = city.strip().lower()
    return FAKE_WEATHER.get(key, "meteo inconnue")
