import os

papka = input("Papka nomini kiriting: ")


if os.path.exists(papka) and os.path.isdir(papka):
    txt_count = 0
    for root, dirs, files in os.walk(papka):
        for file_name in files:
            if file_name.endswith('.txt'):
                txt_count += 1

    print(f"{papka} papkasidagi .txt fayllar soni: {txt_count}")
else:
    print(f"{papka} papkasi mavjud emas yoki bu papka emas.")


# for i in os.listdir():
#     if '.txt'