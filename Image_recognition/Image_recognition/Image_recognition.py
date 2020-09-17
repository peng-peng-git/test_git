import pyautogui
from PIL import Image,ImageOps,ImageFilter
import os
import datetime
import tkinter
from tkinter import messagebox

#検索画像、スクリーンショットを保存するディレクトリをを指定する
img_dir = os.path.abspath("search_img")
log_dir = os.path.abspath("logs")
ss_dir = os.path.abspath("tmp_img")
#スクリーンショット、ログファイル名の名前を指定する。
tmpfile = datetime.datetime.now()
filename = tmpfile.strftime('%Y%m%d_%H%M%S')

#画像をスクリーンショットに収める save_img
def save_img():
    #screenshotの引数は→　region=(cBasePoint[0], cBasePoint[1], 410, 125)
    img = auto.screenshot()
    img.save(ss_dir + "\\" + filename + ".png")
    print(ss_dir + "\\" + filename + ".png を保存したで。")

#認識対象ファイルとファイルパスを辞書化する。
def search_img():
    target_dict = dict()
    #os.listdir(path=img_dir + "//")は配列でできている。
    #ハッシュの宣言、個数はimg_dirディレクトリ内のファイルの個数
    #dict文を作る際、keyを新規で追加する場合は、setdefault(keys,value)メソッド
    #を入れること。
    for i in os.listdir(path=img_dir):
        target_dict.setdefault(os.path.splitext(i)[0],img_dir + i)
        print("search_imgフォルダ内にある画像ファイルをファイル名をキーにして辞書化したったで。（どやぁ")

#認識対象ファイルを検索して、画像の中央をクリック
def click():
    x, y = pyautogui.locateCenterOnScreen(target_dict.values[i])
    pyautogui.Click(x, y)
    print(target_dict.keys[i] + "ダブルクリックしたったで！")

#Tkウィンドウを表示するとき、別窓で小さなウィンドウが表示される
#これはそのウィンドウを非表示にする
root = tkinter.Tk()
root.withdraw()
#while  (messagebox.askyesno('タイトル', 'メッセージ内容') == True):
#    messagebox.showinfo('中断','自動操作処理を終了します。')
#    break
#else:
#    messagebox.askyesno('処理中', '自動操作中です。処理を終了するには「はい」を押してください。')

search_img()
