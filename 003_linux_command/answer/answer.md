Q. 
step1. ローカルのターミナルから「Questionフォルダ」内に、"Hello, World"を出力する「pythonファイル」を作成し、実行する

# カレントディレクトリの確認
pwd

# 自身のフォルダへ移動
ls 
cd <パス>

# 「Questionフォルダ」の作成
mkdir Question

# 「pythonファイル」の作成
cd Question
touch python.py

# "Hello, World"を出力するように編集する
(A1)
echo 'print("Hello, World")' > python.py

(A2)
vi python.py
入力モード(i)に変更し、以下を入力
print("Hello, World")
コマンドモード(esc)に変更し、保存する(:wq)

# ファイル内容の確認
cat python.py

# pythonファイルの実行
python ./python.py

step2. ローカルのターミナルから「Questionフォルダ」と「pythonファイル」を削除する

# ファイルの削除
rm python.py
ls

# フォルダの削除
cd ..
rmdir Question
ls
