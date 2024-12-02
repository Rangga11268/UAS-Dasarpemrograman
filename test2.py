import datetime
import pandas as pd
from tabulate import tabulate

# Harga sewa kendaraan per hari
harga_sewa = {
    1: {1: 900000, 2: 1100000},  # Mobil Elf
    2: {1: 1700000, 2: 2100000},  # Bus Medium
    3: {1: 3600000, 2: 4000000}   # Bus Besar
}

def tampilkan_menu():
    menu_data = [
        ["1", "Mobil Elf (10 dan 19 seat)"],
        ["2", "Bus Medium (27 dan 35 seat)"],
        ["3", "Bus Besar (50 dan 59 seat)"]
    ]
    print("Menu Penyewaan:")
    print(tabulate(menu_data, headers=["No", "Jenis Kendaraan"], tablefmt="fancy_grid"))

def pilih_kendaraan():
    kendaraan_list = []
    while True:
        tampilkan_menu()
        kendaraan = input("Pilih jenis kendaraan (1/2/3) atau 0 untuk selesai: ")
        if kendaraan in ['1', '2', '3']:
            try:
                jumlah_unit = int(input("Masukkan jumlah unit yang ingin disewa: "))
                if jumlah_unit > 0:
                    seat_data = tampilkan_tabel_seat(int(kendaraan))
                    for i in range(jumlah_unit):
                        print(f"\nUnit {i + 1} dari {jumlah_unit}:")
                        seat = pilih_kursi_dari_tabel(seat_data)
                        kendaraan_list.append((int(kendaraan), seat))
                else:
                    print("Jumlah unit harus lebih dari 0. Silakan coba lagi.")
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka.")
        elif kendaraan == '0':
            if not kendaraan_list:
                print("Anda belum memilih kendaraan. Silakan pilih kendaraan terlebih dahulu.")
            else:
                break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
    return kendaraan_list

def tampilkan_tabel_seat(kendaraan):
    seat_data = []
    if kendaraan == 1:
        seat_data = [["1", "Mobil Elf 10 seat"], ["2", "Mobil Elf 19 seat"]]
    elif kendaraan == 2:
        seat_data = [["1", "Bus Medium 27 seat"], ["2", "Bus Medium 35 seat"]]
    else:
        seat_data = [["1", "Bus Besar 50 seat"], ["2", "Bus Besar 59 seat"]]

    print("Pilih kapasitas kursi:")
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

def masukkan_nama_penyewa():
    while True:
        nama = input("Masukkan nama penyewa: ")
        if nama.strip():
            return nama
        else:
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
    while True:
        try:
            lama_sewa = int(input("Masukkan berapa hari sewa: "))
            if lama_sewa > 0:
                return lama_sewa
            else:
                print("Lama sewa harus lebih dari 0. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

def pilih_tempat_penjemputan():
    while True:
        detail_penjemputan = input("Masukkan tempat penjemputan (contoh: Jakarta - SMAN 1 Jakarta): ")
        if detail_penjemputan.strip():
            return detail_penjemputan
        else:
            print("Detail penjemputan tidak boleh kosong. Silakan coba lagi.")

def pilih_tujuan_wisata():
    while True:
        detail_tujuan = input("Masukkan tujuan wisata (contoh: Banten - Anyer): ")
        if detail_tujuan.strip():
            while True:
                try:
                    jarak = int(input("Masukkan jarak tujuan wisata dalam kilometer: "))
                    return detail_tujuan, jarak
                except ValueError:
                    print("Input tidak valid. Silakan masukkan angka untuk jarak.")
        else:
            print("Detail tujuan tidak boleh kosong. Silakan coba lagi.")

def metode_pembayaran():
    pembayaran_data = [
        ["1", "Tunai"],
        ["2", "Kartu Kredit"],
        ["3", "Transfer Bank"]
    ]
    print("Pilih metode pembayaran:")
    print(tabulate(pembayaran_data, headers=["No", "Metode Pembayaran"], tablefmt="fancy_grid"))

    while True:
        try:
            pembayaran = int(input("Pilih metode pembayaran (1/2/3): "))
            if 1 <= pembayaran <= 3:
                return pembayaran
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

def hitung_harga(kendaraan, seat, lama_sewa, jarak):
    harga_kendaraan = harga_sewa[kendaraan][seat]
    harga_lama_sewa = lama_sewa * 50000
    harga_tujuan = jarak * 1000
    return harga_kendaraan + harga_lama_sewa + (harga_tujuan * lama_sewa)

def input_pembayaran(total_harga):
    print(f"Total yang harus dibayar: Rp{total_harga:,}")
    while True:
        try:
            nominal_input = input("Masukkan nominal pembayaran: ")
            nominal = int(nominal_input.replace(',', ''))
            if nominal >= total_harga:
                kembalian = nominal - total_harga
                print(f"Kembalian: Rp{kembalian:,}")
                return nominal, kembalian
            else:
                print("Nominal yang dimasukkan kurang dari total. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

def input_pin():
    while True:
        pin = input("Masukkan PIN (4 digit): ")
        if pin.isdigit() and len(pin) == 4:
            return pin
        else:
            print("PIN tidak valid. Harus 4 digit.")

def main():
    print("╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱━━━╮")
    print("┃              SELAMAT DATANG DI PO CAKRAWALA TRANSPORT                   ┃")
    print("┃  🌟 Siapkan diri Anda untuk perjalanan yang luar biasa bersama kami! 🌟 ┃")
    print("┃              Pesan sekarang dan nikmati perjalanan Anda!                ┃")
    print("╰━━━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱━━━╯")

    # Meminta informasi penyewa
    nama_penyewa = masukkan_nama_penyewa()
    kendaraan_list = pilih_kendaraan()
    tanggal_sewa = masukkan_tanggal()
    lama_sewa = masukkan_lama_sewa()
    penjemputan = pilih_tempat_penjemputan()
    tujuan, jarak = pilih_tujuan_wisata()
    pembayaran = metode_pembayaran()

    total_harga_all = 0
    data = []

    # Menghitung total harga dan menyusun data
    for kendaraan, seat in kendaraan_list:
        total_harga = hitung_harga(kendaraan, seat, lama_sewa, jarak)
        total_harga_all += total_harga
        
        # Menambahkan rincian kendaraan
        data.append({
            "Tanggal Sewa": tanggal_sewa,
            "Jenis Kendaraan": ["Mobil Elf", "Bus Medium", "Bus Besar"][kendaraan - 1],
            "Kapasitas Kursi": ["10 seat", "19 seat", "27 seat", "35 seat", "50 seat", "59 seat"][seat + (kendaraan - 1) * 2 - 1],
            "Lama Sewa": f"{lama_sewa} hari",
            "Tempat Penjemputan": penjemputan,
            "Tujuan Wisata": tujuan,
            "Metode Pembayaran": ["Tunai", "Kartu Kredit", "Transfer Bank"][pembayaran - 1],
            "Total Harga": f"Rp{total_harga:,}"
        })

    # Mengonversi data menjadi DataFrame
    df = pd.DataFrame(data)

    # Menambahkan total keseluruhan ke DataFrame
    df.loc[len(df)] = {
        "Tanggal Sewa": "",
        "Jenis Kendaraan": "",
        "Kapasitas Kursi": "",
        "Lama Sewa": "",
        "Tempat Penjemputan": "",
        "Tujuan Wisata": "",
        "Metode Pembayaran": "",
        "Total Harga": f"Rp{total_harga_all:,}"
    }

    # Input pembayaran
    if pembayaran in [2, 3]:  # Kartu Kredit atau Transfer Bank
        input_pin()

    total_bayar, kembalian = input_pembayaran(total_harga_all)

    # Menampilkan nama penyewa
    print("\nNama Penyewa:")
    print(tabulate([[nama_penyewa]], headers=["Nama Penyewa"], tablefmt='fancy_grid', stralign='center'))
    
    # Menampilkan rincian penyewaan dalam format tabel menggunakan tabulate
    print("\nRincian Penyewaan:")
    print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False, stralign='center', numalign='center'))

    # Menampilkan total bayar dan kembalian dalam tabel terpisah
    total_data = [
        ["Total Bayar", f"Rp{total_bayar:,}"],
        ["Kembalian", f"Rp{kembalian:,}"]
    ]
    print("\nRincian Pembayaran:")
    print(tabulate(total_data, headers=["Deskripsi", "Jumlah"], tablefmt='fancy_grid', stralign='center'))

    print("╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━━╮")
    print("┃     TERIMA KASIH TELAH MEMILIH CAKRAWALA TRANSPORT!       ┃")
    print("┃    ✨Kami berharap Anda menikmati perjalanan Anda!✨      ┃")
    print("┃      ✨Sampai jumpa di perjalanan berikutnya!✨           ┃")
    print("╰━━━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━━╯")

if __name__ == "__main__":
    main()
