import biome_dicts

def place_finish_line(y: int, x: int, orientation: int, elevation: int, biome: str, lines: list, preview_lines: list):
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
            if orientation == 0:
                orientation_hex = b"\x00"
            elif orientation == 1:
                orientation_hex = b"\x01"
            elif orientation == 2:
                orientation_hex = b"\x02"
            elif orientation == 3:
                orientation_hex = b"\x03"
            advance = True
        else:
            print("Orientation must be between 0 and 3.")
            orientation = int(input("Which way would you like the piece to face? 0 for bottom left, 1 for top left, 2 for top right, 3 for bottom right "))

    # Set the coordinates
    advance = False
    while not advance:
        if y < 0 or y > 16 or x < 0 or x > 16:
            print("Coordinates must be between a 16x16 grid.")
            if y < 0 or y > 16:
                y = int(input("Where would you like the finish line's X coordinate to be? 1 is the right side, and 16 is the left. "))
            if x < 0 or x > 16:
                x = int(input("Where would you like the finish line's Y coordinate to be? 1 is the top and 16 is the bottom. "))
        else:
            advance = True
    
    # Set the biome, this should never have to ask for the biome, as it should be handled by the interfact file. This is just here as a backup.
    advance = False
    while not advance:
        if biome == "city":
            piece_hex = b"\x30\x43\x00\x00"
            advance = True
        elif biome == "desert":
            piece_hex = b"\x1D\x47\x00\x00"
            advance = True
        elif biome == "jungle":
            piece_hex = b"\x65\x3B\x00\x00"
            advance = True
        elif biome == "winter":
            piece_hex = b"\x48\x3F\x00\x00"
            advance = True
        else:
            print("Not a biome")
            biome = input("Which biome would you like to use? ").lower()
    
    # Set the elevation
    if elevation <= 0:
        elevation_hex = b"\x80\xBF"
    elif elevation == 1:
        elevation_hex = b"\x00\x41"
    elif elevation == 2:
        elevation_hex = b"\x80\x41"
    else:
        elevation_hex = b"\xC0\x41"

    lines[x - 1][y - 1] = b"\x00\x00\x00\x00\x00\x00" + elevation_hex + piece_hex + orientation_hex + b"\x00\x00\x00"

    # Here and below is for preview file
    # Determines whether or not the x coordinate is the last one on the right
    if x != 1:
        preview_lines[y - 1][16 - x] = f"Finish Line\t"
    else:
        preview_lines[y - 1][16 - x] = f"Finish Line\n"

def place_other_part(y: int, x: int, orientation: int, piece_id: str, elevation: int, biome: str, lines: list, preview_lines: list):
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
    # set the orientation byte
    advance = False
    while not advance:
        if orientation <= 3 and orientation >= 0:
            if orientation == 0:
                orientation_hex = b"\x00"
            elif orientation == 1:
                orientation_hex = b"\x01"
            elif orientation == 2:
                orientation_hex = b"\x02"
            elif orientation == 3:
                orientation_hex = b"\x03"
            advance = True
        else:
            print("Orientation must be between 0 and 3.")
            orientation = int(input("Which way would you like the piece to face? 0 for bottom left, 1 for top left, 2 for top right, 3 for bottom right "))

    # Sets coordinates
    advance = False
    while not advance:
        if y < 0 or y > 16 or x < 0 or x > 16:
            print("Coordinates must be between a 16x16 grid.")
            if y < 0 or y > 16:
                y = int(input("Where would you like the piece's X coordinate to be? 1 is the right side, and 16 is the left. "))
            if x < 0 or x > 16:
                x = int(input("Where would you like the piece's Y coordinate to be? 1 is the top and 16 is the bottom. "))
        else:
            advance = True
    
    # sets pice hex
    biome_dict = biome_dicts.biome_hex_getter(biome)
    piece_hex = biome_dict[piece_id]

    # Set the elevation
    if elevation <= 0:
        elevation_hex = b"\x80\xBF"
    elif elevation == 1:
        elevation_hex = b"\x00\x41"
    elif elevation == 2:
        elevation_hex = b"\x80\x41"
    else:
        elevation_hex = b"\xC0\x41"

    # Sets the line to the correct data
    lines[x - 1][y - 1] = b"\x00\x00\x00\x00\x00\x00" + elevation_hex + piece_hex + orientation_hex + b"\x00\x00\x00"

    # Here and below is for preview file
    # Sets biome and name data
    id_dict = biome_dicts.id_to_name()
    piece_name = id_dict[piece_id]

    # Determines whether or not the x coordinate is the last one on the right
    if x != 1:
        preview_lines[y - 1][16 - x] = f"{piece_name}\t"
    else:
        preview_lines[y - 1][16 - x] = f"{piece_name}\n"

    # Next section is for using multi-spot pieces in the preview file
    if piece_id == "tbar" or piece_id == "loop" or piece_id == "mud" or piece_id == "sjump" or piece_id == "rtrap" or piece_id == "cannon":
        # Code here to determine the other spot that is covered, and put that piece in the preview file
        if orientation == 1:
            if x != 16:
                preview_lines[y - 1][16 - (x + 1)] = f"{piece_name}\t"
            else:
                # clear the original spot in the preview file, as it will not show in game
                preview_lines[y - 1][16 - x] = "-\t"
        elif orientation == 0:
            if y != 16:
                if x != 1:
                    preview_lines[y][16 - x] = f"{piece_name}\t"
                else:
                    preview_lines[y][16 - x] = f"{piece_name}\n"
            else:
                # clear the original spot in the preview file, as it will not show in game
                if x != 1:
                    preview_lines[y - 1][16 - x] = "-\t"
                else:
                    preview_lines[y - 1][16 - x] = "-\n"
        
        elif orientation == 2:
            if y != 16:
                if x != 1:
                    preview_lines[y - 1][15 - x] = f"{piece_name}\t"
                else:
                    preview_lines[y - 1][15 - x] = f"{piece_name}\n"
            else:
                # clear the original spot in the preview file, as it will not show in game
                if y != 1:
                    preview_lines[y- 1][16 - x] = "-\t"
                else:
                    preview_lines[y - 1][16 - x] = "-\n"

        else:  # orientation == 3
            if x != 1:
                if x != 2:
                    preview_lines[y - 1][16 - (x - 1)] = f"{piece_name}\t"
                else:
                    preview_lines[y - 1][16 - (x - 1)] = f"{piece_name}\n"
            else:
                # clear the original spot in the preview file, as it will not show in game
                if x != 1:
                    preview_lines[y - 1][16 - x] = "-\t"
                else:
                    preview_lines[y - 1][16 - x] = "-\n"

    # elif piece_id == "splat" or piece_id == "turbo" or piece_id == "bumper" or piece_id == "traction" or piece_id == "freeze" or piece_id == "random":
    #     # Code here to determine the other spot that is covered, and put that piece in the preview file
    #     pass

    elif piece_id == "3l":
        # Code here to determine the other two spots covered, put that in the preview
        if orientation == 1:
            if x < 15:
                preview_lines[y - 1][16 - (x + 1)] = f"{piece_name}\t"
                preview_lines[y - 1][16 - (x + 2)] = f"{piece_name}\t"
            else:
                # clear the original spot in the preview file, as it will not show in game
                preview_lines[y - 1][16 - x] = "-\t"
        elif orientation == 0:
            if y < 15:
                if x != 1:
                    preview_lines[y][16 - x] = f"{piece_name}\t"
                    preview_lines[y + 1][16 - x] = f"{piece_name}\t"
                else:
                    preview_lines[y][16 - x] = f"{piece_name}\n"
                    preview_lines[y + 1][16 - x] = f"{piece_name}\n"
            else:
                # clear the original spot in the preview file, as it will not show in game
                if x != 1:
                    preview_lines[y - 1][16 - x] = "-\t"
                else:
                    preview_lines[y - 1][16 - x] = "-\n"
        
        elif orientation == 2:
            if y != 16:
                if x != 1:
                    preview_lines[y - 1][15 - x] = f"{piece_name}\t"
                    preview_lines[y - 1][14 - x] = f"{piece_name}\t"
                else:
                    preview_lines[y - 1][15 - x] = f"{piece_name}\n"
                    preview_lines[y - 1][14 - x] = f"{piece_name}\n"
            else:
                # clear the original spot in the preview file, as it will not show in game
                if y != 1:
                    preview_lines[y- 1][16 - x] = "-\t"
                else:
                    preview_lines[y - 1][16 - x] = "-\n"

        else:  # orientation == 3
            if x != 1:
                if x != 2:
                    preview_lines[y - 1][16 - (x - 1)] = f"{piece_name}\t"
                    preview_lines[y - 1][16 - (x - 2)] = f"{piece_name}\t"
                else:
                    preview_lines[y - 1][16 - (x - 1)] = f"{piece_name}\n"
                    preview_lines[y - 1][16 - (x - 2)] = f"{piece_name}\n"
            else:
                # clear the original spot in the preview file, as it will not show in game
                if x != 1:
                    preview_lines[y - 1][16 - x] = "-\t"
                else:
                    preview_lines[y - 1][16 - x] = "-\n"

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
    
    lines[y - 1][x - 1] = b"\x00\x00\x00\x00\x00\x00\x80\xBF\xFF\xFF\xFF\xFF\x00\x00\x00\x00"

    # Here and below is for preview file
    if x != 1:
        preview_lines[y - 1][16 - x] = f"-\t"
    else:
        preview_lines[y - 1][16 - x] = f"-\n"
