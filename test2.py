import datetime
import pandas as pd
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

# Jarak tujuan wisata dalam kilometer
jarak_tujuan = {
    1: 100,  # Banten
    2: 10,   # DKI Jakarta
    3: 50,   # Jawa Barat
    4: 200,  # Jawa Tengah
    5: 300,  # Jawa Timur
    6: 600   # DI Jogjakarta
}

console = Console()

def tampilkan_menu():
    menu_data = [
        [1, "Mobil Elf (10 dan 19 seat)"],
        [2, "Bus Medium (27 dan 35 seat)"],
        [3, "Bus Besar (50 dan 59 seat)"]
    ]
    table = Table(title="🌟 Selamat datang di PO Bus 🌟", title_justify="center")
    table.add_column("No", justify="center")
    table.add_column("Menu Penyewaan", justify="center")
    
    for row in menu_data:
        table.add_row(str(row[0]), row[1])
    
    console.print(table)

def pilih_kendaraan():
    kendaraan_list = []
    while True:
        kendaraan = Prompt.ask("Pilih jenis kendaraan (1/2/3) atau 0 untuk selesai")
        if kendaraan in ['1', '2', '3']:
            jumlah_unit = int(Prompt.ask("Masukkan jumlah unit yang ingin disewa", default="1"))
            if jumlah_unit > 0:
                kendaraan_list.extend((int(kendaraan), pilih_seat(int(kendaraan))) for _ in range(jumlah_unit))
            else:
                console.print("[red]Jumlah unit harus lebih dari 0. Silakan coba lagi.[/red]")
        elif kendaraan == '0':
            break
        else:
            console.print("[red]Pilihan tidak valid. Silakan coba lagi.[/red]")
    return kendaraan_list

def pilih_seat(kendaraan):
    seat_data = {
        1: ["Mobil Elf 10 seat", "Mobil Elf 19 seat"],
        2: ["Bus Medium 27 seat", "Bus Medium 35 seat"],
        3: ["Bus Besar 50 seat", "Bus Besar 59 seat"]
    }
    
    table = Table(title="Pilih kapasitas kursi")
    table.add_column("No", justify="center")
    table.add_column("Kapasitas Kursi", justify="center")
    
    for idx, seat in enumerate(seat_data[kendaraan], start=1):
        table.add_row(str(idx), seat)

    console.print(table)

    while True:
        seat = int(Prompt.ask("Pilih kapasitas kursi (1/2)"))
        if seat in [1, 2]:
            return seat
        else:
            console.print("[red]Pilihan tidak valid. Silakan coba lagi.[/red]")

def masukkan_tanggal():
    while True:
        tanggal_sewa = Prompt.ask("Masukkan tanggal sewa (YYYY-MM-DD)")
        try:
            datetime.datetime.strptime(tanggal_sewa, '%Y-%m-%d')
            return tanggal_sewa
        except ValueError:
            console.print("[red]Format tanggal tidak valid. Silakan coba lagi.[/red]")

def masukkan_lama_sewa():
    while True:
        lama_sewa = int(Prompt.ask("Masukkan berapa hari sewa"))
        if lama_sewa > 0:
            return lama_sewa
        else:
            console.print("[red]Lama sewa harus lebih dari 0. Silakan coba lagi.[/red]")

def pilih_tempat_penjemputan():
    penjemputan_data = ["Jakarta", "Bogor", "Depok", "Tangerang", "Bekasi"]
    table = Table(title="Pilih tempat penjemputan")
    table.add_column("No", justify="center")
    table.add_column("Tempat Penjemputan", justify="center")

    for idx, tempat in enumerate(penjemputan_data, start=1):
        table.add_row (str(idx), tempat)

    console.print(table)

    while True:
        penjemputan = int(Prompt.ask("Pilih tempat penjemputan (1/2/3/4/5)"))
        if 1 <= penjemputan <= len(penjemputan_data):
            detail_penjemputan = Prompt.ask("Masukkan detail penjemputan")
            return penjemputan, detail_penjemputan
        else:
            console.print("[red]Pilihan tidak valid. Silakan coba lagi.[/red]")

def pilih_tujuan_wisata():
    tujuan_data = ["Banten", "DKI Jakarta", "Jawa Barat", "Jawa Tengah", "Jawa Timur", "DI Jogjakarta"]
    table = Table(title="Pilih tujuan wisata")
    table.add_column("No", justify="center")
    table.add_column("Tujuan Wisata", justify="center")
    table.add_column("Jarak (km)", justify="center")

    for idx, tujuan in enumerate(tujuan_data, start=1):
        table.add_row(str(idx), tujuan, str(jarak_tujuan[idx]))

    console.print(table)

    while True:
        tujuan = int(Prompt.ask("Pilih tujuan wisata (1/2/3/4/5/6)"))
        if 1 <= tujuan <= len(tujuan_data):
            detail_tujuan = Prompt.ask("Masukkan detail tempat wisata")
            return tujuan, detail_tujuan
        else:
            console.print("[red]Pilihan tidak valid. Silakan coba lagi.[/red]")

def metode_pembayaran():
    pembayaran_data = ["Tunai", "Kartu Kredit", "Transfer Bank"]
    table = Table(title="Pilih metode pembayaran")
    table.add_column("No", justify="center")
    table.add_column("Metode Pembayaran", justify="center")

    for idx, metode in enumerate(pembayaran_data, start=1):
        table.add_row(str(idx), metode)

    console.print(table)

    while True:
        pembayaran = int(Prompt.ask("Pilih metode pembayaran (1/2/3)"))
        if 1 <= pembayaran <= len(pembayaran_data):
            return pembayaran
        else:
            console.print("[red]Pilihan tidak valid. Silakan coba lagi.[/red]")

def hitung_harga(kendaraan, seat, lama_sewa, tujuan):
    harga_kendaraan = [1000000, 2000000, 3000000][kendaraan - 1] + (500000 if seat == 2 else 0)
    harga_lama_sewa = lama_sewa * 50000
    harga_tujuan = jarak_tujuan[tujuan] * 1000
    return harga_kendaraan + harga_lama_sewa + harga_tujuan

def main():
    tampilkan_menu()
    kendaraan_list = pilih_kendaraan()
    tanggal_sewa = masukkan_tanggal()
    lama_sewa = masukkan_lama_sewa()
    penjemputan, detail_penjemputan = pilih_tempat_penjemputan()
    tujuan, detail_tujuan = pilih_tujuan_wisata()
    pembayaran = metode_pembayaran()

    data = []
    total_harga_all = 0  # Variabel untuk menyimpan total keseluruhan

    for kendaraan, seat in kendaraan_list:
        total_harga = hitung_harga(kendaraan, seat, lama_sewa, tujuan)
        total_harga_all += total_harga  # Menambahkan total harga ke total keseluruhan
        data.append({
            "Tanggal Sewa": tanggal_sewa,
            "Jenis Kendaraan": ["Mobil Elf", "Bus Medium", "Bus Besar"][kendaraan - 1],
            "Kapasitas Kursi": ["10 seat", "19 seat", "27 seat", "35 seat", "50 seat", "59 seat"][seat - 1],
            "Lama Sewa": lama_sewa,
            "Tempat Penjemputan": ["Jakarta", "Bogor", "Depok", "Tangerang", "Bekasi"][penjemputan - 1],
            "Detail Penjemputan": detail_penjemputan,
            "Tujuan Wisata": ["Banten", "DKI Jakarta", "Jawa Barat", "Jawa Tengah", "Jawa Timur", "DI Jogjakarta"][tujuan - 1],
            "Detail Tujuan": detail_tujuan,
            "Metode Pembayaran": ["Tunai", "Kartu Kredit", "Transfer Bank"][pembayaran - 1],
            "Total Harga": total_harga
        })

    df = pd.DataFrame(data)
    table = Table(title="Rincian Penyewaan", title_justify="center")
    for column in df.columns:
        table.add_column(column, justify="center")

    for index, row in df.iterrows():
        table.add_row(*[str(value) for value in row])

    console.print(table)
    console.print(f"\n[bold]Total Keseluruhan: {total_harga_all}[/bold]")  # Menampilkan total keseluruhan
    console.print("\n🎉 Terima kasih telah menggunakan layanan kami! Kami berharap Anda menikmati perjalanan Anda! 🚍✨")

if __name__ == "__main__":
    main()