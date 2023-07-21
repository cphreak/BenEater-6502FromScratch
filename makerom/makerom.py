rom = bytearray([0xea] * 0x8000)

with open("rom.bin", "wb") as out_file:
    out_file.write(rom)