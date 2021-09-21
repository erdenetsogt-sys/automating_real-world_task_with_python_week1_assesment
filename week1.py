#!/usr/bin/env python3
import os
import subprocess
from PIL import Image

def path_of_images():
    #/images/というdir_pathを取得
    src = os.getcwd() + "/images/"
    #/images/ dirのファイルを表示
    list_of_files = os.listdir(src)
    #リストを格納する変数
    all_files = []

    for value in list_of_files:
        #.DS_Store以外の値を表示
        if value != ".DS_Store":
            #srcとimageの名前をくっ付ける
            full_path = os.path.join(src,value)
            all_files.append(full_path)
            image_data = Image.open(full_path)
            #出力先+名前
            export_dir = "/opt/icons/" + value
            image_data.rotate(90).resize((128,128)).convert("RGB").save(export_dir,'JPEG')


if __name__ == "__main__":
    path_of_images()