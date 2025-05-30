import binascii

tmp = 'af86d71122130038e992819dd8392a053531fc9ac3a1d819265b0735fa94829b9927200e3331b4cfd5cfff1822067b1acfa4a2b0f12372503a64b987bc848a0d1c0c3461b9a881dce640743e2d67bac2d4b08d411c0d713ab8a8d7dae6042f55703ab9c49bd8c4'
tmp = binascii.unhexlify(tmp)


print(tmp)
print(len(tmp))
prefix = b'NASA_HW11{'

for i in range(len(tmp)):
    key = bytes(tmp[i+j] ^ prefix[j] for j in range(10))
    dec = bytes(tmp[j] ^ key[(j-i) % 10] for j in range(len(tmp)))
    print(dec)