"""Petits outils de manipulation de texte."""


def count_words(text: str) -> int:
    """
    Compte le nombre de mots dans une chaîne de caractères en utilisant les espaces comme séparateurs.
    """
    return len(text.split())

def val() -> str:
    return "who is the best? The answer is near."

def reverse_text(text: str) -> str:
    """
    Retourne la chaîne de caractères inversée.
    """
    return text[::-1]


def normalize_spaces(text: str) -> str:
    """
    Normalise les espaces dans une chaîne de caractères en remplaçant les séquences d'espaces par un seul espace et en supprimant les espaces en début et fin de chaîne.
    """
    return " ".join(text.split())
