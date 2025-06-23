import biome_dicts

def place_finish_line(x: int, y: int, orientation: int, elevation: int, biome: str, lines: list, preview_lines: list):
    """Places the finish line on the track
    
    :param x: The X coordinate to place the finish line on (1-16)
    :param y: The Y coordinate to place the finish line on (1-16)
    :param orientation: determines the direction the finish line will face (1-4)
    :param elevation: The elevation the piece will be at (0-3)
    :param biome: The biome to pull the hex data from
    :param lines: the list of lines for the output file
    :param preview_lines: the list of lines for the preview file
    """

    # set the orientation byte
    advance = False
    while not advance:
        if orientation <= 3 and orientation >= 0:
            orientation_hex = "0" + str(orientation)
            advance = True
        else:
            print("Orientation must be between 0 and 3.")
            orientation = int(input("Which way would you like the piece to face? 0 for bottom left, 1 for top left, 2 for top right, 3 for bottom right "))

    # Set the coordinates
    advance = False
    while not advance:
        if x < 0 or x > 16 or y < 0 or y > 16:
            print("Coordinates must be between a 16x16 grid.")
            if x < 0 or x > 16:
                x = int(input("Where would you like the finish line's X coordinate to be? 1 is the right side, and 16 is the left. "))
            if y < 0 or y > 16:
                y = int(input("Where would you like the finish line's Y coordinate to be? 1 is the top and 16 is the bottom. "))
        else:
            advance = True
    
    # Set the biome, this should never have to ask for the biome, as it should be handled by the interfact file. This is just here as a backup.
    advance = False
    while not advance:
        if biome == "city":
            piece_hex = "30 43 00 00"
            advance = True
        elif biome == "desert":
            piece_hex = "1D 47 00 00"
            advance = True
        elif biome == "jungle":
            piece_hex = "65 3B 00 00"
            advance = True
        elif biome == "winter":
            piece_hex = "48 3F 00 00"
            advance = True
        else:
            print("Not a biome")
            biome = input("Which biome would you like to use? ").lower()
    
    # Set the elevation
    if elevation <= 0:
        elevation_hex = "80 BF"
    elif elevation == 1:
        elevation_hex = "00 41"
    elif elevation == 2:
        elevation_hex = "80 41"
    else:
        elevation_hex = "C0 41"

    lines[y - 1][x - 1] = f"00 00 00 00 00 00 {elevation_hex} {piece_hex} {orientation_hex} 00 00 00\n"

    # Here and below is for preview file
    # Determines whether or not the x coordinate is the last one on the right
    if x != 1:
        preview_lines[y - 1][16 - x] = f"Finish Line\t"
    else:
        preview_lines[y - 1][16 - x] = f"Finish Line\n"

def place_other_part(x: int, y: int, orientation: int, piece_id: str, elevation: int, biome: str, lines: list, preview_lines: list):
    """Places a piece on the track
    
    :param x: The X coordinate to place the piece on (1-16)
    :param y: The Y coordinate to place the piece on (1-16)
    :param orientation: determines the direction the piece will face (1-4)
    :param piece_id: the ID of the piece. Viewable in supported_track_pieces.txt
    :param elevation: The elevation the piece will be at (0-3)
    :param biome: The biome to pull the hex data from
    :param lines: the list of lines for the output file
    :param preview_lines: The list of lines for the preview file
    """
    # Sets orientation byte
    advance = False
    while not advance:
        if orientation <= 3 and orientation >= 0:
            orientation_hex = "0" + str(orientation)
            advance = True
        else:
            print("Orientation must be between 0 and 3.")
            orientation = int(input("Which way would you like the piece to face? 0 for bottom left, 1 for top left, 2 for top right, 3 for bottom right "))

    # Sets coordinates
    advance = False
    while not advance:
        if x < 0 or x > 16 or y < 0 or y > 16:
            print("Coordinates must be between a 16x16 grid.")
            if x < 0 or x > 16:
                x = int(input("Where would you like the piece's X coordinate to be? 1 is the right side, and 16 is the left. "))
            if y < 0 or y > 16:
                y = int(input("Where would you like the piece's Y coordinate to be? 1 is the top and 16 is the bottom. "))
        else:
            advance = True
    
    # sets biome byte
    biome_dict = biome_dicts.biome_hex_getter(biome)
    piece_hex = biome_dict[piece_id]

    # sets elevation byte
    if elevation <= 0:
        elevation_hex = "80 BF"
    elif elevation == 1:
        elevation_hex = "00 41"
    elif elevation == 2:
        elevation_hex = "80 41"
    else:
        elevation_hex = "C0 41"

    # Sets the line to the correct data
    lines[y - 1][x - 1] = f"00 00 00 00 00 00 {elevation_hex} {piece_hex} {orientation_hex} 00 00 00\n"

    # Here and below is for preview file
    # Sets biome and name data
    id_dict = biome_dicts.id_to_name()
    piece_name = id_dict[piece_id]

    # Determines whether or not the x coordinate is the last one on the right
    if x != 1:
        preview_lines[y - 1][16 - x] = f"{piece_name}\t"
    else:
        preview_lines[y - 1][16 - x] = f"{piece_name}\n"

    # # Next section is for using multi-spot pieces in the preview file, not implemented yet.
    # if piece_id == "bumps" or piece_id == "box" or piece_id == "tbar" or piece_id == "loop" or piece_id == "mud" or piece_id == "sjump" or piece_id == "rtrap" or piece_id == "cannon":
    #     # Code here to determine the other spot that is covered, and put that piece in the preview file
    #     if orientation == 1:
    #         if x != 16:
    #             preview_lines[y - 1][16 - (x + 1)] = f"{piece_name}\t"
    #         else:
    #             # clear the spot in the preview file, as it will not show in game
    #             preview_lines[y - 1][16 - x] = "-\t"
    #     elif orientation == 0:
    #         if y != 16:
    #             if x != 1:
    #                 preview_lines[y][16 - x] = f"{piece_name}\t"
    #             else:
    #                 preview_lines[y][16 - x] = f"{piece_name}\n"
    #         else:
    #             # clear the spot in the preview file, as it will not show in game
    #             if x != 1:
    #                 preview_lines[y][16 - x] = "-\t"
    #             else:
    #                 preview_lines[y][16 - x] = "-\n"
    #     elif orientation == 2:
    #         # Basically the opposite of 0
    #         pass
    #     else:  # orientation == 3
    #         # Basically the opposite of 1
    #         pass

    # elif piece_id == "splat" or piece_id == "turbo" or piece_id == "bumper" or piece_id == "traction" or piece_id == "freeze" or piece_id == "random":
    #     # Code here to determine the other spot that is covered, and put that piece in the preview file
    #     pass
    # elif piece_id == "3l":
    #     # Code here to determine the other two spots covered, put that in the preview
    #     pass
    # elif piece_id == "lcurve" or piece_id == "wlcurve" or piece_id == "dtwist" or piece_id == "factory":
    #     # Code here to determind the other three spots covered, put in preview
    #     pass

def clear(lines: list, preview_lines: list):
    """ Clears a given spot in the file

    :param lines: The list of lines for the output file
    :param preview_lines: The list of lines for the preview file
    """
    x = int(input("Which x coordinate would you like to clear? "))
    y = int(input("Which y coordinate would you like to clear? "))

    # Checks for errors in the coordinates
    advance = False
    while not advance:
        if x < 0 or x > 16 or y < 0 or y > 16:
            print("Coordinates must be between a 16x16 grid.")
            if x < 0 or x > 16:
                x = int(input("Which x coordinate would you like to clear? "))
            if y < 0 or y > 16:
                y = int(input("Which y coordinate would you like to clear? "))
        else:
            advance = True
    
    lines[y - 1][x - 1] = "00 00 00 00 00 00 80 BF FF FF FF FF 00 00 00 00\n"

    # Here and below is for preview file
    if x != 1:
        preview_lines[y - 1][16 - x] = f"-\t"
    else:
        preview_lines[y - 1][16 - x] = f"-\n"