import parol_generatori_1

uzunlik = int(input("Parol uzunligini kiriting: "))
yaratilgan_parol = parol_generatori_1.parol_yarat(uzunlik)

print(f"Yaratilgan parol: {yaratilgan_parol}")
print("Tekshiruv:", parol_generatori_1.parol_tekshir(yaratilgan_parol))