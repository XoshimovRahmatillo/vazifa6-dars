import random
import string

parol_belgilari = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(parol_belgilari) for _ in range(8))

print("Tasodifiy parol:", password)