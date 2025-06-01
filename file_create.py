def create_file(file_name: str, biome_line: str, track_lines: list, complete: bool):
    """ Creates a .txt file with the hex values used for a .trk file
    
    :param file_name: The name of the file to be created
    :param biome_line: The biome header line
    :param track_lines: The list of track lines
    :param complete: Determines whether or not the track is completed. I reccommend this to be set to false, so you can check it in game first.
    """
    with open(f"{file_name}.txt", 'w',) as f:
        # Write the header line
        f.write("4C 45 47 4F 20 4D 4F 54 4F 00 00 00 05 00 00 00\n")
        f.write(biome_line)
        for element in track_lines:
            for line in element:
                f.write(f"{line}")
            for i in range(48):
                # writes 48 blank lines to match a standard track file
                f.write("00 00 00 00 00 00 00 00 FF FF FF FF 00 00 00 00\n")
        # writes an additional 3072 blank lines to match a standard .trk file
        for i in range(3072):
            f.write("00 00 00 00 00 00 00 00 FF FF FF FF 00 00 00 00\n")
        if complete:
            f.write("00 00 00 00 01 00 00 00")
        else:
            f.write("00 00 00 00 00 00 00 00")
        f.close()
