Algoritma = float(input(" Masukan Nilai Algoritma Anda : "))
PerancanganObjek = float(input(" Masukan Nilai Objek Anda : "))
Kalkulus = float(input(" Masukan Nilai Kalkulus Anda : "))
Etika = float(input(" Masukan Nilai Etika Anda : "))
ProfesiDatabase = float(input(" Masukan Nilai Database Anda : "))
Inggris = float(input(" Masukan Nilai Inggris Anda : "))

def skortobobot (skor):
    if skor >= 100:
        return 4
    elif skor >= 89:
        return 3.75
    elif skor >= 84:
        return 3.50
    elif skor >= 79:
        return 3.25
    elif skor >= 74:
        return 3
    elif skor >= 69:
        return 2.75
    elif skor >= 64:
        return 2.5
    elif skor >= 59:
        return 2.25
    elif skor >= 54:
        return 2
    elif skor >= 49:
        return 1.75
    elif skor >= 44:
        return 1.5
    elif skor >= 39:
        return 1.25
    elif skor >= 34:
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
