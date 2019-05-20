import random

class Dice:
    def __init__(self,val=6):
        if val not in [4,6,8,12,20]:
            raise Exception("そんな正多面体はありません。")
        self.face_num = val

    def shoot(self):
        return random.randint(1,self.face_num)

#以下はdice_game.pyです。別ファイルに記載。
import dice

num = eval(input('4,6,8,12,20のどれで勝負しますか？：')) 
my_dice = dice.Dice(num)    
cpu_dice = dice.Dice(num)   

my_pip = my_dice.shoot()    # pipはサイコロの目の意味
cpu_pip = cpu_dice.shoot()  # コンピュータの出た目

# 出目を画面に出力 数字はstr関数を使って文字列に変更
print('CPU：' + str(cpu_pip) + ' あなた：' + str(my_pip))
# 状況によってメッセージを変える
if my_pip > cpu_pip:
    print('おめでとうございます。あなたの勝ちです！')
elif my_pip < cpu_pip:
    print('残念！あなたの負けです。')
else:
    print('引き分けです')
