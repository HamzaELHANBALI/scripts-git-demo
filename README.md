# PyScripts CNAM

Depot fil rouge pour le cours **Git & GitHub**.

L'objectif est de construire progressivement une petite collection de scripts Python :

- session 1 : Git local, commits, historique, branches ;
- session 2 : collaboration, Pull Requests, reviews et conflits.

## Structure

```text
src/pyscripts/   Code Python
tests/           Tests unitaires pytest
```

## Commandes utiles

Installer les outils de developpement :

```bash
python -m pip install -r requirements-dev.txt
```

Lancer les tests :

```bash
PYTHONPATH=src pytest
```

## Idees de contributions

- ajouter une fonction dans `calculator.py` ;
- ajouter un outil de texte dans `text_tools.py` ;
- enrichir le message dans `greetings.py` ;
- ajouter un faux script meteo dans `weather_fake.py` ;
- ajouter un test pour chaque nouvelle fonction.

## Regles de contribution proposees

1. Creer une branche par fonctionnalite.
2. Faire des commits courts et lisibles.
3. Ajouter ou modifier les tests si le comportement change.
4. Ouvrir une Pull Request.
