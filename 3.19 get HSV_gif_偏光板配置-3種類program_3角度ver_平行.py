# 座標系としては一枚目のセロハンの長手方向を基準とする

# モジュールのインポート
import numpy as np
import matplotlib.pyplot as plt
import time
import csv
from decimal import Decimal, ROUND_HALF_UP
import colorsys
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as patches
import math


# 計算における不動変数py -m pip install 

#Cello-x枚(1~4枚)
x = [1,2]
xx = 3
#Cello-p枚(1~2枚)
p = [1,2]
pp = 3
#Cello=z枚(0~4枚)
z = [1,2]
zz = 3

#偏光板配置(直交ニコル/平行ニコル配置/45°配置の3通り)
nn = 4
# 計算のステップ間隔
step = 5
# 三刺激値におけるK定数(初期化)
K = 0
# R"G"B"計算時に使用する，sRGB変換マトリクス．
tosRGB = [
        [3.2406, -1.5372, -0.4986],
        [-0.9689, 1.8758, 0.0415],
        [0.0557, -0.2040, 1.0570]
    ]


#_______________________________________________________________________________________________________________________________________________
## dataファイル(光路差100付近:基準)におけるファイルpass/2024.1.16^F 光路差の精密測定(Excel)より算出/**より精確なdata必要
file_name = "
hsv_gif_maker2026/data/data_d_100.csv"
# dataファイル(光源:白色LED光源)におけるファイルpass
file_name_lED = "
hsv_gif_maker2026/data/data_light.csv"
# dataファイル(光源:白色LED光源※もしかして昔はこっちかも!?)におけるファイルpass
file_name_lED2 = "
hsv_gif_maker2026/data/data_light2.csv"
# dataファイル(光源:スマートフォン-iphone_13_mini)におけるファイルpass
file_name_lED3 = "
hsv_gif_maker2026/data/data_light_iphone13mini.csv"
# dataファイル(光源:白色LED光源※surface-pro-7)におけるファイルpass
file_name_lED4 = "
hsv_gif_maker2026/data/data_light_surface.csv"
# dataファイル(補正データ:C2)におけるファイルpass
file_name_correct = "
hsv_gif_maker2026/data/data_correct.csv"
# dataファイル(等色関数 row[１]=x(λ),row[2]=y(λ),rao[3]=z(λ))におけるファイルpass
file_name_color_f = "
hsv_gif_maker2026/data/data_e_color.csv"
#________________________________________________________________________________________________________________________________________________

# 光路差(with open関数による，基準(100nm 付近)の光路差のinstal
with open(file_name, encoding='utf8') as f1:
    reader = csv.reader(f1)
    header = next(reader)

    λ = 380
    dd = []
    λλ = []
    for row in reader:
        λ = int(row[0])
        d = float(row[1])
        dd.append(d)
        λλ.append(λ)
        
        if int(row[0]) != λ:
            λ += 1
            # 繰り返し施行するための，配列のリセット
            if λ > 750:
                break 
              
dd.append(d)
λλ.append(λ)

#偏光状態の記述のために，installしたfiledataの型をlistからarrayへ変更
array_dd = np.array(dd)
array_λλ = np.array(λλ)

#＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿

# 光源(with open関数による，白色LED光源のdataのinstall)
with open(file_name_lED4, encoding='utf8') as f2:
    reader = csv.reader(f2)
    header = next(reader)

    λ = 380
    ll = []
    λλ = []
    for row in reader:
        λ = int(row[0])
        l = float(row[1])
        ll.append(l)
        
        if int(row[0]) != λ:
            λ += 1
            # 繰り返し施行するための，配列のリセット
            if λ > 750:
                break 
              
ll.append(l)

#偏光状態の記述のために，installしたfiledataの型をlistからarrayへ変更
array_ll = np.array(ll)

#_______________________________________________________________________________________________________________________________________________

# 光源(with open関数による，補正dataのinstall)
with open(file_name_correct, encoding='utf8') as f3:
    reader = csv.reader(f3)
    header = next(reader)

    λ = 380
    cc = []
    λλ = []
    for row in reader:
        λ = int(row[0])
        c = float(row[1])
        cc.append(c)
        
        if int(row[0]) != λ:
            λ += 1
            # 繰り返し施行するための，配列のリセット
            if λ > 750:
                break 
              
cc.append(c)

#偏光状態の記述のために，installしたfiledataの型をlistからarrayへ変更
array_cc = np.array(cc)

#_______________________________________________________________________________________________________________________________________________

# 光源(with open関数による，等色関数のinstall)
with open(file_name_color_f, encoding='utf8') as f4:
    reader = csv.reader(f4)
    header = next(reader)

    λ = 380
    cfx = []
    cfy = []
    cfz = []
    λλ = []
    for row in reader:
        λ = int(row[0])
        fx = float(row[1])
        fy = float(row[2])
        fz = float(row[3])
        cfx.append(fx)
        cfy.append(fy)
        cfz.append(fz)
        
        if int(row[0]) != λ:
            λ += 1
            # 繰り返し施行するための，配列のリセット
            if λ > 750:
                break 
              
cfx.append(fx)
cfy.append(fy)
cfz.append(fz)

#偏光状態の記述のために，installしたfiledataの型をlistからarrayへ変更
array_cfx = np.array(cfx)
array_cfy = np.array(cfy)
array_cfz = np.array(cfz)

#[k定数について]___________________________________________________________________________________________
for i in range(380,751): #各λにおける値の算出
        K += float((array_ll[i-380]*array_cfy[i-380]))
K = 1.0/ K # 光源の際の値を基準として,Y=1とする

#_______________________________________________________________________________________________________________________________________________

for count in range(390,395,5):
    #光路差(各変動-配列値)
    array_ddc = [num*(count/100) for num in np.array(dd)]
    #奥p枚における，光路差(固定値の方がよい..?※ この場合は，約269nmの光路差となっている．)
    #array_ddcp = [num*(2.69) for num in np.array(dd)]

    #それぞれの座標における初期化配列一覧
    #for pp in range(1,5):
        #for xx in range(1,5):
            # それぞれの座標におけるsum等色関数(x(λ),y(λ),z(λ))*E(λ)*Kを格納する配列

    #[直交ニコルver-zero配列一覧]___________________________________________________________________________________________
    arr_spcX= np.zeros(((nn),(zz),(pp),(xx),int(180/step)+1, int(180/step)+1,int(180/step)+1))
    arr_spcY = np.zeros(((nn),(zz),(pp),(xx),int(180/step)+1, int(180/step)+1,int(180/step)+1))
    arr_spcZ = np.zeros(((nn),(zz),(pp),(xx),int(180/step)+1, int(180/step)+1,int(180/step)+1))

    # それぞれの座標における混色比を格納する配列
    arr_spcXx = np.zeros(((nn),(zz),(pp),(xx),int(180/step)+1, int(180/step)+1,int(180/step)+1))
    arr_spcYy = np.zeros(((nn),(zz),(pp),(xx),int(180/step)+1, int(180/step)+1,int(180/step)+1))
    arr_spcZz = np.zeros(((nn),(zz),(pp),(xx),int(180/step)+1, int(180/step)+1,int(180/step)+1))

    # それぞれの座標におけるR"G"B"を格納する配列
    arr_RR = np.zeros(((nn),(zz),(pp),(xx),int(180/step)+1, int(180/step)+1,int(180/step)+1))
    arr_GG = np.zeros(((nn),(zz),(pp),(xx),int(180/step)+1, int(180/step)+1,int(180/step)+1))
    arr_BB = np.zeros(((nn),(zz),(pp),(xx),int(180/step)+1, int(180/step)+1,int(180/step)+1))

    # それぞれの座標におけるR'G'B'を格納する配列
    arr_R = np.zeros(((nn),(zz),(pp),(xx),int(180/step)+1, int(180/step)+1,int(180/step)+1))
    arr_G = np.zeros(((nn),(zz),(pp),(xx),int(180/step)+1, int(180/step)+1,int(180/step)+1))
    arr_B = np.zeros(((nn),(zz),(pp),(xx),int(180/step)+1, int(180/step)+1,int(180/step)+1))

    # それぞれの座標におけるRGBを格納する配列
    arr_Rr = np.zeros(((nn),(zz),(pp),(xx),int(180/step)+1, int(180/step)+1,int(180/step)+1))
    arr_Gr = np.zeros(((nn),(zz),(pp),(xx),int(180/step)+1, int(180/step)+1,int(180/step)+1))
    arr_Br = np.zeros(((nn),(zz),(pp),(xx),int(180/step)+1, int(180/step)+1,int(180/step)+1))

    # それぞれの座標におけるHSVを格納する配列
    arr_H = np.zeros(((nn),(zz),(pp),(xx),int(180/step)+1, int(180/step)+1,int(180/step)+1))
    arr_S = np.zeros(((nn),(zz),(pp),(xx),int(180/step)+1, int(180/step)+1,int(180/step)+1))
    arr_V = np.zeros(((nn),(zz),(pp),(xx),int(180/step)+1, int(180/step)+1,int(180/step)+1))

    # HSV色空間におけるxyz,3次元座標系
    arr_x = np.zeros(((nn),(zz),(pp),(xx),int(180/step)+1, int(180/step)+1,int(180/step)+1))
    arr_y = np.zeros(((nn),(zz),(pp),(xx),int(180/step)+1, int(180/step)+1,int(180/step)+1))
    arr_z = np.zeros(((nn),(zz),(pp),(xx),int(180/step)+1, int(180/step)+1,int(180/step)+1))

    #_____________________________________________________________________________________________________________________________________

    def r_theta(theta):  # 回転行列R(θ）
        return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

    def mai_r_theta(theta):  # 回転行列R(-θ）
        return np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])

    def jhons(theta):  # ジョーンズマトリクス
        return np.array([[np.sin(theta)**2, -np.sin(theta)*np.cos(theta)], [-np.sin(theta)*np.cos(theta), np.cos(theta)**2]])





    def main():  # メインの関数(各ニコル配置における全条件でのRGB値のfloat型-1次元配列算出機構)
        start_time = time.time()
        
        for nn in range(2,3): #平行ニコル配置の3通りの表現
            for zz in range(1,2):
                for pp in range(1,2):
                    for xx in range(1,2):
                        for ε in range(0,181,step):
                            for β in range(0, 181, step):##角度2つ目(β度)
                                for w in range(0, 181, step):##角度1つ目(w度)
                                    #XYZ(混色比)の総和を求めるための変数(float)
                                    spcX = 0.0
                                    spcY = 0.0
                                    spcZ = 0.0
                                    # 偏光板一枚目の回転角
                                    a = np.deg2rad(-w)
                                    E_1 = np.array([[-np.sin(a)], [np.cos(a)]])
                                    # セロハン二枚目の回転角
                                    b = np.deg2rad(β-w)
                                    # セロハン三枚目の回転角
                                    e = np.deg2rad(ε-w)
                                    # 偏光板二枚目の回転角
                                    if nn == 1: # 直交ニコル配置ver
                                        c = np.deg2rad(-w-90)
                                    elif nn ==2: # 平行ニコル配置ver
                                        c = np.deg2rad(-w)
                                    elif nn == 3: # 45°配置ver
                                        c = np.deg2rad(-w-45)

                                    for i in range(380,751): #各λにおける光路差d対応とジョーンズ・マトリクス計算
                                        # 波長
                                        l = i
                                        ## 位相差(手前x枚)
                                        delta = 2*array_ddc[l-380]*np.pi/l
                                        ## 位相差(中p枚)
                                        deltap = 2*array_ddc[l-380]*np.pi/l
                                        ## 位相差(奥z枚)
                                        deltaz = 2*array_ddc[l-380]*np.pi/l
                                        # セロハンの項(1jで虚数iを明示的に表現):x枚
                                        cellox = np.array([[1, 0], [0, np.exp(-1j*delta*xx)]])
                                        # セロハンの項(1jで虚数iを明示的に表現):p枚
                                        cellop = np.array([[1, 0], [0, np.exp(-1j*deltap*pp)]])
                                        # セロハンの項(1jで虚数iを明示的に表現):z枚
                                        celloz = np.array([[1, 0], [0, np.exp(-1j*deltaz*zz)]])
                                        # E_2への変換
                                        E_2 = np.dot(cellox, E_1)
                                        # E_3への変換（あやしいかも）
                                        E_3 = np.dot(r_theta(b), np.dot(
                                            cellop, np.dot(mai_r_theta(b), E_2)))
                                        #E_4への変換
                                        E_4 = np.dot(r_theta(e), np.dot(
                                            celloz, np.dot(mai_r_theta(e), E_3)))
                                        # E_5への変換
                                        E_5 = np.dot(jhons(c), E_4)
                                        # 各波長でのI(光強度)を算出する
                                        I = (np.abs(np.abs(E_5[0]**2) + np.abs(E_5[1]**2)))
                                        #2.強度配列に光源データ配列を積した測定直交スペクトルを算出　
                                        sp = I*(array_ll[l-380])
                                        #3.補正データを積した補正測定直交配置スペクトルを算出
                                        spc = sp*array_cc[l-380]
                                        #4について3種類の等色関数の積の総和をそれぞれ求める /K定数により三刺激値の算出(全座標について)
                                        spcX += float((spc*array_cfx[l-380])*K)
                                        spcY += float((spc*array_cfy[l-380])*K)
                                        spcZ += float((spc*array_cfz[l-380])*K)
                                    print("step:"+str(1),"nn:"+str(nn),"z枚:"+str(zz),"p枚:"+str(pp),"x枚:"+str(xx),"3角度目の角度:"+str(ε),"2角度目の角度:"+str(β), "1角度目の角度:"+str(w))
                                    arr_spcX[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)] = spcX #座標の配列(等色関数)について，積の総和を代入
                                    arr_spcY[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)] = spcY
                                    arr_spcZ[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)] = spcZ
            
        # 三刺激値XYZを全座標についてR"G"B"値へ変換
        for nn in range(2,3):#平行ニコル
            for zz in range(1,2):
                for pp in range(1,2):
                    for xx in range(1,2):
                        for ε in range(0,181,step):
                            for β in range(0, 181, step):##角度2つ目(β度)
                                for w in range(0, 181, step):##角度1つ目(w度)
                                    arr_spcXx[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)] = (arr_spcX[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)])
                                    arr_spcYy[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)] = (arr_spcY[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)])
                                    arr_spcZz[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)] = (arr_spcZ[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)])
                                    ##三刺激値の行列(3行1列)をE5として作成し，sRGB変換マトリクスとの積を[R"G"B"]配列として算出
                                    E_5 = np.array([[arr_spcXx[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)]], [arr_spcYy[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)]],
                                                    [arr_spcZz[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)]]])
                                    #
                                    arr_RGB = np.dot(tosRGB, E_5)
                                    arr_RR[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)]= arr_RGB[0]
                                    arr_GG[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)] = arr_RGB[1]
                                    arr_BB[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)] = arr_RGB[2]
                                    print("step:"+str(2),"nn:"+str(nn),"z枚:"+str(zz),"p枚:"+str(pp),"x枚:"+str(xx),"3角度目の角度:"+str(ε),"2角度目の角度:"+str(β), "1角度目の角度:"+str(w))
                                    #R'G'B'値について，R"G"B"配列から算出.
                                    
                                    for color in [arr_RR, arr_GG, arr_BB]:
                                        value = color[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)]
                                        if value <= 0.0031308:
                                            value *= 12.92 * 255
                                        else:
                                            value = (1.055 * (value ** (1 / 2.4)) - 0.055) * 255
                                        color[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)] = min(255, max(0, value))  
                                        # 0から255の範囲内に値を制限#R'G'B'値について，R"G"B"配列から算出.
        
    
        
        # RGB値をR'G'B'値から算出する．Decimalでstr型で四捨五入(整数)として，.to_integral_valueで数の型にしている
        for nn in range(2,3):
            for zz in range(1,2):
                for pp in range(1,2):
                    for xx in range(1,2):
                        for ε in range(0,181,step):##角度3つ目
                            for β in range(0, 181, step):##角度2つ目(β度)
                                for w in range(0, 181, step):##角度1つ目(w度)
                                    arr_Rr[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)]= (Decimal(str(arr_RR[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)])).quantize(Decimal('0'), rounding=ROUND_HALF_UP).to_integral_value())
                                    arr_Gr[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)]= (Decimal(str(arr_GG[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)])).quantize(Decimal('0'), rounding=ROUND_HALF_UP).to_integral_value())
                                    arr_Br[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)]= (Decimal(str(arr_BB[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)])).quantize(Decimal('0'), rounding=ROUND_HALF_UP).to_integral_value())
                                    print("step:"+str(3),"nn:"+str(nn),"z枚:"+str(zz),"p枚:"+str(pp),"x枚:"+str(xx),"3角度目の角度:"+str(ε),"2角度目の角度:"+str(β), "1角度目の角度:"+str(w))
                            
        # RGB値をHSV値に変換する．
        for nn in range(2,3):
            for zz in range(1,3):
                for pp in range(1,3):
                    for xx in range(1,3):
                        for ε in range(0,181,step):#角度3つ目
                            for β in range(0, 181, step):##角度2つ目(β度)
                                for w in range(0, 181, step):##角度1つ目(w度)
                                    HSV = colorsys.rgb_to_hsv((arr_Rr[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)])/255,(arr_Gr[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)])/255,
                                                            (arr_Br[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)])/255)
                                    arr_H[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)] = HSV[0]
                                    arr_S[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)] = HSV[1]
                                    arr_V[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)]= HSV[2]
                                    print("step:"+str(4),"nn:"+str(nn),"z枚:"+str(zz),"p枚:"+str(pp),"x枚:"+str(xx),"3角度目の角度:"+str(ε),"2角度目の角度:"+str(β), "1角度目の角度:"+str(w))
        
        # Figureを追加(figsizeで図の大きさを指定)
        fig = plt.figure(figsize=[24,12])

        # 3DAxesを追加
        ax1 = fig.add_subplot(2, 4, 1)
        ax2 = fig.add_subplot(2, 4, 2)
        ax3 = fig.add_subplot(2, 4, 3)
        ax4 = fig.add_subplot(2, 4, 4)
        ax5 = fig.add_subplot(2, 4, 5)
        ax6 = fig.add_subplot(2, 4, 6)
        ax7 = fig.add_subplot(2, 4, 7)
        ax8 = fig.add_subplot(2, 4, 8)

        # Axesのタイトルを設定
        ax1.grid(True)  # grid表示ON
        ax1.set_xlim(-1,1)
        ax1.set_ylim(-1,1)
        ax1.set_xlabel("x")
        ax1.set_ylabel("y")
        ax1.set_title("closed gate z1-p1-x1/R(retardation)"+str(count))  # グラフタイトル
        #グラフに円を描写する(ec = edge color)
        c = patches.Circle(xy=(0, 0), radius=1.0,fill=False, ec='r')
        # グラフに円を追加する．
        ax1.add_patch(c)
        
        ax2.grid(True)  # grid表示ON
        ax2.set_xlim(-1,1)
        ax2.set_ylim(-1,1)
        ax2.set_xlabel("x")
        ax2.set_ylabel("y")
        ax2.set_title("closed gate z1-p1-x2/R(retardation)"+str(count))  # グラフタイトル
        #グラフに円を描写する(ec = edge color)
        c = patches.Circle(xy=(0, 0), radius=1.0,fill=False, ec='r')
        # グラフに円を追加する．
        ax2.add_patch(c)
        
        ax3.grid(True)  # grid表示ON
        ax3.set_xlim(-1,1)
        ax3.set_ylim(-1,1)
        ax3.set_xlabel("x")
        ax3.set_ylabel("y")
        ax3.set_title("closed gate z1-p2-x1/R(retardation)"+str(count))  # グラフタイトル
        #グラフに円を描写する(ec = edge color)
        c = patches.Circle(xy=(0, 0), radius=1.0,fill=False, ec='r')
        # グラフに円を追加する．
        ax3.add_patch(c)
        
        ax4.grid(True)  # grid表示ON
        ax4.set_xlim(-1,1)
        ax4.set_ylim(-1,1)
        ax4.set_xlabel("x")
        ax4.set_ylabel("y")
        ax4.set_title("closed gate z1-p2-x2/R(retardation)"+str(count))  # グラフタイトル
        #グラフに円を描写する(ec = edge color)
        c = patches.Circle(xy=(0, 0), radius=1.0,fill=False, ec='r')
        # グラフに円を追加する．
        ax4.add_patch(c)
        
        ax5.grid(True)  # grid表示ON
        ax5.set_xlim(-1,1)
        ax5.set_ylim(-1,1)
        ax5.set_xlabel("x")
        ax5.set_ylabel("y")
        ax5.set_title("closed gate z2-p1-x1/R(retardation)"+str(count))  # グラフタイトル
        #グラフに円を描写する(ec = edge color)
        c = patches.Circle(xy=(0, 0), radius=1.0,fill=False, ec='r')
        # グラフに円を追加する．
        ax5.add_patch(c)
        
        ax6.grid(True)  # grid表示ON
        ax6.set_xlim(-1,1)
        ax6.set_ylim(-1,1)
        ax6.set_xlabel("x")
        ax6.set_ylabel("y")
        ax6.set_title("closed gate z2-p1-x2/R(retardation)"+str(count))  # グラフタイトル
        #グラフに円を描写する(ec = edge color)
        c = patches.Circle(xy=(0, 0), radius=1.0,fill=False, ec='r')
        # グラフに円を追加する．
        ax6.add_patch(c)

        ax7.grid(True)  # grid表示ON
        ax7.set_xlim(-1,1)
        ax7.set_ylim(-1,1)
        ax7.set_xlabel("x")
        ax7.set_ylabel("y")
        ax7.set_title("closed gate z2-p2-x1/R(retardation)"+str(count))  # グラフタイトル
        #グラフに円を描写する(ec = edge color)
        c = patches.Circle(xy=(0, 0), radius=1.0,fill=False, ec='r')
        # グラフに円を追加する．
        ax7.add_patch(c)
        
        ax8.grid(True)  # grid表示ON
        ax8.set_xlim(-1,1)
        ax8.set_ylim(-1,1)
        ax8.set_xlabel("x")
        ax8.set_ylabel("y")
        ax8.set_title("closed gate z2-p2-x2/R(retardation)"+str(count))  # グラフタイトル
        #グラフに円を描写する(ec = edge color)
        c = patches.Circle(xy=(0, 0), radius=1.0,fill=False, ec='r')
        # グラフに円を追加する．
        ax8.add_patch(c)
        
        # HSV値を極座標表示する
        
        #color ='c'
        #X = []
        #Y = []
        
        for nn in range(2,3):#(平行ニコルのみ抽出)
            for zz in range(1,2):
                for pp in range(1,2):
                    for xx in range(1,2):
                        X = []
                        Y = []
                        for ε in range(0,181,step):##角度3つ目(ε度)
                            for β in range(0, 181, step):##角度2つ目(β度)
                                for w in range(0, 181, step):##角度1つ目(w度)
                                    arr_x[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)] = (arr_S[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)])*np.cos(2*np.pi*(arr_H[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)]))
                                    arr_y[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)] = (arr_S[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)])*np.sin(2*np.pi*(arr_H[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)]))
                                    arr_z[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)] = arr_V[(nn)][(zz)][(pp)][(xx)][int(ε/step)][int(β/step)][int(w/step)]
                        X.append(arr_x)
                        Y.append(arr_y)
                        if xx == 1 and pp ==1 and zz==1 and nn==2:
                            color = "b"
                            ax1.scatter(X,Y,s=0.1,c=color)
                        elif xx == 2 and pp ==1 and zz==1 and nn ==2:
                            color = "r"
                            ax2.scatter(X,Y,s=0.1,c=color)
                        elif xx == 1 and pp ==2 and zz==1 and nn == 2:
                            color = "g"
                            ax3.scatter(X,Y,s=0.1,c=color)
                        elif xx == 2 and pp ==2 and zz == 1 and nn==2:
                            color = "y"
                            ax4.scatter(X,Y,s=0.1,c=color)
                        elif xx == 1 and pp ==1 and zz == 2 and nn==2:
                            color = "c"
                            ax5.scatter(X,Y,s=0.1,c=color)
                        elif xx == 2 and pp ==1 and zz == 2 and nn ==2:
                            color = "0.6"
                            ax6.scatter(X,Y,s=0.1,c=color)
                        elif xx == 1 and pp ==2 and zz == 2 and nn ==2:
                            color = "k"
                            ax7.scatter(X,Y,s=0.1,c=color)
                        elif xx == 2 and pp ==2 and zz == 2 and  nn==2:
                            color = "m"
                            ax8.scatter(X,Y,s=0.1,c=color)
                        
                       

        end_time = time.time()
        print("実行時間:"+str(end_time-start_time)+"秒")
        # グラフをfigファイルに保存する
        plt.savefig("fig_8_check/"+str(count)+".png")
            
    if __name__:
        main()     
