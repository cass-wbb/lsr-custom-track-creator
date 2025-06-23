# LEGO Stunt Rally custom track creator

This will (hopefully) become a functional track editor for LEGO Stunt Rally, which is a game I love dearly. 

When this is completed, it should produce a fully functional .trk file, able to be imported into the Stunt Rally folder, or on a floppy disk to play in the game itself.

As this is very much a work in progress, it likely won't do any of that for quite a while.

## An explanation on how the .trk file type works

.trk files are essentially just a bunch of hexadecimals, with only certain lines actually contributing to the final track.
Each track piece has its own hex value, biome value, and two zeroed out bytes, compared to the FF FF bytes when there is not a piece on that spot, and an orientation value.

# How to use this program

By running sb_sp_interface.py, you are able to create an entire single player track for LEGO Stunt Rally, without even opening the game!
When you go through the program, it will prompt you for specific data. Follow the prompts and you should be able to create a track!

When you are ready to export your track, it will ask you for a name, as well as asking if it is complete. I recommend you do not mark it as complete, and check using the in game track editor, to make sure everything is how you want it. Then save in game. It should export to whichever folder you are running the program in, and will export as a .trk file. Afterwards, you will need to put it in one of the saved track locations, described below.

## Saved track locations
Depending on where you launch the game, you will need to put your custom tracks in different location.
If you launch it from the launcher on the CD, put the track in your install path in the SavedTracks folder.
C:\Program Files (x86)\LEGO Media\LEGO Stunt Rally\SavedTracks is the default install path.

If you launch it from the installed launcher, put the track at the following:
%userprofile%\AppData\Local\VirtualStore\Program Files (x86)\LEGO Media\LEGO Stunt Rally\SavedTracks

You can also put it in the root of the A:\ drive, whether that's a real floppy disk or just anything that's mounted there.

## If when you load a track in the editor, the game crashes:
Go to the saved track locations seen above, do not go to the root of the A:\ drive, as this is not useful here.
Delete Autosaved.trk
From here, you can copy another one and name it Autosaved.trk to load it on the next time you go into construction, or you can so into construction and just make a new track from there.

### Future plans for this program

* Make it possible to restore a working .trk file in the event that a track crashes
* Make alternate versions for multiplayer tracks, as well as tracks containing pieces from multiple biomes

## Special thanks!
Thank you to [Yellow](https://github.com/yellowberryHN) for pointing out a bug with the code, as well as telling me how to write directly in hex!
