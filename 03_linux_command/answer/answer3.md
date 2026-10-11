Q. Pythonの実行
step1. 「Question」フォルダの中に、"Hello, World" を出力するPythonファイルを作成する
step2. 相対パスを使ってそのファイルを実行する
step3. 一度ホームディレクトリまで移動し、絶対パスを使って同じファイルを実行する
step4. 確認できたら「Question」フォルダを中身ごと削除する

```bash
# 「Question」フォルダへ移動する（中には練習2で作った A, B フォルダもある）
cd ~/Question

# pythonファイルを作成する
touch hello.py
echo 'print("Hello, World")' > hello.py

# 内容を確認する
cat hello.py

# 相対パスで実行する
python ./hello.py

# ホームディレクトリへ移動する
cd ~

# 絶対パスで実行する（パスは練習1の pwd で確認した内容に置き換える）
python /home/user/Question/hello.py

# 後片付け（A, B フォルダも含めて Question ごと削除する）
rm -r Question
```
