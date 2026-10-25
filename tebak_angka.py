import random

rahasia = random.randint(1, 100)
percobaan = 0
print("tebak angka 1 sampai 100")

while True:
    tebakan = int(input("tebakanmu: "))
    percobaan += 1

    if tebakan < rahasia:
        print('terlalu kecil')
    elif tebakan > rahasia:
        print("terlalu besar")       
    else:
        print(f"benar! kamu berhasil dalam {percobaan} percobaan")
        break