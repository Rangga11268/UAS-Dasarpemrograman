import datetime
import pandas as pd
from tabulate import tabulate

# Jarak tujuan wisata dalam kilometer
jarak_tujuan = {1: 100, 2: 10, 3: 50, 4: 200, 5: 300, 6: 600, 7: 1200}

# Harga sewa kendaraan per hari
harga_sewa = {
    1: {1: 900000, 2: 1100000},  # Mobil Elf
    2: {1: 1700000, 2: 2100000},  # Bus Medium
    3: {1: 3600000, 2: 4000000}   # Bus Besar
}

def tampilkan_menu(data, headers):
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

def input_with_validation(prompt, valid_options, error_message):
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_options:
                return choice
            else:
                print(error_message)
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

def masukkan_nama_penyewa():
    while True:
        nama = input("Masukkan nama penyewa: ")
        if nama.strip():
            return nama
        print("Nama tidak boleh kosong. Silakan coba lagi.")

def masukkan_tanggal():
    while True:
        tanggal_sewa = input("Masukkan tanggal sewa (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(tanggal_sewa, '%Y-%m-%d')
            return tanggal_sewa
        except ValueError:
            print("Format tanggal tidak valid. Silakan coba lagi.")

def masukkan_lama_sewa():
    return input_with_validation("Masukkan berapa hari sewa: ", range(1, 100), "Lama sewa harus lebih dari 0.")

def pilih_tempat_penjemputan():
    penjemputan_data = [
        ["1", "Jakarta"],
        ["2", "Bogor"],
        ["3", "Depok"],
        ["4", "Tangerang"],
        ["5", "Bekasi"]
    ]
    tampilkan_menu(penjemputan_data, ["No", "Tempat Penjemputan"])
    choice = input_with_validation("Pilih tempat penjemputan (1/2/3/4/5): ", range(1, 6), "Pilihan tidak valid.")
    detail_penjemputan = input("Masukkan detail penjemputan: ")
    return f"{['Jakarta', 'Bogor', 'Depok', 'Tangerang', 'Bekasi'][choice - 1]} - {detail_penjemputan}"

def pilih_tujuan_wisata():
    tujuan_data = [[str(i), t] for i, t in enumerate(["Banten", "DKI Jakarta", "Jawa Barat", "Jawa Tengah", "Jawa Timur", "DI Jogjakarta", "Bali"], start=1)]
    tampilkan_menu(tujuan_data, ["No", "Tujuan Wisata"])
    choice = input_with_validation("Pilih tujuan wisata (1-7): ", range(1, 8), "Pilihan tidak valid.")
    detail_tujuan = input("Masukkan detail tempat wisata: ")
    return choice, detail_tujuan

def metode_pembayaran():
    pembayaran_data = [["1", "Tunai"], ["2", "Kartu Kredit"], ["3", "Transfer Bank"]]
    tampilkan_menu(pembayaran_data, ["No", "Metode Pembayaran"])
    return input_with_validation("Pilih metode pembayaran (1-3): ", range(1, 4), "Pilihan tidak valid.")

def hitung_harga(kendaraan, seat, lama_sewa, tujuan):
    harga_kendaraan = harga_sewa[kendaraan][seat]
    harga_lama_sewa = lama_sewa * 50000
    harga_tujuan = jarak_tujuan[tujuan] * 1000
    return harga_kendaraan + harga_lama_sewa + (harga_tujuan * lama_sewa)

def input_pembayaran(total_harga):
    while True:
        try:
            nominal = int(input(f"Masukkan nominal pembayaran (Total: Rp{total_harga:,}): ").replace(',', ''))
            if nominal >= total_harga:
                return nominal, nominal - total_harga
            print("Nominal yang dimasukkan kurang dari total. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

def input_pin():
    while True:
        pin = input("Masukkan PIN (4 digit): ")
        if pin.isdigit() and len(pin) == 4:
            return pin
        print("PIN tidak valid. Harus 4 digit.")

def pilih_kendaraan():
    kendaraan_list = []
    while True:
        tampilkan_menu([
            ["1", "Mobil Elf (10 dan 19 seat)"],
            ["2", "Bus Medium (27 dan 35 seat)"],
            ["3", "Bus Besar (50 dan 59 seat)"]
        ], ["No", "Jenis Kendaraan"])

        kendaraan = input_with_validation("Pilih jenis kendaraan (1/2/3) atau 0 untuk selesai: ", range(0, 4), "Pilihan tidak valid.")
        if kendaraan == 0:
            break
        try:
            jumlah_unit = int(input("Masukkan jumlah unit yang ingin disewa: "))
            if jumlah_unit > 0:
                seat = tampilkan_tabel_seat(int(kendaraan))  # Tampilkan tabel hanya 1 kali
                for i in range(jumlah_unit):  # Iterasi sesuai jumlah unit
                    print(f"\nUnit {i + 1} dari {jumlah_unit}:")
                    pilihan = pilih_kursi_dari_tabel(seat)  # Ambil input pilihan
                    kendaraan_list.append((int(kendaraan), pilihan))
            else:
                print("Jumlah unit harus lebih dari 0. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")
    return kendaraan_list
def tampilkan_tabel_seat(kendaraan):
    seat_data = []
    if kendaraan == 1:
        seat_data = [["1", "Mobil Elf 10 seat"], ["2", "Mobil Elf 19 seat"]]
    elif kendaraan == 2:
        seat_data = [["1", "Bus Medium 27 seat"], ["2", "Bus Medium 35 seat"]]
    else:
        seat_data = [["1", "Bus Besar 50 seat"], ["2", "Bus Besar 59 seat"]]

    print(tabulate(seat_data, headers=["No", "Kapasitas Kursi"], tablefmt="fancy_grid"))
    return seat_data
def pilih_kursi_dari_tabel(seat_data):
    while True:
        try:
            pilihan = int(input("Pilih kapasitas kursi (1/2): "))
            if pilihan in [1, 2]:
                return pilihan
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

def main():
    print("╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱━━━╮")
    print("┃              SELAMAT DATANG DI PO CAKRAWALA TRANSPORT                    ┃")
    print("┃  🌟 Siapkan diri Anda untuk perjalanan yang  luar biasa bersama kami!🌟  ┃")
    print("┃              Pesan sekarang dan nikmati perjalanan Anda!                 ┃")
    print("╰━━━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱━━━╯")
    
    nama_penyewa = masukkan_nama_penyewa()
    kendaraan_list = pilih_kendaraan()  # Pilih kendaraan melalui fungsi yang telah dimodifikasi
    
    tanggal_sewa = masukkan_tanggal()
    lama_sewa = masukkan_lama_sewa()
    penjemputan = pilih_tempat_penjemputan()
    tujuan, detail_tujuan = pilih_tujuan_wisata()
    pembayaran = metode_pembayaran()

    total_harga_all = 0
    data = []

    for kendaraan, seat in kendaraan_list:
        total_harga = hitung_harga(kendaraan, seat, lama_sewa, tujuan)
        total_harga_all += total_harga
        data.append({
            "Tanggal Sewa": tanggal_sewa,
            "Jenis Kendaraan": ["Mobil Elf", "Bus Medium", "Bus Besar"][kendaraan - 1],
            "Kapasitas Kursi": ["10 seat", "19 seat", "27 seat", "35 seat", "50 seat", "59 seat"][seat + (kendaraan - 1) * 2 - 1],
            "Lama Sewa": f"{lama_sewa} hari",
            "Tempat Penjemputan": penjemputan,
            "Tujuan Wisata": ["Banten", "DKI Jakarta", "Jawa Barat", "Jawa Tengah", "Jawa Timur", "DI Jogjakarta", "Bali"][tujuan - 1],
            "Detail Tujuan": detail_tujuan,
            "Metode Pembayaran": ["Tunai", "Kartu Kredit", "Transfer Bank"][pembayaran - 1],
            "Total Harga": f"Rp{total_harga:,}"
        })

    df = pd.DataFrame(data)
    df.loc[len(df)] = {key: "" for key in df.columns[:-1]}
    df.at[len(df) - 1, "Total Harga"] = f"Rp{total_harga_all:,}"

    if pembayaran in [2, 3]:
        input_pin()

    total_bayar, kembalian = input_pembayaran(total_harga_all)

    print("\nNama Penyewa:")
    print(tabulate([[nama_penyewa]], headers=["Nama Penyewa"], tablefmt='fancy_grid', stralign='center'))
    print("\nRincian Penyewaan:")
    print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False, stralign='center', numalign='center'))

    total_data = [["Total Bayar", f"Rp{total_bayar:,}"], ["Kembalian", f"Rp{kembalian:,}"]]
    print("\nRincian Pembayaran:")
    print(tabulate(total_data, headers=["Deskripsi", "Jumlah"], tablefmt='fancy_grid', stralign='center'))

    print("╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━━╮")
    print("┃     TERIMA KASIH TELAH MEMILIH CAKRAWALA TRANSPORT!       ┃")
    print("┃    ✨Kami berharap Anda menikmati perjalanan Anda!✨      ┃")
    print("┃      ✨Sampai jumpa di perjalanan berikutnya!✨           ┃")
    print("╰━━━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱━━━╯")

if __name__ == "__main__":
    main()
