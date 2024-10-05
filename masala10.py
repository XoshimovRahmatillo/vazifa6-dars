import random

a = int(input("Boshlang'ich sonni kiriting: "))
b = int(input("Oxirgi sonni kiriting: "))

tasodifiy_raqamlar = random.sample(range(a, b + 1), 5)

print("Tasodifiy butun sonlar:", tasodifiy_raqamlar)
