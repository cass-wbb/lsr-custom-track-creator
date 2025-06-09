import initializer, place_piece, file_create

def main():
    lines = initializer.create_blank_lines()
    preview_lines = initializer.create_readable_lines()
    biome_select = input("Which biome would you like to use? ").lower()
    if input("Do you want it to be day or night? ").lower() == "day":
        day = True
    else:
        day = False
    biome = initializer.biome_day_select(biome_select, day)
    complete = False

    # interactive finish line placment here
    x = int(input("Where would you like the finish line's X coordinate to be? 1 is the right side, and 16 is the left. "))
    y = int(input("Where would you like the finish line's Y coordinate to be? 1 is the top and 16 is the bottom. "))
    orientation = int(input("Which way would you like the finish line to face? 0 for bottom left, 1 for top left, 2 for top right, 3 for bottom right "))
    elevation = int(input("How elevated would you like your piece to be? 0-3 "))
    place_piece.place_finish_line(x, y, orientation, elevation, biome_select, lines, preview_lines)

    # interactive other piece placement here
    end = False
    while not end:
        if input("Would you like to continue adding pieces to the track? y/n ") == "n":
            end = True
        else:
            id = input("Enter the track piece ID that you want to add. Track piece IDs are listed in supported_track_pieces.txt. If you want to clear a spot, type clear. If you want to make a preview file, type preview. ")
            if id == "clear":
                place_piece.clear(lines, preview_lines)
            elif id == "preview":
                preview_file_name = input("What would you like the preview file name to be? ")
                file_create.create_preview(preview_file_name, biome_select, preview_lines)
            else:
                x = int(input("Where would you like the piece's X coordinate to be? 1 is the right side, and 16 is the left. "))
                y = int(input("Where would you like the piece's Y coordinate to be? 1 is the top and 16 is the bottom. "))
                orientation = int(input("Which way would you like the piece to face? 0 for bottom left, 1 for top left, 2 for top right, 3 for bottom right "))
                elevation = int(input("How elevated would you like your piece to be? 0-3 "))

                place_piece.place_other_part(x, y, orientation, id, elevation, biome_select, lines, preview_lines)

    # place_piece.place_finish_line(1, 2, 1, 0, "city", lines)
    # place_piece.place_other_part(1, 1, 0, "curve", 0, "city", lines)
    # place_piece.place_other_part(2, 1, 1, "wcurve", 0, "city", lines)
    # place_piece.place_other_part(2, 2, 1, "wtrack", 0, "city", lines)
    # place_piece.place_other_part(2, 3, 2, "curve", 0, "city", lines)
    # place_piece.place_other_part(1, 3, 3, "curve", 0, "city", lines)

    name = input("What would you like the track to be named? ")
    if input("Would you like the file to be marked as complete? It is recommended that you check it in the in-game track editor to make sure everything is working properly. y/n ") == "y":
        complete = True

    file_create.create_file(name, biome, lines, complete)

if __name__ == "__main__":
    main()