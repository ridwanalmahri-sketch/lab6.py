"Program Manajemen Nilai Mahasiswa"

📋 Daftar Isi
1. [Deskripsi Program](#deskripsi-program)
2. [Fitur](#fitur)
3. [Flowchart](#flowchart)
4. [Penjelasan Program](#penjelasan-program)
5. [Cara Penggunaan](#cara-penggunaan)
6. [Struktur Data](#struktur-data)



"Deskripsi Program"

Program ini adalah aplikasi manajemen nilai mahasiswa yang dibangun menggunakan Python. Program memungkinkan pengguna untuk menambah, menampilkan, mengubah, dan menghapus data nilai mahasiswa dengan antarmuka menu yang interaktif.


 ✨ Fitur

 1. **Tambah Data Mahasiswa**
   - Menambahkan data mahasiswa baru dengan input: Nama, NIM, dan Nilai
   - Sistem otomatis menghitung grade berdasarkan nilai
   - Validasi untuk mencegah data duplikat
   - Validasi nilai (0-100)

 2. **Tampilkan Data Mahasiswa**
   - Menampilkan semua data mahasiswa dalam format tabel
   - Menampilkan informasi: No, Nama, NIM, Nilai, Grade
   - Menampilkan total jumlah mahasiswa

 3. **Ubah Data Mahasiswa**
   - Mengubah data berdasarkan nama mahasiswa
   - Dapat mengubah: Nama, NIM, atau Nilai
   - Jika nilai diubah, grade otomatis diperbarui
   - Verifikasi sebelum perubahan dilakukan

4. **Hapus Data Mahasiswa**
   - Menghapus data berdasarkan nama mahasiswa
   - Konfirmasi nama sebelum dihapus
```

📊 Flowchart
┌──────────────────────────┐
│        START             │
└─────────────┬────────────┘
              ▼
   ┌───────────────────────┐
   │   Tampilkan Menu      │
   └───────────┬───────────┘
               ▼
   ┌───────────────────────┐
   │   Input Pilihan       │
   └──────┬─────┬─────┬────┘
          │     │     │
     ┌────┘     │     └───────┐
     ▼          ▼              ▼
 [1] Tambah   [2] Tampil     [3] Ubah
     ▼          ▼              ▼
 [Tambah Data] [Tampilkan]  [Ubah Data]
     │          │              │
     └──────┬───┘              │
            ▼                   ▼
         [Kembali ke Menu]   [Kembali ke Menu]

             ┌───────────────┐
             ▼               ▼
           [4] Hapus      [5] Keluar
             ▼               ▼
        [Hapus Data]       ┌──────────┐
             │             │   END    │
             └────────────►└──────────┘
```
 Detail Flowchart per Fungsi:

"Flowchart Tambah Data"
```
┌──────────────────────────┐
│      START TAMBAH        │
└─────────────┬────────────┘
              ▼
     [Input Nama]
              ▼
      Nama sudah ada?
       ┌───────┴────────┐
       │                │
      YES             NO
       │                ▼
    [ERROR]       [Input NIM]
       │                ▼
       └──► RETURN   [Input Nilai]
                       ▼
               Nilai valid?
                 ┌──┴───┐
                 │      │
                NO     YES
                 │      ▼
             [ERROR]  [Hitung Grade]
                 │      ▼
                 └──► RETURN
                      ▼
                [Simpan Data]
                      ▼
                 ┌─────────┐
                 │ RETURN  │
                 └─────────┘


 **Flowchart Ubah Data**

┌──────────────────────────┐
│       START UBAH         │
└─────────────┬────────────┘
              ▼
     [Tampilkan Data]
              ▼
       [Input Nama]
              ▼
      Nama ditemukan?
       ┌───────┴────────┐
       │                │
      NO              YES
       │                ▼
   [ERROR]       [Pilih Field]
       │        (1=Nama/2=NIM/3=Nilai/4=Batal)
       └──► RETURN   │
                     ▼
         Field yang dipilih?
            ┌──────┬──────┬──────┬───────────┐
            │      │      │       │
           1      2      3     4(Batal)
            ▼      ▼      ▼       ▼
        [Update] [Update] [Input Nilai Baru] 
                             ▼
                      Nilai valid?
                       ┌──┴───┐
                       │      │
                      NO     YES
                       │      ▼
                   [ERROR]  [Update]
                       │      ▼
                       └──► RETURN
                              ▼
                         ┌─────────┐
                         │ RETURN  │
                         └─────────┘
```

"Flowchart Hapus Data"
```
┌──────────────────────────┐
│      START HAPUS         │
└─────────────┬────────────┘
              ▼
     [Tampilkan Data]
              ▼
      [Input Nama]
              ▼
      Nama ditemukan?
       ┌───────┴────────┐
       │                │
      NO              YES
       │                ▼
    [ERROR]          [HAPUS]
       │                ▼
       └──► RETURN   ┌─────────┐
                     │ RETURN  │
                     └─────────┘

```

💡 Penjelasan Program

"Struktur Global"
Program menggunakan sebuah list global `data_mahasiswa` untuk menyimpan semua data mahasiswa dalam bentuk dictionary.

python
data_mahasiswa = [
    {
        'nama': 'Budi Santoso',
        'nim': '20210001',
        'nilai': 85.5,
        'grade': 'A'
    },
    ...
]


 "Fungsi Tambah ()"

"Tujuan": Menambahkan data mahasiswa baru

"Proses":
1. Menerima input nama, NIM, dan nilai dari pengguna
2. Validasi nama (cek duplikat dengan perbandingan case-insensitive)
3. Validasi nilai (harus antara 0-100)
4. Menghitung grade berdasarkan skala:
   - 85-100: Grade A
   - 75-84: Grade B
   - 65-74: Grade C
   - 55-64: Grade D
   - 0-54: Grade E
5. Menyimpan data ke dalam list `data_mahasiswa`
6. Menampilkan pesan sukses

"Fungsi Tampilkan ()"

"Tujuan": Menampilkan semua data mahasiswa dalam format tabel

"Proses":
1. Cek apakah ada data (list tidak kosong)
2. Menampilkan header tabel dengan format kolom: No, Nama, NIM, Nilai, Grade
3. Iterasi setiap data dan menampilkan dalam format tabel
4. Menampilkan total jumlah mahasiswa di akhir

 "Fungsi Ubah (nama_input=None)"

"Tujuan": Mengubah data mahasiswa yang ada

"Proses":
1. Menampilkan data yang ada
2. Menerima input nama mahasiswa yang ingin diubah
3. Mencari data dengan nama yang sesuai (case-insensitive)
4. Jika ditemukan, menampilkan submenu pilihan:
   - Ubah Nama
   - Ubah NIM
   - Ubah Nilai
5. Validasi input sesuai tipe data
6. Jika nilai diubah, grade otomatis dihitung ulang
7. Menyimpan perubahan ke dalam dictionary

"Fungsi Hapus (nama_input=None)"

Tujuan: Menghapus data mahasiswa berdasarkan nama

Proses:
1. Menampilkan data yang ada
2. Menerima input nama mahasiswa yang ingin dihapus
3. Mencari data dengan nama yang sesuai (case-insensitive)
4. Jika ditemukan, menghapus data dari list menggunakan `pop()`
5. Menampilkan pesan sukses penghapusan

 "Fungsi Menu ()"

"Tujuan**: Menampilkan menu interaktif dan mengatur alur program

"Proses":
1. Menampilkan menu utama dalam loop `while True`
2. Menerima input pilihan dari pengguna (1-5)
3. Memanggil fungsi sesuai pilihan:
   - 1 → `tambah()`
   - 2 → `tampilkan()`
   - 3 → `ubah()`
   - 4 → `hapus()`
   - 5 → Keluar dari program
4. Menampilkan pesan error jika pilihan tidak valid
5. Kembali ke menu setelah setiap operasi

---

 🚀 Cara Penggunaan

"Menjalankan Program"

```bash
python tugas_praktikum.py
```

"Contoh Penggunaan:"

 1. **Menambah Data**

Pilihan: 1
--- Tambah Data Mahasiswa ---
Masukkan nama mahasiswa: Budi Santoso
Masukkan NIM: 20210001
Masukkan nilai: 85
✅ Data mahasiswa 'Budi Santoso' berhasil ditambahkan!
```

2. "Menampilkan Data"
```
Pilihan: 2
--- Daftar Nilai Mahasiswa ---

No   Nama                 NIM          Nilai    Grade 
--------------------------------------------------
1    Budi Santoso         20210001     85.00    A     
2    Ani Wijaya          20210002     78.00    B     

Total mahasiswa: 2


" 3. "Mengubah Data"

Pilihan: 3
--- Ubah Data Mahasiswa ---
Masukkan nama mahasiswa yang ingin diubah: Budi Santoso
Data saat ini: {...}
1. Nama
2. NIM
3. Nilai
4. Batal

Pilihan: 3
Masukkan nilai baru: 90
✅ Nilai berhasil diubah menjadi 90.0 (Grade: A)!


 4. "Menghapus Data"

Pilihan: 4
--- Hapus Data Mahasiswa ---
Masukkan nama mahasiswa yang ingin dihapus: Ani Wijaya
✅ Data mahasiswa 'Ani Wijaya' berhasil dihapus!




 "Struktur Data"

 **Data Mahasiswa**

python
{
    'nama': str,      # Nama lengkap mahasiswa
    'nim': str,       # Nomor Induk Mahasiswa
    'nilai': float,   # Nilai (0-100)
    'grade': str      # Grade (A, B, C, D, E)
}


"List Data Mahasiswa"

python
data_mahasiswa = [
    {'nama': 'Budi Santoso', 'nim': '20210001', 'nilai': 85.0, 'grade': 'A'},
    {'nama': 'Ani Wijaya', 'nim': '20210002', 'nilai': 78.5, 'grade': 'B'},
    {'nama': 'Citra Dewi', 'nim': '20210003', 'nilai': 92.0, 'grade': 'A'},
]




 "Validasi Data"

Program memiliki validasi berikut:

1. **Validasi Nama**: Mencegah duplikasi nama (case-insensitive)
2. **Validasi Nilai**: Nilai harus antara 0-100
3. **Validasi Input**: Menangani error jika input tidak sesuai tipe data
4. **Validasi Pencarian**: Memberikan pesan jika data tidak ditemukan

---

 📝 Catatan Penting

- Data hanya tersimpan selama program berjalan (dalam memory)
- Untuk persistent storage, dapat diintegrasikan dengan database atau file
- Program menggunakan perbandingan case-insensitive untuk nama (Budi = budi)
- Grade dihitung otomatis berdasarkan nilai

---

 "Konsep Python yang Digunakan"

- List & Dictionary**: Struktur data untuk menyimpan data
- Function**: Modularisasi kode
- Loop**: Untuk iterasi data dan menu
- Conditional (if-elif-else)**: Untuk logika validasi dan branching
- String Methods**: `.strip()`, `.lower()` untuk validasi input
- List Methods**: `.append()`, `.pop()` untuk manipulasi data
- Exception Handling**: `try-except` untuk error handling
