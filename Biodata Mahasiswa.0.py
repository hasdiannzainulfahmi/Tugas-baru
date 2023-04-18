# Membuat kamus berisi biodata mahasiswa dan nilai matakuliah
mahasiswa = {
    "Riski": {
        "nim": "SI1234567890",
        "alamat": "Praya",
        "prodi": "Sistem Informasi",
        "semester": 2,
        "ipk": 3.5,
        "nilai_matakuliah": {
            "Pemrograman Dasar": 90,
            "Kalkulus": 70,
            "Fisika Dasar": 75
        }
    },
    "Riko": {
        "nim": "SI0344578901",
        "alamat": "Praya",
        "prodi": "Sistem Informasi",
        "semester": 3,
        "ipk": 3.8,
        "nilai_matakuliah": {
            "Pemrograman Lanjut": 80,
            "Algoritma dan Struktur Data": 87,
            "Basis Data": 92
        }
    },
    "Wawan": {
        "nim": "SI5678901234",
        "alamat": "Ganti",
        "prodi": "Sistem Informasi",
        "semester": 4,
        "ipk": 3.6,
        "nilai_matakuliah": {
            "Rangkaian Listrik": 70,
            "Sistem Digital": 80,
            "Sistem Kendali": 90
        }
    },
    "Sambo": {
        "nim": "TI4321098765",
        "alamat": "praya",
        "prodi": "Teknik Informatika",
        "semester": 5,
        "ipk": 3.7,
        "nilai_matakuliah": {
            "Kimia Fisika": 88,
            "Rekayasa Proses Kimia": 85,
            "Termokimia": 92
        }
    },
    "Fadli": {
        "nim": "TI9012345678",
        "alamat": "Kopang",
        "prodi": "Teknik Informatika",
        "semester": 6,
        "ipk": 3.9,
        "nilai_matakuliah": {
            "Mekanika Tanah": 95,
            "Struktur Baja": 92,
            "Konstruksi Beton": 93
        }
    }
}

# Menampilkan biodata mahasiswa dan nilai akumulasi tiga matakuliah
for nama, data in mahasiswa.items():
    print("Biodata Mahasiswa")
    print("Nama          :", nama)
    print("NIM           :", data["nim"])
    print("Alamat        :", data["alamat"])
    print("Program Studi :", data["prodi"])
    print("Semester      :", data["semester"])
    print("IPK           :", data["ipk"])
    print("Nilai Akumulasi Matakuliah:")
    total_nilai = 0
    for matakuliah, nilai in data["nilai_matakuliah"].items():
        print("-", matakuliah, ":", nilai)
        total_nilai += nilai
    print("Total Nilai:", total_nilai)
    print("")
