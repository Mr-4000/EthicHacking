fin = open("flag.opera", "rb")
fin_data = fin.read()

for i in range(1, 0xff + 1):
    fout = open("flag.{}".format(i), "wb")
    data = bytearray(fin_data)
    for j, item in enumerate(data):
        data[j] = item ^ i
    fout.write(data)
    fout.close()