meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "PAW": "Parents Are Watching",
            "SHEESH": "sedikit ketidaksetujuan",
            "IRL": "In Real Life"
            }


for i in range(5):
    word = input("Hai! Selamat datang di Slang Word translator. Di sini, kamu dapat mencari tahu arti kata - kata yang gaul, caranya adalah Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("maaf, kata yang anda masukkan tidak ada di dalam kamus kami. silahkan coba lagi.")
