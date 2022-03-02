
import os

import struct

a = open("target.bin", "wb")

fil = "x555uj_firmware_extracted"

print((8388608 - os.path.getsize(fil)))

os.exit(0)

for i in range(0, (6291456 - os.path.getsize(fil))):
	a.write(struct.pack('B', 0xFF))

with open(fil, "rb") as f:
	while True:
		section = f.read(1)
		if section:
			a.write(section)
		else:
			break
	# Do stuff with byte.
	

a.close()
