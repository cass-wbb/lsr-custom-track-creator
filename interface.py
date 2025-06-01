import initializer, place_piece, file_create

def main():
    lines = initializer.create_blank_lines()
    biome = initializer.biome_day_select("city", True)
    complete = False
    place_piece.place_finish_line(1, 2, 1, 0, "city", lines)
    place_piece.place_other_part(1, 1, 0, "curve", 0, "city", lines)
    place_piece.place_other_part(2, 1, 1, "wcurve", 0, "city", lines)
    place_piece.place_other_part(2, 2, 1, "wtrack", 0, "city", lines)
    place_piece.place_other_part(2, 3, 2, "curve", 0, "city", lines)
    place_piece.place_other_part(1, 3, 3, "curve", 0, "city", lines)

    file_create.create_file("full_track", biome, lines, complete)

if __name__ == "__main__":
    main()