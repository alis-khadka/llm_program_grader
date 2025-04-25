from typing import List, Union


def opt(preise: List[int]) -> int:
    anzahl_angebote = len(preise)
    maximales_gehalt = [None] * anzahl_angebote
    
    maximales_gehalt[0] = preise[0]
    if anzahl_angebote > 1:
        maximales_gehalt[1] = max(preise[:2])
    
    return Gehaltsoptimierung(anzahl_angebote - 1, maximales_gehalt, preise)


def Gehaltsoptimierung(km: int, maximales_gehalt: List[Union[int, None]], preise: List[int]) -> int:
    if maximales_gehalt[km] is None:
        maximales_gehalt[km] = max(Gehaltsoptimierung(km - 2, maximales_gehalt, preise) + preise[km],
                                   Gehaltsoptimierung(km - 1, maximales_gehalt, preise))
    return maximales_gehalt[km]