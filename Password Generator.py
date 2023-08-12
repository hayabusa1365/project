import random

keyword =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password = ""

jumlah_password = int(input("Silahkan masukkan angka untuk menentukan panjang passwordmu: "))

for i in range(jumlah_password):
    password += random.choice(keyword)

print(password)
