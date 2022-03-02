# AsusBiosRebuilder
A script to rebuild the flash on Asus laptops from .cap files

Scenario:
This repository contains scripts used to recover an Asus x555UA laptop firmware. The laptop was turned off mid-way through a BIOS update, resulting in only half of the firmware on the storage device. The BIOS user settings were intact. The scripts used could be applied to other motherboards.

Simple steps:
Dump flash (with CH341 for example)
Download firmware cap (https://www.asus.com/Laptops/X555UA/HelpDesk_BIOS/)
Extract AMI image using (https://github.com/LongSoft/UEFITool)
Use scripts to identify which part of the current firmware is corrupted and replace it with the new image.
Reflash with the same tool as step 1
Profit?

Interesting things to note:
Back in the olden days, BIOS settings would be stored on a separate memory device from the EEPROM. The EEPROM would store the BIOS alone which makes recovery easy. New UEFI supported motherboards typically use a Flash chip instead and store the BIOS settings in the same place. This chip can contain not only the UEFI parts but a legacy BIOS, apps and settings. This becomes a problem when you want to recover the firmware as you can't just overwrite it back to a fresh start.

On this laptop, Asus used an 8MB Flash chip which was split into 2MB for user settings and 6MB for the firmware. The 6MB can be investigated to find what was corrupted.

TODO: Improve this.
