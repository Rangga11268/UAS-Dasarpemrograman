import datetime
from tabulate import tabulate
import pandas as pd

unit_shuttle = {
    1: {"kd_seat": 10, "nama": "Hiace Private Class 10 Seat", "tujuan": "Jakarta - Bandung", "harga": 150000},
    2: {"kd_seat": 19, "nama": "Hiace Reguler Class 19 Seat", "tujuan": "Bekasi - Bandung", "harga": 85000},
    3: {"kd_seat": 10, "nama": "Hiace Private Class 10 Seat", "tujuan": "Tangerang - Bandung", "harga": 100000},
    4: {"kd_seat": 19, "nama": "Hiace Reguler Class 19 Seat", "tujuan": "Bandung - Jakarta", "harga": 100000},
    5: {"kd_seat": 19, "nama": "Hiace Reguler Class 19 Seat", "tujuan": "Bandung - Bekasi", "harga": 85000},
    6: {"kd_seat": 19, "nama": "Hiace Reguler Class 19 Seat", "tujuan": "Bandung - Tangerang", "harga": 100000}
}

df_reservations = pd.DataFrame(columns=[
    "Nama Penyewa", "Tanggal Perjalanan", "Tujuan", "Jumlah Tiket", "Kursi yang Dipilih", "Total Harga", 
    "Kembalian", "Metode Pembayaran", "Nomor Tujuan"
])

def format_harga(harga):
    return f"Rp {harga:,.0f}".replace(',', '.').replace('.', '.', 1)

def tampilkan_unit_shuttle():
    print("Daftar Unit Shuttle Hiace:")
    menu_data = [[key, value["nama"], value["tujuan"], format_harga(value['harga'])] for key, value in unit_shuttle.items()]
    print(tabulate(menu_data, headers=["No", "Nama", "Tujuan", "Harga"], tablefmt="fancy_grid"))

def masukkan_nama():
    while True:
        nama = input("Masukkan nama: ")
        if nama.strip():  
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

def masukkan_jumlah_tiket(kd_seat):
    while True:
        try:
            jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
            if 0 < jumlah_tiket <= kd_seat:
                return jumlah_tiket
            else:
                print(f"Jumlah tiket harus antara 1 dan {kd_seat}. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

def tampilkan_kursi(kursi_dipilih, kursi_tersedia, kd_seat):
    kursi_tampilan = []
    for kursi in range(1, kd_seat + 1):
        if kursi in kursi_dipilih:
            kursi_tampilan.append(f"[\U0001F534] {kursi}")  # Selected seat (green circle)
        elif kursi not in kursi_tersedia:
            kursi_tampilan.append(f"[\U0001F535] {kursi}")  # Unavailable seat (red circle)
        else:
            kursi_tampilan.append(f"[\U0001F7E2] {kursi}")  # Available seat (yellow circle)

    kursi_data = [kursi_tampilan[i:i + 5] for i in range(0, len(kursi_tampilan), 5)]
    headers = [f"Kursi {i+1}" for i in range(5)]
    print(tabulate(kursi_data, headers=headers, tablefmt="fancy_grid"))

def pilih_kursi(jumlah_tiket , kd_seat, tanggal, tujuan):
    global df_reservations
    kursi_tersedia = list(range(1, kd_seat + 1))

    # Filter kursi berdasarkan tanggal dan tujuan
    if not df_reservations.empty:
        reserved_seats = df_reservations[
            (df_reservations['Tanggal Perjalanan'] == tanggal) & 
            (df_reservations['Tujuan'] == tujuan)
        ]
        if not reserved_seats.empty:
            reserved_seats = reserved_seats['Kursi yang Dipilih'].apply(lambda x: list(map(int, x.split(', '))) if x else []).sum()
            kursi_tersedia = [kursi for kursi in kursi_tersedia if kursi not in reserved_seats]

    # Check if there are available seats
    if len(kursi_tersedia) == 0:
        print("Semua kursi sudah terisi. Silakan pilih unit shuttle lain.")
        return None  # Indicate that no seats are available

    kursi_dipilih = []

    # Call the modified function to display seats
    tampilkan_kursi(kursi_dipilih, kursi_tersedia, kd_seat)
    
    for i in range(jumlah_tiket):
        while True:
            try:
                kursi = int(input(f"Pilih kursi untuk tiket {i + 1} (1-{kd_seat}): "))
                if kursi in kursi_tersedia:
                    kursi_dipilih.append(kursi)
                    kursi_tersedia.remove(kursi)
                    print(f"Kursi {kursi} berhasil dipilih.")
                    # Call the modified function to display seats
                    tampilkan_kursi(kursi_dipilih, kursi_tersedia, kd_seat)
                    break
                else:
                    print("Kursi tidak tersedia. Silakan pilih kursi lain.")
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka.")

    return tuple(kursi_dipilih)
def masukkan_pin():
    while True:
        pin = input("Masukkan PIN 4 digit: ")
        if len(pin) == 4 and pin.isdigit():
            return pin
        else:
            print("PIN harus terdiri dari 4 digit angka. Silakan coba lagi.")

def metode_pembayaran():
    pembayaran_data = [
        ["1", "E-wallet"],
        ["2", "Transfer Bank"],
    ]
    print("Pilih metode pembayaran:")
    print(tabulate(pembayaran_data, headers=["No", "Metode Pembayaran"], tablefmt="fancy_grid"))
    while True:
        try:
            pembayaran = int(input("Pilih metode pembayaran (1-2): "))
            if 1 <= pembayaran <= 2:
                if pembayaran == 1:
                    ewallet_data = [
                        ["1", "GoPay"],
                        ["2", "OVO"],
                        ["3", "DANA"]
                    ]
                    print("Pilih E-wallet yang ingin digunakan:")
                    print(tabulate(ewallet_data, headers=["No", "E-wallet"], tablefmt="fancy_grid"))
                    while True:
                        try:
                            ewallet_choice = int(input("Pilih E-wallet (1-3): "))
                            if 1 <= ewallet_choice <= 3:
                                ewallet_names = ["GoPay", "OVO", "DANA"]
                                print(f"Anda memilih pembayaran dengan {ewallet_names[ewallet_choice - 1]}.")
                                nomor_telepon = input("Masukkan nomor rekening/telepon tujuan: ")
                                masukkan_pin()
                                return "E-wallet", nomor_telepon
                            else:
                                print("Pilihan tidak valid. Silakan coba lagi.")
                        except ValueError:
                            print("Input tidak valid. Silakan masukkan angka.")
                elif pembayaran == 2:
                    bank_data = [
                        ["1", "BCA"],
                        ["2", "BRI"],
                        ["3", "BNI"]
                    ]
                    print("Pilih bank yang ingin digunakan:")
                    print(tabulate(bank_data, headers=["No", "Bank"], tablefmt="fancy_grid"))
                    while True:
                        try:
                            bank_choice = int(input("Pilih Bank (1-3): "))
                            if 1 <= bank_choice <= 3:
                                bank_names = ["BCA", "BRI", "BNI"]
                                print(f"Anda memilih pembayaran dengan {bank_names[bank_choice - 1]}.")
                                nomor_rekening = input("Masukkan nomor rekening tujuan: ")
                                masukkan_pin()
                                return "Transfer Bank", nomor_rekening
                            else:
                                print("Pilihan tidak valid. Silakan coba lagi.")
                        except ValueError:
                            print("Input tidak valid. Silakan masukkan angka.")
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

def input_pembayaran(total_harga):
    print(f"Total yang harus dibayar: {format_harga(total_harga)}")
    while True:
        try:
            nominal_input = input("Masukkan nominal pembayaran: ")
            nominal = int(nominal_input.replace('.', ''))
            if nominal >= total_harga:
                kembalian = nominal - total_harga
                print(f"Kembalian: {format_harga(kembalian)}")
                return nominal, kembalian
            else:
                print("Nominal pembayaran tidak cukup. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

def tampilkan_struk(nama, tanggal, jumlah_tiket, kursi, total_harga, kembalian, metode, nomor, tujuan):
    struk_data = [
        ["Nama Penyewa", nama],
        ["Tanggal Perjalanan", tanggal],
        ["Tujuan", tujuan],
        ["Jumlah Tiket", jumlah_tiket],
        ["Kursi yang Dipilih", ', '.join(map(str, kursi))],
        ["Total Harga", format_harga(total_harga)],
        ["Kembalian", format_harga(kembalian)],
        ["Metode Pembayaran", metode],
        ["Nomor Tujuan", nomor]
    ]
    print("\n--- STRUK PEMBELIAN TIKET ---")
    print(tabulate(struk_data, headers=["Deskripsi", "Detail"], tablefmt="fancy_grid", stralign="center"))
    print("------------------------------")

def simpan_data_ke_pandas(nama, tanggal, jumlah_tiket, kursi, total_harga, kembalian, metode, nomor, tujuan):
    global df_reservations
    data = {
        "Nama Penyewa": [nama],
        "Tanggal Perjalanan": [tanggal],
        "Tujuan": [tujuan],
        "Jumlah Tiket": [jumlah_tiket],
        "Kursi yang Dipilih": [', '.join(map(str, kursi))],
        "Total Harga": [total_harga],
        "Kembalian": [kembalian],
        "Metode Pembayaran": [metode],
        "Nomor Tujuan": [nomor]
    }
    df = pd.DataFrame(data)
    df_reservations = pd.concat([df_reservations, df], ignore_index=True)
    print("\n--- DATA TERSIMPAN DI PANDAS DATAFRAME ---")
    print(df_reservations)

def simpan_data_ke_file():
    """Simpan data DataFrame ke file CSV."""
    global df_reservations
    df_reservations.to_csv("reservasi_shuttle.csv", index=False)
    print("\n--- Data berhasil disimpan ke 'reservasi_shuttle.csv' ---")

def muat_data_dari_file():
    """Muat data dari file CSV ke DataFrame."""
    global df_reservations
    try:
        df_reservations = pd.read_csv("reservasi_shuttle.csv")
        print("\n--- Data berhasil dimuat dari 'reservasi_shuttle.csv' ---")
    except FileNotFoundError:
        print("\n--- File data belum ada. Memulai dengan data kosong. ---")
        df_reservations = pd.DataFrame(columns=[
            "Nama Penyewa", "Tanggal Perjalanan", "Tujuan", "Jumlah Tiket", "Kursi yang Dipilih",
            "Total Harga", "Kembalian", "Metode Pembayaran", "Nomor Tujuan"
        ])

def main():
    print("✨🛸 ~*~ 🌟 SELAMAT DATANG DI AGEN SHUTTLE CAKRAWALA TRANSPORT 🌟 ~*~ 🛸✨")
    print("        Pasang sabuk pengaman Anda untuk pengalaman yang tak terlupakan!        ")

    muat_data_dari_file()  # Memuat data yang sudah tersimpan

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
        kd_seat = unit_shuttle[pilihan_unit]["kd_seat"]
        
        # Hitung jumlah tiket yang sudah terpesan untuk tanggal dan tujuan yang sama
        reserved_seats = df_reservations[
            (df_reservations['Tanggal Perjalanan'] == tanggal_perjalanan) & 
            (df_reservations['Tujuan'] == unit_shuttle[pilihan_unit]["tujuan"])
        ]
        
        total_reserved = 0
        if not reserved_seats.empty:
            total_reserved = reserved_seats['Jumlah Tiket'].sum()
        
        sisa_tiket = kd_seat - total_reserved
        
        # Memastikan pengguna tidak bisa membeli lebih dari sisa tiket
        if sisa_tiket <= 0:
            print("Semua kursi sudah terisi. Silakan pilih unit shuttle lain.")
            continue
        
        print(f"Sisa tiket yang tersedia: {sisa_tiket}")
        jumlah_tiket = masukkan_jumlah_tiket(sisa_tiket)  # Pass sisa_tiket ke fungsi ini
        tujuan = unit_shuttle[pilihan_unit]["tujuan"]
        kursi_dipilih = pilih_kursi(jumlah_tiket, kd_seat, tanggal_perjalanan, tujuan)

        if kursi_dipilih is None:
            continue  # Skip to the next iteration if no seats are available

        total_harga = unit_shuttle[pilihan_unit]["harga"] * jumlah_tiket
        metode, nomor_tujuan = metode_pembayaran()
        nominal, kembalian = input_pembayaran(total_harga)

        tampilkan_struk(nama_penyewa, tanggal_perjalanan, jumlah_tiket, kursi_dipilih, total_harga, kembalian, metode, nomor_tujuan, tujuan)
        
        simpan_data_ke_pandas(nama_penyewa, tanggal_perjalanan, jumlah_tiket, kursi_dipilih, total_harga, kembalian, metode, nomor_tujuan, tujuan)

        # Simpan data setelah setiap transaksi
        simpan_data_ke_file()

        lagi = input("Apakah Anda ingin membeli tiket lagi? (ya/tidak): ")
        if lagi.lower() != 'ya':
            print("Terima kasih telah menggunakan layanan kami! 🌟 Selamat bepergian! 🌟")
            break

if __name__ == "__main__":
    main()
