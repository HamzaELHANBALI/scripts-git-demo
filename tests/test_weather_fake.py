from pyscripts.weather_fake import get_fake_weather


def test_get_fake_weather_known_city():
    assert get_fake_weather("Toulouse") == "soleil"


def test_get_fake_weather_unknown_city():
    assert get_fake_weather("Lyon") == "meteo inconnue"

def test_get_fake_weather_empty_city(): # Test with an empty city name
    assert get_fake_weather("") == "meteo inconnue" # Test with an empty city name, should return "meteo inconnue"
