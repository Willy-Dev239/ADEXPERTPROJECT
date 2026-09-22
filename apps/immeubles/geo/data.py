# apps/immeubles/geo/data.py
from .africa import AFRICA
from .europe import EUROPE
from .americas import AMERICAS
from .asia import ASIA
from .oceania import OCEANIA


CONTINENTS = {
    "Afrique":   AFRICA,
    "Europe":    EUROPE,
    "Amériques": AMERICAS,
    "Asie":      ASIA,
    "Océanie":   OCEANIA,
}

# Flat : PAYS → RÉGION → VILLE → QUARTIER
PAYS = {}
for continent, pays_dict in CONTINENTS.items():
    PAYS.update(pays_dict)

CONTINENT_CHOICES = [(c, c) for c in CONTINENTS.keys()]
PAYS_CHOICES = [(p, p) for p in PAYS.keys()]