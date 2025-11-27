"""""
program daftar nilai mahasiswa dengan fitur CRUD (Create, Read, Update, Delete)
"""
# Data mahasiswa disimpan dalam list of dictionaries
data_mahasiswa = []

def tambah():
    """Fungsi untuk menambah data mahasiswa baru"""
    print("\n--- Tambah Data Mahasiswa ---")
    nama = input("Masukkan nama mahasiswa: ").strip()
    
    # Cek apakah nama sudah ada
    if any(m['nama'].lower() == nama.lower() for m in data_mahasiswa):
        print(f" Data mahasiswa '{nama}' sudah ada!")
        return
    
    try:
        nim = input("Masukkan NIM: ").strip()
        nilai = float(input("Masukkan nilai: "))
        
        if nilai < 0 or nilai > 100:
            print(" Nilai harus berada antara 0-100!")
            return
        
        # Tentukan grade berdasarkan nilai
        if nilai >= 85:
            grade = 'A'
        elif nilai >= 75:
            grade = 'B'
        elif nilai >= 65:
            grade = 'C'
        elif nilai >= 55:
            grade = 'D'
        else:
            grade = 'E'
        
        data_mahasiswa.append({
            'nama': nama,
            'nim': nim,
            'nilai': nilai,
            'grade': grade
        })
        
        print(f" Data mahasiswa '{nama}' berhasil ditambahkan!")
        
    except ValueError:
        print(" Input tidak valid! NIM harus berupa angka dan nilai harus berupa angka desimal.")

def tampilkan():
    """Fungsi untuk menampilkan semua data mahasiswa"""
    print("\n--- Daftar Nilai Mahasiswa ---")
    
    if not data_mahasiswa:
        print("  Belum ada data mahasiswa.")
        return
    
    # Tampilkan header
    print(f"\n{'No':<4} {'Nama':<20} {'NIM':<12} {'Nilai':<8} {'Grade':<6}")
    print("-" * 50)
    
    # Tampilkan data
    for i, mhs in enumerate(data_mahasiswa, 1):
        print(f"{i:<4} {mhs['nama']:<20} {mhs['nim']:<12} {mhs['nilai']:<8.2f} {mhs['grade']:<6}")
    
    print(f"\nTotal mahasiswa: {len(data_mahasiswa)}")

def hapus(nama_input=None):
    """Fungsi untuk menghapus data mahasiswa berdasarkan nama"""
    print("\n--- Hapus Data Mahasiswa ---")
    
    if not data_mahasiswa:
        print("  Belum ada data untuk dihapus.")
        return
    
    # Jika nama tidak diberikan, minta input
    if nama_input is None:
        tampilkan()
        nama = input("\nMasukkan nama mahasiswa yang ingin dihapus: ").strip()
    else:
        nama = nama_input
    
    # Cari dan hapus data
    for i, mhs in enumerate(data_mahasiswa):
        if mhs['nama'].lower() == nama.lower():
            hapus_data = data_mahasiswa.pop(i)
            print(f" Data mahasiswa '{hapus_data['nama']}' berhasil dihapus!")
            return
    
    print(f" Mahasiswa dengan nama '{nama}' tidak ditemukan!")

def ubah(nama_input=None):
    """Fungsi untuk mengubah data mahasiswa berdasarkan nama"""
    print("\n--- Ubah Data Mahasiswa ---")
    
    if not data_mahasiswa:
        print("  Belum ada data untuk diubah.")
        return
    
    # Jika nama tidak diberikan, minta input
    if nama_input is None:
        tampilkan()
        nama = input("\nMasukkan nama mahasiswa yang ingin diubah: ").strip()
    else:
        nama = nama_input
    
    # Cari data
    for mhs in data_mahasiswa:
        if mhs['nama'].lower() == nama.lower():
            print(f"\nData saat ini: {mhs}")
            print("Pilih apa yang ingin diubah:")
            print("1. Nama")
            print("2. NIM")
            print("3. Nilai")
            print("4. Batal")
            
            pilihan = input("Masukkan pilihan (1-4): ").strip()
            
            if pilihan == '1':
                nama_baru = input("Masukkan nama baru: ").strip()
                mhs['nama'] = nama_baru
                print(f" Nama berhasil diubah menjadi '{nama_baru}'!")
                
            elif pilihan == '2':
                nim_baru = input("Masukkan NIM baru: ").strip()
                mhs['nim'] = nim_baru
                print(f" NIM berhasil diubah menjadi '{nim_baru}'!")
                
            elif pilihan == '3':
                try:
                    nilai_baru = float(input("Masukkan nilai baru: "))
                    if nilai_baru < 0 or nilai_baru > 100:
                        print(" Nilai harus berada antara 0-100!")
                        return
                    
                    mhs['nilai'] = nilai_baru
                    
                    # Update grade
                    if nilai_baru >= 85:
                        mhs['grade'] = 'A'
                    elif nilai_baru >= 75:
                        mhs['grade'] = 'B'
                    elif nilai_baru >= 65:
                        mhs['grade'] = 'C'
                    elif nilai_baru >= 55:
                        mhs['grade'] = 'D'
                    else:
                        mhs['grade'] = 'E'
                    
                    print(f" Nilai berhasil diubah menjadi {nilai_baru} (Grade: {mhs['grade']})!")
                    
                except ValueError:
                    print(" Input tidak valid!")
                    
            elif pilihan == '4':
                print(" Perubahan dibatalkan.")
            else:
                print(" Pilihan tidak valid!")
            
            return
    
    print(f" Mahasiswa dengan nama '{nama}' tidak ditemukan!")

def menu():
    """Fungsi untuk menampilkan menu utama"""
    while True:
        print("\n" + "="*50)
        print("   PROGRAM MANAJEMEN NILAI MAHASISWA")
        print("="*50)
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Keluar")
        print("-"*50)
        
        pilihan = input("Masukkan pilihan menu (1-5): ").strip()
        
        if pilihan == '1':
            tambah()
        elif pilihan == '2':
            tampilkan()
        elif pilihan == '3':
            ubah()
        elif pilihan == '4':
            hapus()
        elif pilihan == '5':
            print("\n Terima kasih telah menggunakan program ini. Sampai jumpa!")
            break
        else:
            print(" Pilihan tidak valid! Silakan coba lagi.")

if __name__ == "__main__":
    menu()
