def CatAndMouse(x: int, y: int, z: int) -> str:
    distA = abs(x - z)
    distB = abs(y - z)

    if distA == distB :
        return "Mouse C"
    elif distA < distB :
        return "Cat A"
    elif distA > distB :
        return "Cat B"

