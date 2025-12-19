def create_blank_lines() -> list[list[str]]:
    """ Creates blank lines to be used for track pieces
    This function works only for single player tracks.

    :return: The list of blank lines, represented in hex
    """
    lines = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for element in lines:
        i = 0
        while i < 16:
            element.append(b"\x00\x00\x00\x00\x00\x00\x80\xBF\xFF\xFF\xFF\xFF\x00\x00\x00\x00")
            i += 1
    return lines

def biome_day_select(biome: str, day: bool) -> str:
    """ Selects a biome and if it is day/night for the background
    This function only works for single player tracks.
    
    :param biome: The name of the biome to use for this level.
    :return: the single player biome header
    """
    if day:
        day_night = b"\x00"
    else:
        day_night = b"\x01"

    advance = False
    while not advance:
        if biome == "city":
            biome_byte = b"\x03"
            advance = True
        elif biome == "desert":
            biome_byte = b"\x02"
            advance = True
        elif biome == "jungle":
            biome_byte = b"\x00"
            advance = True
        elif biome == "winter":
            biome_byte = b"\x01"
            advance = True
        else:
            biome = input("Biome not available. Please type one of the following:\ncity, desert, jungle, winter").lower()
    
    return b"\x28\x00\x01\x00\x01\x00\x00\x00" + biome_byte + b"\x00\x00\x00" + day_night + b"\x00\x00\x00"

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
