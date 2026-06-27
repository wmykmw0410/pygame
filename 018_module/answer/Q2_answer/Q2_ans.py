"""datetimeモジュールを使用して、誕生日から何日経過したか計算する"""
# datetimeモジュールをインポート
import datetime

# 今日の年月日を取得
today = datetime.date.today()
birthday = datetime.date(2000,1,1)
print(today-birthday)