import os
import shutil

papka_ochir = "test"

if os.path.exists(papka_ochir) and os.path.isdir(papka_ochir):
    shutil.rmtree(papka_ochir)
    print(f"{papka_ochir} papkasi muvaffaqiyatli o'chirildi.")
else:
    print(f"{papka_ochir} papkasi mavjud emas.")
