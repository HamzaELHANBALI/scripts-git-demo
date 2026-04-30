"""Donnees meteo fictives pour les exercices."""

FAKE_WEATHER = {
    "toulouse": "soleil",
    "montpellier": "vent",
    "paris": "nuages",
}


def get_fake_weather(city: str) -> str:
    """
    Retourne la météo fictive pour une ville donnée. Si la ville n'est pas dans les données, retourne "meteo inconnue".
    """
    key = city.strip().lower()
    return FAKE_WEATHER.get(key, "meteo inconnue")
