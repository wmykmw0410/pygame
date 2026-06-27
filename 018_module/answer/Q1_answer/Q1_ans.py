"""random,timeモジュールを使用して、ジャンケンゲームを作る"""
# randomモジュールをインポート
import random
import time

# ジャンケン
janken = ["rock", "paper", "scissors"]
result = random.choice(janken)

print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print(result)