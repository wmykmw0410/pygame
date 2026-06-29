```text
pygameを動かすための環境を準備しましょう
```

| ツール | バージョン |
| --- | --- |
| Python | 3.12 系 |
| pip | 25.2 |
| pygame | 2.6.1（SDL 2.28.4） |

# 目次
- [Pythonのインストール](#pythonのインストール)
- [Pythonの確認](#pythonの確認)
- [pipの確認](#pipの確認)
- [pygameのインストール](#pygameのインストール)
- [pipのアップグレード](#pipのアップグレード)

---

# Pythonのインストール

公式サイト( https://www.python.org/downloads/ )から **Python 3.12系の最新版** を選んでダウンロードする

| OS | 手順 |
| --- | --- |
| Mac | `.pkg` ファイルをダウンロードして実行 |
| Windows | `.exe` ファイルをダウンロードして実行。インストール時に **「Add Python to PATH」にチェックを入れる** |
| Linux | `sudo apt install python3.12` |

> このカリキュラムでは **Python 3.12 系** を使用する

---

# Pythonの確認

```bash
python --version
```

バージョン番号が表示されればインストール済み

Pythonの実行ファイルがどこにあるか確認する

```bash
which python    # Mac / Linux
where python    # Windows
```

表示例（Mac）

```
/usr/local/bin/python3
```

`which` コマンドはPATHに登録されているコマンドの実体ファイルの場所を返す  
Windowsインストール時に「Add Python to PATH」にチェックを入れないと `where` で見つからず、コマンドも使えない

---

# pipの確認

pip はPythonのパッケージ管理ツール。Python 3.4以降は標準で同梱されている

```bash
pip --version
```

| OS | 表示例 |
| --- | --- |
| Mac / Linux | `pip 24.x.x from .../pip (python 3.x)` |
| Windows | 同上（表示されない場合は `py -m pip --version`） |

---

# pygameのインストール

| OS | コマンド |
| --- | --- |
| Mac / Linux | `pip install pygame==2.6.1` |
| Windows | `py -m pip install pygame==2.6.1` |

インストール確認

```bash
pip show pygame
```

以下のように表示されれば成功

```
Name: pygame
Version: 2.6.1
...
```

> このカリキュラムでは **pygame 2.6.1**（SDL 2.28.4）を使用する

---

# pipのアップグレード

以下のようなエラーが出た場合はpipをアップグレードする

```
[notice] A new release of pip is available: xx.x -> xx.x
ERROR: No matching distribution found for pygame
```

| OS | コマンド |
| --- | --- |
| Mac / Linux | `pip install --upgrade pip==25.2` |
| Windows | `py -m pip install --upgrade pip==25.2` |

> このカリキュラムでは **pip 25.2** を使用する
