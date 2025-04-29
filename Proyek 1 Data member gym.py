import csv 

FILE_NAME = "data_member.csv"

def hitung_bmi(berat, tinggi_cm):
    tinggi_m = tinggi_cm / 100
    bmi = berat / (tinggi_m ** 2)
    return round(bmi, 2)

def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesitas"

def load_data():
    data = []
    try:
        with open(FILE_NAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['Berat Badan'] = float(row['Berat Badan'])
                row['Tinggi Badan'] = float(row['Tinggi Badan'])
                row['Umur'] = int(row['Umur'])
                data.append(row)
    except FileNotFoundError:
        pass
    return data

def simpan_data(data):
    with open(FILE_NAME, mode='w', newline='') as file:
        fieldnames = ['Nama Lengkap', 'Berat Badan', 'Tinggi Badan', 'Jenis Kelamin', 'Umur']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for member in data:
            writer.writerow(member)

def tampilkan_data(data):
    if not data:
        print("Belum ada data member.")
        return
    for i, member in enumerate(data):
        bmi = hitung_bmi(member['Berat Badan'], member['Tinggi Badan'])
        kategori = kategori_bmi(bmi)
        print(f"{i+1}. {member['Nama Lengkap']} | {member['Jenis Kelamin']} | Umur: {member['Umur']} tahun")
        print(f"   Berat: {member['Berat Badan']} kg, Tinggi: {member['Tinggi Badan']} cm")
        print(f"   BMI: {bmi} ({kategori})")
        print("-" * 50)

def tambah_member(data):
    nama = input("Nama Lengkap: ")
    berat = float(input("Berat Badan (kg): "))
    tinggi = float(input("Tinggi Badan (cm): "))
    gender = input("Jenis Kelamin (L/P): ")
    umur = int(input("Umur: "))

    member = {
        'Nama Lengkap': nama,
        'Berat Badan': berat,
        'Tinggi Badan': tinggi,
        'Jenis Kelamin': gender.upper(),
        'Umur': umur
    }
    data.append(member)
    simpan_data(data)
    print("Data berhasil ditambahkan!")

def edit_member(data):
    tampilkan_data(data)
    try:
        idx = int(input("Pilih nomor data yang ingin diedit: ")) - 1
        if 0 <= idx < len(data):
            data[idx]['Nama Lengkap'] = input("Nama Lengkap: ")
            data[idx]['Berat Badan'] = float(input("Berat Badan (kg): "))
            data[idx]['Tinggi Badan'] = float(input("Tinggi Badan (cm): "))
            data[idx]['Jenis Kelamin'] = input("Jenis Kelamin (L/P): ").upper()
            data[idx]['Umur'] = int(input("Umur: "))
            simpan_data(data)
            print("Data berhasil diubah!")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input tidak valid.")

def hapus_member(data):
    tampilkan_data(data)
    try:
        idx = int(input("Pilih nomor data yang ingin dihapus: ")) - 1
        if 0 <= idx < len(data):
            del data[idx]
            simpan_data(data)
            print("Data berhasil dihapus!")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input tidak valid.")

def menu():
    data = load_data()
    while True:
        print("\n=== Aplikasi Data Member Gym Telyu ===")
        print("1. Lihat Data Member")
        print("2. Tambah Data Member")
        print("3. Edit Data Member")
        print("4. Hapus Data Member")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tampilkan_data(data)
        elif pilihan == "2":
            tambah_member(data)
        elif pilihan == "3":
            edit_member(data)
        elif pilihan == "4":
            hapus_member(data)
        elif pilihan == "5":
            print("Terima kasih. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu()
