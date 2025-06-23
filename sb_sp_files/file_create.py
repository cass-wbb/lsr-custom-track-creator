def create_file(file_name: str, biome_line: str, track_lines: list, complete: bool):
    """ Creates a .txt file with the hex values used for a .trk file
    
    :param file_name: The name of the file to be created
    :param biome_line: The biome header line
    :param track_lines: The list of track lines
    :param complete: Determines whether or not the track is completed. I reccommend this to be set to false, so you can check it in game first.
    """
    with open(f"{file_name}.trk", 'wb+') as f:
        # Write the header line
        f.write(b"\x4C\x45\x47\x4F\x20\x4D\x4F\x54\x4F\x00\x00\x00\x05\x00\x00\x00")
        f.write(biome_line)
        for element in track_lines:
            for line in element:
                f.write(line)
            for i in range(48):
                # writes 48 blank lines to match a standard track file
                f.write(b"\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00")
        # writes an additional 3072 blank lines to match a standard .trk file
        for i in range(3072):
            f.write(b"\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00")
        if complete:
            f.write(b"\x00\x00\x00\x00\x01\x00\x00\x00")
        else:
            f.write(b"\x00\x00\x00\x00\x00\x00\x00\x00")
        f.close()
    print(f"File created with name {file_name}.trk. Move to a track folder or to the root of the A drive to play.")

def create_preview(file_name: str, biome: str, preview_lines: list):
    """ Creates a .tsv file that can be put in Excel or a similar program
    to see how the track works.
    
    :param file_name: The name of the preview file to be created, as .tsv
    :param biome: The biome data
    :param track_lines: The list of readable lines
    """
    with open(f"{file_name}.tsv", 'w') as preview_file:
        for element in preview_lines:
            for line in element:
                preview_file.write(f"{line}")
        preview_file.close()
    print(f"File created with name {file_name}.tsv. Use excel to view.")
