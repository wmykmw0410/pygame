"""Q4. 図形パッケージ

circle.py と rectangle.py を shapes パッケージにまとめ、2パターンの呼び出し方を確認する

step1. shapes/ フォルダを作り __init__.py を作成する

step2. circle.py に以下の関数を作る
       ・area(r)       → 円の面積（math.pi * r ** 2）
       ・perimeter(r)  → 円の周長（2 * math.pi * r）

step3. rectangle.py に以下の関数を作る
       ・area(w, h)       → 長方形の面積
       ・perimeter(w, h)  → 長方形の周長

step4. __init__.py に全関数をエクスポートする
       ・circle_area / circle_perimeter / rectangle_area / rectangle_perimeter

step5. 2パターンで呼び出す
       ・use_module.py → from shapes import circle を使う
       ・use_init.py   → from shapes import circle_area を使う（__init__.py 経由）

※ shapes/ フォルダ + use_module.py + use_init.py をこのフォルダに作成する
"""
