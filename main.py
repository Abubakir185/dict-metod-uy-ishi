# 1. `keys()` va `values()` usullariga tayinlash: - Meva nomi-miqdori juftlari (masalan, "olma": 5, "banan": 3 va boshqalar) bilan
#  lug'at yarating. - `keys()` usulidan foydalanib, barcha meva nomlari ro`yxatini oling. - 
# `values()` usulidan foydalanib, mevalarning barcha miqdori ro`yxatini oling. - Qabul qilingan ro'yxatlarni ko'rsatish.

mevalar = {
    "banan": "3 ta",
    "olma": "4tA"
}

key = mevalar.keys()
print(key)

value = mevalar.values()
print(value)


# 2. `items()` usulini sozlash: - Davlat nomi-poytaxt juftliklari bilan lug‘at yaratish (masalan, “O‘zbekiston”: “Toshkent”, 
# “Fransiya”: “Parij” va boshqalar). - 
# `items()` usulidan foydalanib, "mamlakat nomi-poytaxti" juftliklari bilan kortejlar ro'yxatini oling. - Olingan ro'yxatni ko'rsatish.

countries = {
    "Ozbekiston": "Toshkent",
    "Fransiya": "Parij",
    "Avstriya": "Vena" 
}

print(countries.items())


# 3. `pop()` usulini sozlash: - Shahar-aholi juftliklari bilan lug‘at yaratish 
# (masalan, “Toshkent”: 2 million, “Parij”: 2,1 million va boshqalar). - Foydalanuvchidan o'chirmoqchi bo'lgan shahar nomini kiritishini so'rang. 
#  `pop()` usulidan foydalanib, ko'rsatilgan shaharni lug'atdan olib tashlang. - O'zgartirilgan lug'atni chiqarish.


shaharlar = {
    "Toshkent": "2 million",
    "Parij": "2,1 million"
}

shahar = input("Shahar nomini kiriting: ").capitalize()

shaharlar.pop(shahar)

print(shaharlar)


# 4. `For` siklida `keys()`, `values()` va `items()` usullarini o`rnatish: - Davlat nomi-aholi juftliklari bilan 
# lug‘at yarating (masalan, “Rossiya”: 144 million, “Fransiya”: 67 million va boshqalar). - “For” tsiklidan foydalanib, 
# lug‘atdagi har bir “mamlakat-aholi” juftligini takrorlang. - Davraning har bir iteratsiyasida mamlakat nomi, aholisi va barcha mamlakatlarning 
# umumiy aholisini ko'rsating. - Umumiy aholi sonini hisoblash uchun “qiymatlar()” va “sum()” usullaridan foydalaning.

countries = {
    "uzb": 37,
    "rus": 144,
    "usa": 370
}

total = 0

# for country in countries:
#     print(f"{country} -> {countries[country]}")
#     total += countries[country]
    
# print(total)

for country in countries.items():
    print(f"{country[0]} -> {country[1]}")
    total += country[1]

print(total)






# 5. `while` siklida `keys()` va `pop()` usullarini o`rnatish: - Film nomi-reyting juftliklari bilan lug'at yarating 
# (masalan, "Forrest Gump": 8,8, "Yulduzli urushlar": 8,7 va boshqalar). - Lug'at bo'sh bo'lgunga qadar "while" tsiklidan 
# foydalaning: - Kino nomlari roʻyxatini olish uchun “keys()” usulidan foydalaning. - Foydalanuvchidan o'chirmoqchi bo'lgan
#  film nomini kiritishini so'rang. 
# - `pop()` usulidan foydalanib, ko`rsatilgan filmni lug`atdan olib tashlang. - Lug'at bo'shligi haqidagi xabarni ko'rsatish."

kinolar = {
    "Forrest Gump": 8.8, 
    "Yulduzli urushlar": 8.7 
}

kino = input("royxatdan ochirmoqchi bolgan kinoni nomini kiriting: ").capitalize()

while kino in kinolar:
    kinolar.pop(kino)

print(f"{kino} kinolar royxatidan ochirildi")