import datetime
from tabulate import tabulate  # Import tabulate

# Daftar unit shuttle Hiace
unit_shuttle = {
    1: {"nama": "Hiace Private Class 10 Seat", "tujuan": "Jakarta - Bandung", "harga": 1100000},
    2: {"nama": "Hiace Reguler Class 19 Seat", "tujuan": "Bekasi - Bandung", "harga": 910000},
    3: {"nama": "Hiace Private Class 10 Seat", "tujuan": "Tangerang - Bandung", "harga": 1100000},
    4: {"nama": "Hiace Reguler Class 19 Seat", "tujuan": "Bandung - Jakarta", "harga": 910000},
    5: {"nama": "Hiace Reguler Class 19 Seat", "tujuan": "Bandung - Bekasi", "harga": 910000},
    6: {"nama": "Hiace Reguler Class 19 Seat", "tujuan": "Bandung - Tangerang", "harga": 910000}
}

def tampilkan_unit_shuttle():
    print("Daftar Unit Shuttle Hiace:")
    menu_data = [[key, value["nama"], value["tujuan"], f"Rp {value['harga']:,}"] for key, value in unit_shuttle.items()]
    print(tabulate(menu_data, headers=["No", "Nama", "Tujuan", "Harga"], tablefmt="fancy_grid"))

def masukkan_nama():
    while True:
        nama = input("Masukkan nama: ")
        if nama.strip():  # Check if name is not empty
            return nama
        else:
            print("Nama tidak boleh kosong. Silakan coba lagi.")

def masukkan_tanggal():
    while True:
        tanggal_sewa = input("Masukkan tanggal perjalanan (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(tanggal_sewa, '%Y-%m-%d')
            return tanggal_sewa
        except ValueError:
            print("Format tanggal tidak valid. Silakan coba lagi.")

def masukkan_jumlah_tiket():
    while True:
        try:
            jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
            if jumlah_tiket > 0:
                return jumlah_tiket
            else:
                print("Jumlah tiket harus lebih dari 0. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

def pilih_kursi(jumlah_tiket):
    kursi_tersedia = list(range(1, 11))  # Kursi 1 hingga 10 untuk Private Class
    kursi_dipilih = []

    while len(kursi_dipilih) < jumlah_tiket:
        # Tampilkan kursi yang tersedia dalam tabel
        print("DAFTAR PILIHAN KURSI:")
        
        # Buat tampilan kursi
        kursi_tampilan = []
        for kursi in range(1, 11):  # Hanya untuk kursi 1-10
            if kursi in kursi_dipilih:
                kursi_tampilan.append(f"[🔴] {kursi}")  # Kursi yang dipilih
            else:
                kursi_tampilan.append(f"[🟢] {kursi}")  # Kursi yang tersedia

        # Membagi kursi_tampilan menjadi baris
        kursi_data = [kursi_tampilan[i:i + 5] for i in range(0, len(kursi_tampilan), 5)]
        headers = ["Kursi 1", "Kursi 2", "Kursi 3", "Kursi 4", "Kursi 5"]  # Headers for each column
        print(tabulate(kursi_data, headers=headers, tablefmt="fancy_grid"))

        try:
            kursi = int(input(f"Pilih kursi untuk tiket {len(kursi_dipilih) + 1} (1-10): "))
            if kursi in kursi_tersedia:
                kursi_dipilih.append(kursi)  # Menyimpan kursi dalam list
                kursi_tersedia.remove(kursi)
            else:
                print("Kursi tidak tersedia. Silakan pilih kursi lain.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

    return tuple(kursi_dipilih)  # Mengembalikan kursi yang dipilih sebagai tuple


def masukkan_pin():
    while True:
        pin = input("Masukkan PIN 4 digit: ")
        if len(pin) == 4 and pin.isdigit():
            return pin
        else:
            print("PIN harus terdiri dari 4 digit angka. Silakan coba lagi.")

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
                if pembayaran == 1:
                    print("Anda memilih pembayaran Tunai.")
                elif pembayaran == 2:
                    print("Anda memilih pembayaran Kartu Kredit.")
                    masukkan_pin()
                else:
                    print("Anda memilih pembayaran Transfer Bank.")
                    masukkan_pin()
                return pembayaran
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")


def input_pembayaran(total_harga):
    print(f"Total yang harus dibayar: Rp{total_harga:,}")
    while True:
        try:
            nominal_input = input("Masukkan nominal pembayaran: ")
            nominal = int(nominal_input.replace('.', ''))
            if nominal >= total_harga:
                kembalian = nominal - total_harga
                print(f"Kembalian: Rp {kembalian:,}")
                return nominal, kembalian
            else:
                print("Nominal pembayaran tidak cukup. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

def tampilkan_struk(nama, tanggal, jumlah_tiket, kursi, total_harga, kembalian):
    struk_data = [
        ["Nama Penyewa", nama],
        ["Tanggal Perjalanan", tanggal],
        ["Jumlah Tiket", jumlah_tiket],
        ["Kursi yang Dipilih", ', '.join(map(str, kursi))],
        ["Total Harga", f"Rp {total_harga:,}"],
        ["Kembalian", f"Rp {kembalian:,}"]
    ]
    print("\n--- STRUK PEMBELIAN TIKET ---")
    print(tabulate(struk_data, headers=["Deskripsi", "Detail"], tablefmt="fancy_grid"))
    print("------------------------------")

def main():
    while True:
        tampilkan_unit_shuttle()
        while True:
            try:
                pilihan_unit = int(input("Pilih unit shuttle (1-6): "))
                if 1 <= pilihan_unit <= 6:
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka.")

        nama_penyewa = masukkan_nama()
        tanggal_perjalanan = masukkan_tanggal()
        jumlah_tiket = masukkan_jumlah_tiket()
        kursi_dipilih = pilih_kursi(jumlah_tiket)
        
        total_harga = unit_shuttle[pilihan_unit]["harga"] * jumlah_tiket
        metode = metode_pembayaran()
        nominal, kembalian = input_pembayaran(total_harga)

        tampilkan_struk(nama_penyewa, tanggal_perjalanan, jumlah_tiket, kursi_dipilih, total_harga, kembalian)

        # Menanyakan apakah pengguna ingin membeli tiket lagi
        lagi = input("Apakah Anda ingin membeli tiket lagi? (ya/tidak): ").strip().lower()
        if lagi != 'ya':
            print("Terima kasih telah menggunakan layanan kami!")
            break

if __name__ == "__main__":
    main()