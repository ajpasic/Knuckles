XBOX 360 Controller emulator v3.0 for PC games using XINPUT.

This program will add more controller support for Games for Windows.

Notes:
Tested with Logitech Cordless Rumblepad 2 & Logitech G25 Racing Wheel.
Tested with the following PC Games
Juiced 2: HIN
Crysis WARHEAD
GTAIV
GRID
MotoGP 08
The Club
Kane & Lynch
Sega Rally
Bionic Commando
SpiderMan Web of Shadows
Unreal Tournament 3
Shadowrun
Fallout 3
Flatout 2 Ultimate Carnage
and the new
Lord of the Rings Conquest
Mirror's Edge (with some mapping bugs) 

It is not working with
Gears of War
007 Quantum of Solace 

The xinput dll can go by several names, you can rename the dll to those below till you find one that works
xinput9_1_0.dll
xinput1_3.dll
xinput1_2.dll
xinput1_1.dll

GTAIV uses xinput9_1_0.dll
GTAIV v1.1 info:
Use included dinput8.dll


Look at included xbox360cemu.ini for config help

Installation:
Extract xinput1_3.dll, xbox360cemu.ini file to the game exe directory.
Rename DLL if needed
Extract dinput8.dll file to the game exe directory if you want to hide your controller from the game.
**DO NOT REPLACE SYSTEM FILES**

Uninstallation:
Delete xbox360cemu.ini, xinput1_3.dll file.

Usage:
When the game starts you should hear a beep from your PC speaker.  
If you do not have a PC speaker you may not hear the beep, but it will still work.
Play the game as normal.

History:

1\12\09
Major improvements to Force Feedback (with default settings)
Added Fade In/Out for Force Feedback vibration
Added Spring Effect for Force Feedback Wheels
Added Inertia Effect for Force Feedback Wheels
Added UseAutoPad variable (automatically make any pad PAD1 after detecting movement)
Added UseInitBeep variable
Added lots of new Force Feedback options
Added ability to map slider to Left/Right trigger
Added ability to map buttons to Analog axis
Added Non-Linear adjustments to Analog axis
Added new comments to included ini file
Added hotkey F9 to reload config file and reinit
Fixed bug with non Force Feedback controller detection
Fixed bug with swapped Left/Right trigger
Fixed more DLL exit bugs?
Fixed a slider axis map bug?
Small changes to XInput Test Utility



1\9\09
More Imrovements to Force Feedback (removed a start flag)
DLL now exits properly
Higher axis Resolution


1\8\09
Added support for 4 controllers PAD1 to PAD4
Improved Force Feedback Support (INFINITE effect time)
Added ForceFeedbackStrength variable (default 100, use 0-999)
Added Index variable for controller index (use -1 for disable)
Added Crysis WARHEAD support (added packetnumber)
Added Test Utility (uses xinput1_3.dll)
Added variable SteeringWheel (this will fix force feedback effects for wheels)
Added ability to disable an axis (set axis to 7)


12\8\08
Added Force Feedback Support (add UseForceFeedback=1 to xbox360cemu.ini file)
Changed INI Location

Contact/Credits/Donate:
Made by Racer_S http://tocaedit.com
Credits go to MSDN and pkt-zer0.
You like this? I like donations!  http://tocaedit.com/donate


