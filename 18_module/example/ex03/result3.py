# greeting3モジュールのgreeting関数をインポート
"""パターン1
モジュール全体をインポート
使用したい関数は<モジュール名>.<関数名>で呼び出す
"""
# import greeting3
# print("A")
# greeting3.greetingA()
# greeting3.greetingB()
# print("B")


"""パターン2
モジュールから使用する関数をインポート
使用したい関数は<関数名>で呼び出す
"""
from greeting3 import greetingA
print("A")
greetingA()
# greetingB()  # NameError: インポートしていない関数は呼び出せない
print("B")