def create_blank_lines() -> list[list[str]]:
    """ Creates blank lines to be used for track pieces
    This function works only for single player tracks.

    :return: The list of blank lines, represented in hex
    """
    lines = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for element in lines:
        i = 0
        while i < 16:
            element.append("00 00 00 00 00 00 80 BF FF FF FF FF 00 00 00 00\n")
            i += 1
    return lines

def biome_day_select(biome: str, day: bool) -> str:
    """ Selects a biome and if it is day/night for the background
    This function only works for single player tracks.
    
    :param biome: The name of the biome to use for this level.
    :return: the single player biome header
    """
    if day:
        day_night = "00"
    else:
        day_night = "01"

    advance = False
    while not advance:
        if biome == "city":
            biome_byte = "03"
            advance = True
        elif biome == "desert":
            biome_byte = "02"
            advance = True
        elif biome == "jungle":
            biome_byte = "00"
            advance = True
        elif biome == "winter":
            biome_byte = "01"
            advance = True
        else:
            biome = input("Biome not available. Please type one of the following:\ncity, desert, jungle, winter").lower()
    
    return f"28 00 01 00 01 00 00 00 {biome_byte} 00 00 00 {day_night} 00 00 00\n"

def create_readable_lines() -> list[list[str]]:
    """ Creates blank lines to be used for track pieces
    This function works only for single player tracks.

    :return: The list of blank lines, represented in piece ids
    """
    pieces = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for element in pieces:
        i = 0
        while i < 15:
            element.append("-\t")
            i += 1
        element.append("-\n")
    return pieces