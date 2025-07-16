""" Restore a working autosave track file in the event that the one you created crashed the game
Only works if the install folder is the default path
"""

import sb_sp_files.initializer as initializer, sb_sp_files.place_piece as place_piece, sb_sp_files.file_create as file_create
import os

def main():
    proceed = input("If the install location is not the default location, this will only restore the Autosave.trk file from the CD launcher. Continue? y/n ")
    if proceed != "y":
        quit()

    lines = initializer.create_blank_lines()
    preview_lines = initializer.create_readable_lines()
    biome_select = "city"
    day = True
    biome = initializer.biome_day_select(biome_select, day)
    complete = False

    place_piece.place_finish_line(1, 1, 1, 0, biome_select, lines, preview_lines)

    user = os.path.expanduser("~")

    try:
        file_create.create_file("C:\\Program Files (x86)\\LEGO Media\\LEGO Stunt Rally\\SavedTracks\\Autosaved", biome, lines, complete)
    except:
        print("Restore failed. Only works if the LSR install folder is the default install location. Continuing with CD launcher autosave.")
    file_create.create_file(user + "\\AppData\\Local\\VirtualStore\\Program Files (x86)\\LEGO Media\\LEGO Stunt Rally\\SavedTracks\\Autosaved", biome, lines, preview_lines)

if __name__ == "__main__":
    main()
