import sb_sp_files.initializer as initializer, sb_sp_files.place_piece as place_piece, sb_sp_files.file_create as file_create

def main():
    lines = initializer.create_blank_lines()
    preview_lines = initializer.create_readable_lines()
    biome_select = input("Which biome would you like to use? ").lower()
    advance = False
    while not advance:
        if biome_select != "city" and biome_select != "desert" and biome_select != "jungle" and biome_select != "winter":
            print("That is not a biome. Please type city, desert, jungle, or winter.")
            biome_select = input("Which biome would you like to use? ").lower()
        else:
            advance = True
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
    place_piece.place_finish_line(y, x, orientation, elevation, biome_select, lines, preview_lines)

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

                try:
                    place_piece.place_other_part(y, x, orientation, id, elevation, biome_select, lines, preview_lines)
                except KeyError:
                    print("Track piece name invalid.")

    name = input("What would you like the track to be named? ")
    if input("Would you like the file to be marked as complete? It is recommended that you check it in the in-game track editor to make sure everything is working properly. y/n ") == "y":
        complete = True

    file_create.create_file(name, biome, lines, complete)

if __name__ == "__main__":
    main()
