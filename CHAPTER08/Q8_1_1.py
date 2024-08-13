import os
def prepare_dir(a="seve_dir"):
    if os.path.exists(a):
        print("存在します")
    else:
        os.mkdir(a)
        print("作りました")

prepare_dir()

