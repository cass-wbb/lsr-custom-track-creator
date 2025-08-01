# LEGO Stunt Rally custom track creator

This will (hopefully) become a functional track editor for LEGO Stunt Rally, which is a game I love dearly. 

When this is completed, it should produce a fully functional .trk file, able to be imported into the Stunt Rally folder, or on a floppy disk to play in the game itself.

## An explanation on how the .trk file type works

.trk files are essentially just a bunch of hexadecimals, with only certain lines actually contributing to the final track.
Each track piece has its own hex value, biome value, and two zeroed out bytes, compared to the FF FF bytes when there is not a piece on that spot, and an orientation value.

# How to use this program

By running sb_sp_interface.py, you are able to create an entire single player track for LEGO Stunt Rally, without even opening the game!
When you go through the program, it will prompt you for specific data. Follow the prompts and you should be able to create a track!

When you are ready to export your track, it will ask you for a name, as well as asking if it is complete. I recommend you do not mark it as complete, and check using the in game track editor, to make sure everything is how you want it. Then save in game. It should export to whichever folder you are running the program in, and will export as a .trk file. Afterwards, you will need to put it in one of the saved track locations, described below.

## If when you load a track in the editor, the game crashes:
Simply run the restore.py file and it should make it so it no longer crashes.

## Future plans for this program

* Make alternate versions for multiplayer tracks, as well as tracks containing pieces from multiple biomes
* Add support for decorative pieces

## Current bugs
* Placing multi-piece parts can bring it into out of bounds spaces when placesd on an edge with certain orientations, when you try to make it a part of the path, the game will crash.
* Most multi-piece parts do not show up properly on the preview file

## Special thanks!
Thank you to [Yellow](https://github.com/yellowberryHN) for pointing out a bug with the code, as well as telling me how to write directly in hex!
