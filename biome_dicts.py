def biome_hex_getter(biome: str):
    """ Sets a dictionary for all possible track pieces' hex values.
    
    :param biome: the biome to pull from.
    :return: The dictionary for all the pieces
    """
    track_dict = {}
    if biome == "city":
        track_dict["track"] = "31 43 00 00"
        track_dict["wtrack"] = "36 43 00 00"
        track_dict["curve"] = "33 43 00 00"
        track_dict["wcurve"] = "38 43 00 00"
        track_dict["vent"] = "4A 43 00 00"
        track_dict["slight"] = "51 43 00 00"
        track_dict["covered"] = "40 43 00 00"
        track_dict["sbump"] = "3B 43 00 00"
        track_dict["nlight"] = "8D 43 00 00"
        track_dict["bumps"] = "4B 43 00 00"
        track_dict["box"] = "4C 43 00 00"
        track_dict["isec"] = "49 43 00 00"
        track_dict["ramp"] = "53 43 00 00"
        track_dict["wramp"] = "3C 43 00 00"
        track_dict["aramp"] = "46 43 00 00"
        track_dict["fan"] = "42 43 00 00"
        track_dict["crush"] = "47 43 00 00"
        track_dict["tbar"] = "32 43 00 00"
        track_dict["3l"] = "37 43 00 00"
        track_dict["lcurve"] = "34 43 00 00"
        track_dict["wlcurve"] = "39 43 00 00"
        track_dict["dtwist"] = "41 43 00 00"
        track_dict["loop"] = "45 43 00 00"
        track_dict["mud"] = "43 43 00 00"
        track_dict["sjump"] = "44 43 00 00"
        track_dict["rtrap"] = "48 43 00 00"
        track_dict["cannon"] = "4D 43 00 00"
        track_dict["splat"] = "5C 43 00 00"
        track_dict["turbo"] = "59 43 00 00"
        track_dict["bumper"] = "5B 43 00 00"
        track_dict["traction"] = "58 43 00 00"
        track_dict["freeze"] = "5F 43 00 00"
        track_dict["random"] = "5A 43 00 00"
        track_dict["factory"] = "5D 43 00 00"
    elif biome == "desert":
        pass
    elif biome == "jungle":
        pass
    elif biome == "winter":
        pass

    return track_dict