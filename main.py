# 1. 
mevalar = {
    "banan": "3 ta",
    "olma": "4tA"
}

key = mevalar.keys()
print(key)

value = mevalar.values()
print(value)


# 2.
countries = {
    "Ozbekiston": "Toshkent",
    "Fransiya": "Parij",
    "Avstriya": "Vena" 
}

print(countries.items())


# 3.

shaharlar = {
    "Toshkent": "2 million",
    "Parij": "2,1 million"
}

shahar = input("Shahar nomini kiriting: ").capitalize()

shaharlar.pop(shahar)

print(shaharlar)


# 4.

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


# 5.

kinolar = {
    "Forrest Gump": 8.8, 
    "Yulduzli urushlar": 8.7 
}

kino = input("royxatdan ochirmoqchi bolgan kinoni nomini kiriting: ").capitalize()

while kino in kinolar:
    kinolar.pop(kino)

print(f"{kino} kinolar royxatidan ochirildi")
