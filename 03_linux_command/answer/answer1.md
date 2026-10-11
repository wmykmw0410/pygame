Q. パスの理解
step1. ホームディレクトリの1つ下に「Question」フォルダを作る
step2. 「Question」フォルダの絶対パスを pwd で確認する
step3. 一度ホームディレクトリに戻り、相対パスだけを使って「Question」フォルダに移動する

```bash
# ホームディレクトリに移動する
cd ~

# 「Question」フォルダを作成する
mkdir Question

# 作成したフォルダへ移動して、絶対パスを確認する
cd Question
pwd
# → /home/user/Question のように表示される（ユーザー名などは環境によって異なる）

# 一度ホームディレクトリへ戻る
cd ~

# 相対パスだけを使って「Question」フォルダへ移動する
cd Question
# 「./」は省略できるので cd ./Question と同じ意味
```
