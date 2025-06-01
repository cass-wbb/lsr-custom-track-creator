# LEGO Stunt Rally custom track creator

This will (hopefully) become a functional track editor for LEGO Stunt Rally, which is a game I love dearly. 

When this is completed, it should produce a fully functional .trk file, able to be imported into the Stunt Rally folder, or on a floppy disk to play in the game itself.

As this is very much a work in progress, it likely won't do any of that for quite a while.

As of right now, it only supports creating a completely empty track file, not including a finish line, meaning you currently can't race on it. It also outputs to a plain text file, which will need to be put into a hex editor and saved as a .trk file to bring it in game.

## An explanation on how the .trk file type works

.trk files are essentially just a bunch of hexadecimals, with only certain lines actually contributing to the final track.
Each track piece has its own hex value, biome value, and two zeroed out bytes, compared to the FF FF bytes when there is not a piece on that spot, and an orientation value.
