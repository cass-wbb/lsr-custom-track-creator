import file_create

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

def biome_select(biome: str) -> str:
    """ Selects a biome for the background
    This function only works for single player tracks.
    
    :param biome: The name of the biome to use for this level.
    :return: the single player biome header
    """
    if biome == "city":
        return "28 00 01 00 01 00 00 00 03 00 00 00 00 00 00 00\n"
    elif biome == "desert":
        return "28 00 01 00 01 00 00 00 02 00 00 00 00 00 00 00\n"
    elif biome == "jungle":
        return "28 00 01 00 01 00 00 00 00 00 00 00 00 00 00 00\n"
    elif biome == "winter":
        return "28 00 01 00 01 00 00 00 01 00 00 00 00 00 00 00\n"
    else:
        raise ValueError("Biome not available. Please type one of the following:\ncity, desert, jungle, winter")

def main():
    lines = create_blank_lines()
    biome = biome_select("city")
    complete = False
    file_create.create_file("test", biome, lines, complete)

if __name__ == "__main__":
    main()