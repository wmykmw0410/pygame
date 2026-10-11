"""raise文の使用例"""

def calc_speed(dist, time):
    if time <= 0:
        raise ValueError("時間は0より大きい値を入力してください。")
    return dist / time

try:
    speed = calc_speed(10, 0)
    print(f"時速は{speed}km/hです。")
    
except ValueError as e:
    print(e)