import random

keyword =  "@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

username = ""

jumlah_username = int(input("Halo! Selamat Datang di Username Generator! Disini kamu dapat menentukan nama username mu jika kamu tidak memiliki ide untuk namanya. Silahkan masukkan angka untuk menentukan panjang usernamemu: "))

for i in range(jumlah_username):
    username += random.choice(keyword)

print(username)
