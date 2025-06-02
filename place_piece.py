import biome_dicts

def place_finish_line(x: int, y: int, orientation: int, elevation: int, biome: str, lines: list):
    """Places the finish line on the track
    
    :param x: The X coordinate to place the finish line on (1-16)
    :param y: The Y coordinate to place the finish line on (1-16)
    :param orientation: determines the direction the finish line will face (1-4)
    :param elevation: The elevation the piece will be at (0-3)
    :param biome: The biome to pull the hex data from
    :param lines: the list of lines
    """
    if orientation < 4 and orientation > 0:
        orientation_hex = "0" + str(orientation)
    else:
        raise ValueError("Orientation must be between 0 and 4")

    if x < 0 or x > 16 or y < 0 or y > 16:
        raise ValueError("Coordinates must be between a 16x16 grid.")
    
    if biome == "city":
        piece_hex = "30 43 00 00"
    elif biome == "desert":
        piece_hex = "1D 47 00 00"
    elif biome == "jungle":
        piece_hex = "65 3B 00 00"
    elif biome == "winter":
        piece_hex = "48 3F 00 00"
    else:
        raise ValueError("Not a biome")
    
    if elevation <= 0:
        elevation_hex = "80 BF"
    elif elevation == 1:
        elevation_hex = "00 41"
    elif elevation == 2:
        elevation_hex = "80 41"
    else:
        elevation_hex = "C0 41"

    lines[y - 1][x - 1] = f"00 00 00 00 00 00 {elevation_hex} {piece_hex} {orientation_hex} 00 00 00\n"

def place_other_part(x: int, y: int, orientation: int, piece_id: str, elevation: int, biome: str, lines: list):
    """Places a piece on the track
    
    :param x: The X coordinate to place the piece on (1-16)
    :param y: The Y coordinate to place the piece on (1-16)
    :param orientation: determines the direction the piece will face (1-4)
    :param piece_id: the ID of the piece. Viewable in supported_track_pieces.txt
    :param elevation: The elevation the piece will be at (0-3)
    :param biome: The biome to pull the hex data from
    :param lines: the list of lines
    """
    if orientation <= 4 and orientation >= 0:
        orientation_hex = "0" + str(orientation)
    else:
        raise ValueError("Orientation must be between 0 and 4")

    if x < 0 or x > 16 or y < 0 or y > 16:
        raise ValueError("Coordinates must be between a 16x16 grid.")
    
    biome_dict = biome_dicts.biome_hex_getter(biome)
    piece_hex = biome_dict[piece_id]

    if elevation <= 0:
        elevation_hex = "80 BF"
    elif elevation == 1:
        elevation_hex = "00 41"
    elif elevation == 2:
        elevation_hex = "80 41"
    else:
        elevation_hex = "C0 41"

    lines[y - 1][x - 1] = f"00 00 00 00 00 00 {elevation_hex} {piece_hex} {orientation_hex} 00 00 00\n"

def clear(lines):
    x = int(input("Which x coordinate would you like to clear? "))
    y = int(input("Which y coordinate would you like to clear? "))

    if x < 0 or x > 16 or y < 0 or y > 16:
        raise ValueError("Coordinates must be between a 16x16 grid.")
    
    lines[y - 1][x - 1] = "00 00 00 00 00 00 80 BF FF FF FF FF 00 00 00 00\n"