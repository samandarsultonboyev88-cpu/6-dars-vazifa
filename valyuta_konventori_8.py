import requests

url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
javob = requests.get(url)
kurslar = javob.json()

valyuta_kodi = input("Valyuta kodini kiriting (masalan: USD): ").upper()
miqdor = float(input("Miqdorni kiriting: "))

for item in kurslar:
    if item['Ccy'] == valyuta_kodi:
        kurs = float(item['Rate'])
        jami = miqdor * kurs
        print(f"Valyuta: {item['CcyNm_UZ']}")
        print(f"1 {valyuta_kodi} kursi: {kurs} so'm")
        print(f"Jami: {jami} so'm")
        break