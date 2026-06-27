"""
モンティ・ホール問題 〜実践編〜

monty_hall_simulation関数を1000回実行し、
ヤギと車それぞれ何階ずつ引き当てたか集計する
試行回数を増やせば、実際に出る結果の割合は、真の確率に近づく

プレイヤーが最初に選ぶドア番号はランダムにし、
最後にドアを変更するかどうかは、TrueかFalseのどちらかで固定する
Trueで固定したパターン、Falseで固定したパターンをどちらも実行して結果を集計する
"""

import random


# 関数：モンティホール
def monty_hall_simulation():
    
    # ドアのリストを作成してシャッフルする
    doors = ["ヤギ", "ヤギ", "車"]
    random.shuffle(doors)
    
    # プレイヤーが最初に選ぶドアの番号をランダムに決定し、変数player_choiceに代入する
    
    # モンティが開けるドアの番号を決めた変数monty_choiceに代入する
    available_doors = []
    for i in range(3):
        if (i != player_choice) and (doors[i] == "ヤギ"):
            available_doors.append(i)
    monty_choice = random.choice(available_doors)
    
    # 変更する(True)か、変更しない(False)かを変数is_switchに代入する
    
    # プレイヤーがドアを変更する場合、変数player_choiceのドア番号を更新する
    if is_switch:
        for i in range(3):
            if i != player_choice and i != monty_choice:
                player_choice = i
                break
            
    # 最終的にプレイヤーが選んだドアの結果を返す
    return doors[player_choice]
    
# 結果を集計するための辞書を作成する

# シミュレーションを実行し、結果を表示する