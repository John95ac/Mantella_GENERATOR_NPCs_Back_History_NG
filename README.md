# 📜 SKSE "Mantella Adding NPCs Back History NG"

It's a simple yet powerful SKSE DLL that manages the character_overrides stories from the Mantella AI mod. It was created with the objective of allowing players and creators to create and share the stories of NPCs from the base game as mods for the Mantella AI mod.

---

# What does it do?

Each time Skyrim is launched, the DLL will check if your installed mods contain a folder named "Mantella BackHistory". Within these, it will organize each story in .json format.

The first action with this information is:

Check if the character file exists in the folder "My Games\Mantella\data\Skyrim\character_overrides" on your PC. If it exists, it will update it with the version from the installed mod, assuming it is the most updated version.

If the file does not exist in "My Games\Mantella\data\Skyrim\character_overrides", it will copy the version found in the mod folder "Mantella BackHistory".

If the story exists in "My Games\Mantella\data\Skyrim\character_overrides" but not in any part of the mods in their respective folder "Mantella BackHistory", it will deduce that it was deactivated from the mod manager. Thus, the DLL will move this unmanaged character to a new folder called "Repository of Unused Characters" at the location "\My Games\Mantella\data\Skyrim\character_overrides\Repository of Unused Characters".

While performing all these procedures at incredible speed, it will create a file named "Mantella-Adding-NPCs-Back-History-NG.log" at the location "\My Games\Mantella" and "\My Games\Skyrim Special Edition\SKSE" to keep a record of the files.

Additionally, on the startup screen, it will generate a maintenance message when pressing ~. The first message will be "Mantella NPCs Back History loaded successfully > ^ < ."

That's all for now.

# Acknowledgements

Special thanks to mrowrpurr "https://github.com/SkyrimScripting/SKSE_Template_HelloWorld", who created the tutorial for starting with SKSE. It's an incredible piece of work, really good for beginners. "She forgot to mention downloading GIT, but it's a minor detail. If you follow the tutorial without downloading GIT, you'll have a hard time like I did." This work is based solely on what I learned from her tutorials, and of course, my own contributions. I respect her conduct guidelines and license. Here is everything. Thanks, and if you want to learn how to do it, I recommend looking up her videos—they are good.

# CommonLibSSE NG

Because this uses [CommonLibSSE NG](https://github.com/CharmedBaryon/CommonLibSSE-NG), it supports Skyrim SE, AE, GOG, and VR.

[CommonLibSSE NG](https://github.com/CharmedBaryon/CommonLibSSE-NG) is a fork of the popular [powerof3 fork](https://github.com/powerof3/CommonLibSSE) of the _original_ `CommonLibSSE` library created by [Ryan McKenzie](https://github.com/Ryan-rsm-McKenzie) in [2018](https://github.com/Ryan-rsm-McKenzie/CommonLibSSE/commit/224773c424bdb8e36c761810cdff0fcfefda5f4a).

# Requirements

- [Mantella - Bring NPCs to Life with AI](https://www.nexusmods.com/skyrimspecialedition/mods/98631)
- [Address Library for SKSE Plugins](https://www.nexusmods.com/skyrimspecialedition/mods/32444)