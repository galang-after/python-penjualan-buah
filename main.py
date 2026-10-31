
# Menyimpan nama buah dan harga masing-masing
daftar_buah = ["mangga", "apel", "jeruk", "melon", "alpukat", "nanas"]
daftar_harga = [7500, 10000, 8000, 21000, 11500, 17000]

# Menggabungkan nama buah dan harganya ke dalam dictionary
etalase = dict(zip(daftar_buah, daftar_harga))

# Mengecek apakah pengguna ingin melihat daftar buah
cek_stok_buah = input("Cek ketersediaan buah ya/tidak: ").lower()

if cek_stok_buah == "ya":
    print(f"Daftar jenis buah: {list(etalase)}")
else:
    print("Selesai")

# Mengecek apakah pengguna ingin melihat harga buah
cek_harga_buah = input("Cek harga buah ya/tidak: ").lower()

if cek_harga_buah == "ya":
    print("Daftar harga buah:")

    # Menampilkan nama dan harga setiap buah
    for buah, harga in etalase.items():
        print(f"{buah.capitalize():10} : Rp {harga:,.0f}")
else:
    print("Selesai")

# Menanyakan apakah pengguna ingin membeli buah
beli_buah = input("Apakah ingin membeli buah? ya/tidak: ").lower()

if beli_buah == "ya":

    # Mengulang pemilihan jika buah atau jumlah yang dimasukkan tidak valid
    while True:
        membeli = input("Mau membeli buah apa? ").lower()

        # Memastikan buah yang dipilih tersedia di etalase
        if membeli not in etalase:
            print(f"{membeli} tidak tersedia. Coba lagi.")
            continue

        print("- Berhasil memilih buah")

        # Meminta jumlah buah yang ingin dibeli
        try:
            jumlah = int(input("Berapa banyak buah? "))

            # Jumlah pembelian harus lebih dari nol
            if jumlah <= 0:
                print("Jumlah buah harus lebih dari 0.")
                continue

        # Menangani input jika bukan berupa angka bulat
        except ValueError:
            print("Jumlah harus berupa angka bulat.")
            continue

        print("- Berhasil menambahkan jumlah")

        # Menghitung total harga berdasarkan jumlah pembelian
        harga_buah = etalase[membeli]
        total = harga_buah * jumlah

        # Menentukan diskon berdasarkan total belanja
        diskon_harga = total

        if diskon_harga > 150000:
            diskon = 10
        elif diskon_harga > 100000:
            diskon = 5
        elif diskon_harga > 75000:
            diskon = 3
        else:
            diskon = 0

        # Menghitung potongan harga dan total setelah diskon
        jumlah_diskon = diskon_harga * (diskon / 100)
        total_diskon = diskon_harga - jumlah_diskon

        # Menampilkan ringkasan pembelian
        print("=" * 40)
        print(f"Kategori Buah  : {membeli.capitalize()}")
        print(f"Harga Satuan   : Rp {harga_buah:,.0f}")
        print(f"Jumlah Buah    : {jumlah}")
        print(f"Total Harga    : Rp {total:,.0f}")
        print(f"Diskon         : {diskon}%")
        print(f"Potongan Harga : Rp {jumlah_diskon:,.0f}")
        print(f"Total Bayar    : Rp {total_diskon:,.0f}")
        print("=" * 40)
        print("Terima kasih telah berbelanja!")

        # Mengakhiri perulangan setelah transaksi selesai
        break

elif beli_buah == "tidak":
    print("Terima kasih!")
else:
    print("Pilihan tidak valid.")
