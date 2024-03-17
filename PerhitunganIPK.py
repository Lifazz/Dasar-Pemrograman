Algoritma = float(input(" Masukan Nilai Algoritma Anda : "))
PerancanganObjek = float(input(" Masukan Nilai Objek Anda : "))
Kalkulus = float(input(" Masukan Nilai Kalkulus Anda : "))
Etika = float(input(" Masukan Nilai Etika Anda : "))
ProfesiDatabase = float(input(" Masukan Nilai Database Anda : "))
Inggris = float(input(" Masukan Nilai Inggris Anda : "))

def skortobobot (skor):
    if skor >= 90:
        return 4
    elif skor >= 85:
        return 3.75
    elif skor >= 80:
        return 3.50
    elif skor >= 75:
        return 3.25
    elif skor >= 70:
        return 3
    elif skor >= 65:
        return 2.75
    elif skor >= 60:
        return 2.5
    elif skor >= 55:
        return 2.25
    elif skor >= 50:
        return 2
    elif skor >= 45:
        return 1.75
    elif skor >= 40:
        return 1.5
    elif skor >= 35:
        return 1.25
    elif skor >= 30:
        return 1
    else:
        return 0
    
NilaiKredit = 3

TotalAlgoritma = NilaiKredit * skortobobot(Algoritma)
TotalObjek = NilaiKredit * skortobobot(PerancanganObjek)
TotalKalkulus = NilaiKredit * skortobobot(Kalkulus)
TotalEtika = NilaiKredit * skortobobot(Etika)
TotalDatabase = NilaiKredit * skortobobot(ProfesiDatabase)
TotalInggris = NilaiKredit * skortobobot(Inggris)

Total_Bobot = TotalAlgoritma + TotalObjek + TotalKalkulus + TotalDatabase + TotalEtika + TotalInggris

def countIps(Total_Skor, Total_Kredit):
    Total_ipk = Total_Skor / Total_Kredit
    return Total_ipk

print(" Nilai IPK anda adalah : ", countIps(Total_Bobot, 18))
