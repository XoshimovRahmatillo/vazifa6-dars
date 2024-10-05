from datetime import datetime, timedelta

kun1 = input("1-kunni kiriting: ")
kun2 = input("2-kunni kiriting: ")

kun1 = datetime.strptime(kun1, "%Y-%m-%d")
kun2 = datetime.strptime(kun2, "%Y-%m-%d")



distance = abs(kun2 - kun1)

print(f"Kunlar farqi: {distance.days}")