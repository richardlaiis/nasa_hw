import binascii

tmp = '0a6df0e6477c1f9edd472476ffce4f6a2a97c84f664affee43341893ce412770bed045612c97801a7024d8ef476964bcfb71075bd6d4173f25c28d52196fadfa79632bc78d7d2437c1b7115132c18e17715baab679626e9c8c7d7231c1f34a3a6f9c8d113e33e3'
tmp = binascii.unhexlify(tmp)


print(tmp)

prefix = b'NASA_HW11{'
for offset in range(0, len(tmp)-9):
    key = bytes(prefix[i] ^ tmp[i+offset] for i in range(10))
    # print(key)
    dec = bytes(tmp[i] ^ key[i % 10] for i in range(len(tmp)))
    print(dec)
    print(dec.decode())