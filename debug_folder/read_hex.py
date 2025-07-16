import biome_dicts


current = biome_dicts.biome_hex_getter("city")
errors = []
with open("test2.trk", 'w') as f:
    for key, value in current.items():
        try:
            f.write(value)
        except:
            errors.append(f"{key} (city)")

    current = biome_dicts.biome_hex_getter("desert")
    for key, value in current.items():
        try:
            f.write(value)
        except:
            errors.append(f"{key} (desert)")

    current = biome_dicts.biome_hex_getter("jungle")
    for key, value in current.items():
        try:
            f.write(value)
        except:
            errors.append(f"{key} (jungle)")

    current = biome_dicts.biome_hex_getter("winter")
    for key, value in current.items():
        try:
            f.write(value)
        except:
            errors.append(f"{key} (winter)")

with open("errors.txt", 'w') as a:
    for item in errors:
        a.write(f"{item}\n")
