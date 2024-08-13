import os
def delete_dir(a="seve_dir"):
    if os.path.exists(a):
        print("存在します")
        os.rmdir(a)
        print("削除しました")
    else:
        print("存在しません")

delete_dir()

