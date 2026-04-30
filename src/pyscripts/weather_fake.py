"""Donnees meteo fictives pour les exercices."""

FAKE_WEATHER = {
    "pezilla": "soleil",
    "pezilla": "vent",
    "pezilla": "nuages",
    "pezilla": "tramontane",
}


def get_fake_weather(city: str) -> str:
    key = city.strip().lower()
    return FAKE_WEATHER.get(key, "meteo inconnue")
