"""
モンティ・ホール問題
ここに3つのドアがあります。
1つのドアには当たりとして車を、その他2つはにはハズレとしてヤギをランダムに入れました。
さて、あなたはこの3つのドアのうち1つを選んでもらいます。
でも、どのドアの後ろに車があるかは分かりません。

あなたが1つのドアを選んだ後、
私は残った2つのドアのうち、ヤギがいるドアを1つ開けます。
すると、あなたの選んだドアと、もう1つのドアが残ります。

「選んだドアのままにしますか？それとも、もう1つのドアにしますか？」

最後の質問において、どちらかの選択をすると車を引き当てる確率が2倍になることが知られています。

次の条件に沿って、まずはこの問題を再現するmonty_hall_simulation関数を作成する

<条件>
・monty_hall_simulationの引数はなし
最終的にプレイヤーが選んだドアの中身を戻り値として返す

・ドアの中身は次のリストで定義し、ゲーム開始時にシャッフルする
doors = ["ヤギ", "ヤギ", "車"]

・最初にドアを選択する際は、シェルからドアの要素番号(0~2)を入力する
存在しない要素番号や数値として認識できない文字を入力されたとしても
エラーは出さず、Noneを戻り値として返す

・モンティが選んだドアの番号の中身は、必ず出力する

・ドアを変更するかどうかは"Yes","No"をシェルから入力させる
ただし、大文字と小文字は区別はしない
それ以外の文字は全て"No"とみなす

<ポイント>
・モンティは、プレイヤーの選んでいないドアのうち、ヤギが入っているドアを1つだけ開ける
プレイヤーが最初に車のドアを選び、残りがどちらもヤギでも、その中からランダムで1つを選ぶ
プレイヤーが選んでいないかつ中身がヤギのドアを一旦リストに格納し、
その中からランダムに1つ選べば、モンティの操作を再現できる
"""

import random


# 関数：モンティホール
def monty_hall_simulation():
    
    # ドアのリストを作成してシャッフルする
    doors = ["ヤギ", "ヤギ", "車"]
    random.shuffle(doors)
    
    # 最初に選ぶドアの番号をプレイヤーに入力させ、変数player_choiceに代入する
    # 存在しないドアまたは数値として認識できない文字が入力されたらNoneを返す
    try:
        player_choice = int(input("ドアを選択してください(0~2):"))
        # if (player_choice < 0) or (player_choice > 2):
        if not (0 <= player_choice <=2):
            return None
        
    except ValueError:
        return None
    
    # モンティが開けるドアの番号を決めた変数monty_choiceに代入する
    available_doors = []
    for i in range(3):
        if (i != player_choice) and (doors[i] == "ヤギ"):
            available_doors.append(i)
    monty_choice = random.choice(available_doors)
    
    # モンティの開けたドアの要素番号と中身を公開する
    print(f"モンティが開けたドアの番号: {monty_choice}, 中身: {doors[monty_choice]}")
    
    # プレイヤーがドアを変更するかどうか決める
    # 変更する(True)かしない(False)かを変数is_switchに代入する
    switch_input = input("ドアを変更しますか?(Yes/No):")
    is_switch = switch_input.lower() == "yes"
    
    # プレイヤーがドアを変更する場合、変数player_choiceのドア番号を更新する
    if is_switch:
        for i in range(3):
            if i != player_choice and i != monty_choice:
                player_choice = i
                break
            
    # 最終的にプレイヤーが選んだドアの結果を返す
    return doors[player_choice]
    
# 関数を実行し、プレイヤーが選んだドアの中身を表示する
print(f"プレイヤーが選んだドアの中身: {monty_hall_simulation()}")
            