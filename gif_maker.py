# ライブラリのインポート
from PIL import Image
import os
# 画像を入れる箱を準備
pictures = []

# ファイルの保管されているフォルダー名
DIR = 'fig_8_check'
file_count = sum(os.path.isfile(os.path.join(DIR, name))
                for name in os.listdir(DIR))

# 画像を箱に入れていく pic_nameにて画像を保存しているフォルダーとファイル名を参照している. 200~270(最後の275はカウントされない).pngを参照して合成
for count in range(200,275,5):
    pic_name = 'fig_8_check/'+str(count) + '.png'
    img = Image.open(pic_name)
    pictures.append(img)
# gifアニメを出力する
pictures[0].save('anime.gif', save_all=True, append_images=pictures[1:],
                optimize=True, duration=240, loop=0)
