from datetime import datetime, timedelta

tg_kun = input("Tug'ilgan kuningizni kiriting: ")

tg = datetime.strptime(tg_kun, "%Y-%m-%d")

now = datetime.now()

keyingi_tg = tg.replace(year=now.year)
if keyingi_tg < now:
    keyingi_tg = keyingi_tg.replace(year=now.year + 1)

distance = keyingi_tg - now

print(f"Keyingi tug'ilgan kunigacha {distance.days} kun qolgan.")