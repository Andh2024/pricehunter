# ---------------------------------------------------------------------------------------------------
# Zusätzliicher Unit-Test für chf_filter-Funktion aus main.py
# Testet Funktionalität des eingebauten CHF-Filters
# Um diesen Test durchzuführen, muss die temporäre Auskommentierung der Funktion in main.py entfernt werden
# ---------------------------------------------------------------------------------------------------

from main import *


def test_chf_filter():
    # Test erwartet ein Ergebnis im Format eines Strings wie in diesem Fall CHF 5'000
    assert chf_filter(5000) == "CHF 5'000"
