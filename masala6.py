import os
for papka , dir, file in os.walk("Dars"):
    print(papka,dir,file)