def hitung_nilai_akhir(tugas, uts, uas):
    nilai_akhir = 0.25 * tugas + 0.35 * uts + 0.40 * uas
    return nilai_akhir

def tentukan_huruf_nilai(nilai_akhir):
    if nilai_akhir > 85:
        return "A"
    elif nilai_akhir > 80:
        return "A-"
    elif nilai_akhir > 75:
        return "B+"
    elif nilai_akhir > 70:
        return "B"
    elif nilai_akhir > 65:
        return "B-"
    elif nilai_akhir > 60:
        return "C+"
    elif nilai_akhir > 55:
        return "C"
    elif nilai_akhir > 50:
        return "C-"
    elif nilai_akhir > 30:
        return "D"
    else:
        return "E"

print("Selamat datang di aplikasi perhitungan nilai mahasiswa")
tugas = float(input("Silahkan masukan nilai tugas : "))
uts = float(input("Silahkan masukan nilai uts : "))
uas = float(input("Silahkan masukan nilai uas : "))

nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
print("Nilai Akhir :", nilai_akhir)
print("Mendapatkan Grade :", tentukan_huruf_nilai(nilai_akhir))