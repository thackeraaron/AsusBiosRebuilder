original_file = open("../backup.bin", "rb")
original_firmware = original_file.read()

extracted_file = open("x555uj_firmware_extracted", "rb")
extracted_firmware = extracted_file.read()

#print(original_firmware[-2:])

corrupted_count = 0

for index in range(0, len(extracted_firmware)):
	index_on_original = (len(original_firmware)-1)-index
	index_on_extracted = (len(extracted_firmware)-1)-index

	if original_firmware[index_on_original] == 255:
		corrupted_count += 1
	else:
		corrupted_count = 0

	# if theres a mismatch between updates and theres more than 16 empty bytes, this is the start of the erased section.
	if (not (original_firmware[index_on_original]==extracted_firmware[index_on_extracted])) and (corrupted_count>16):
		print("Error at index ORIGINAL {:02X}".format(index_on_original))
		print("Error at index NEW {:02X}".format(index_on_extracted))
		print()
		print("ORIGINAL : NEW")
		print("{:02X}{:02X} : {:02X}{:02X}".format(
			original_firmware[index_on_original],
			original_firmware[index_on_original+1],
			extracted_firmware[index_on_extracted],
			extracted_firmware[index_on_extracted+1]
			))
		break

# Update note: found its easier to just overlay the entire new rom into the memory backwards
# than to work out whats missing, if there are version mismatches, this should fix it by overwriting
# the old one

new_firmware = bytearray(original_firmware)

#print(new_firmware[0:16])

# loop backwards through original firmware image and get relative index's on both firmwares.
for index in range(0, len(extracted_firmware)):
	index_on_new_firmware = (len(new_firmware)-1)-index
	index_on_extracted = (len(extracted_firmware)-1)-index

	new_firmware[index_on_new_firmware] = extracted_firmware[index_on_extracted]

#print(new_firmware[0:16])

f = open("new_firmware.bin", "wb")
f.write(new_firmware)
f.close()
print("Done: new_firmware.bin")
