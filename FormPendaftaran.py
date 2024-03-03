print(" Silahkan Isi Biodata Anda ")

Nama = str(input(" Masukan Nama Lengkap Anda : "))
TempatLahir = str(input(" Masukan Tempat lahir Anda : "))
TanggalLahir = float(input(" Masukan Tanggal Lahir Anda : "))
TahunLahir = float(input(" Msukan Tahun Lahir Anda : "))
TahunSaatIni  = 2024

print(" Silahkan Isi Nilai Dan Jenis Kelamin Anda")

NilaiEnglish = float(input(" Masukan Nilai English Anda : "))
NilaiMatematika = float(input(" Masukan Niai Matematika Anda : "))
NilaiBahasaIndonesia = float(input(" Masukan Nilai Bahasa Indonesia Anda : "))
JenisKelamin = str(input(" Masukan Jenis Kelamin L/P (Laki-Laki/Perempuan) : "))

umur = TahunSaatIni - TahunLahir
NilaiRataRata = (NilaiEnglish + NilaiMatematika + NilaiBahasaIndonesia) /3

if umur >= 25:
    print(" Anda Tidak Diterima Karena Umur Anda Melebihi Batas Umur Yang di Tentukan ")
elif NilaiRataRata >=80 and JenisKelamin == "L":
    print(" Anda Disarankan Untuk Masuk Jurusan Teknik Informatika ")
elif NilaiRataRata >=80 and JenisKelamin == "P":
    print(" Anda Disarankan Untuk Masuk Jurusan Sistem Informasi ")
else:
    print(" Selebihnya Anda Disarankan Untuk Masuk Jurusan DKV ")
