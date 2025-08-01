variabel_nama = "audry"
variabel_nim = 1124022
variabel_nilai = 92

nama = input("Masukkan nama mahasiswa: ")
nim = input("Masukkan NIM: ")
nilai = int(input("Masukkan nilai ujian (0-100): "))

if 85 <= nilai <= 100:
  kategori_nilai = "A (Sangat Baik)"
elif 75 <= nilai <= 84:
  kategori_nilai = "B (Baik)"
elif 60 <= nilai <= 74:
  kategori_nilai = "C (Cukup)"
elif 40 <= nilai <= 59:
  kategori_nilai = "D (Kurang)"
else:
  kategori_nilai = "E (Sangat Kurang)"


print(f"\nNama: {nama} (type: {type(nama)})")
print(f"NIM: {nim} (type: {type(nim)})")
print(f"Nilai: {nilai} (type: {type(nilai)})")

print("\nHasil Evaluasi:")
print(f"Mahasiswa: {nama} (NIM: {nim})")
print(f"Nilai Ujian: {nilai}")
print(f"Kategori Nilai: {kategori_nilai}")