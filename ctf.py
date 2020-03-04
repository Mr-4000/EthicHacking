with open("flag.mid", "rb") as fin:
    fout = open("flag.opera", "wb")
    data = bytearray(fin.read())
    for i, item in enumerate(data):
        data[i] = item ^ 0x66
    fout.write(data)
    fout.close()