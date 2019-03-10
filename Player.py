import random

class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.max_hp = hp
    
    def attack(self):
        """
        攻撃の処理。今はprintだけだが後々ここに追加することになりそう
        """
        print("プレイヤー{}の攻撃！".format(self.name))
    
    def receive_damage(self, damage):
        """
        ダメージ計算処理
        """
        self.hp -= damage
        print("プレイヤー{}は{}ダメージを受けた！".format(self.name, damage))

"""
バトルシーンの流れチェック（現在は使っていない）
"""

"""
players = [Player("A", 1000), Player("B", 1000)]
atk_turn = 0
total_turns = 1

while True:
    print("{}ターン目".format(total_turns))
    print("認識の選択")
    isRecognized = random.choice([False, True]) # 正しく認識できたかどうか（一旦ランダムで選択させる）
    print("isRecognized: {}".format(isRecognized))

    # 正しく認識できたらダメージ、できなかったらノーダメージ
    print("ダメージ計算")
    players[atk_turn].attack() # 攻撃の表示
    if isRecognized:
        if atk_turn == 0:
            players[1].receive_damage(400)
        elif atk_turn == 1:
            players[0].receive_damage(300)
    else:
        print("何も起こらなかった！")
    print("プレイヤー{} 残りHP：{}".format(players[0].name, players[0].hp))
    print("プレイヤー{} 残りHP：{}".format(players[1].name, players[1].hp))

    # 勝敗判定
    if players[0].hp <= 0: # A戦闘不能
        print("プレイヤー{}は倒れた！".format(players[0].name))
        print("プレイヤー{}の勝利！".format(players[1].name))
        break
    elif players[1].hp <= 0: # B戦闘不能
        print("プレイヤー{}は倒れた！".format(players[1].name))
        print("プレイヤー{}の勝利！".format(players[0].name))
        break
    
    # 攻守交代
    print("攻守交代")
    if atk_turn == 0:
        atk_turn = 1
    else:
        atk_turn = 0
    
    total_turns += 1
    print()
"""