# datetimeモジュールをインポートする
import datetime

# 今日の日付を表示する
today = datetime.date.today()
print(today)

# 今の時刻を表示する
d = datetime.datetime.now()
print(d.hour)
print(d.minute)
print(d.second)