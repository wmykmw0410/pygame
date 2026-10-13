# Pygame 学習カリキュラム

```
次回:

メモ:
```

---

## 進捗

### 準備
- [ ] 00_setup — 環境構築

### pygame 入門
- [ ] 01_window — ウィンドウ作成・ゲームループ
  - [ ] ex01
- [ ] 02_draw_shapes — 図形・テキスト描画・アニメーション
  - [ ] 01_draw_shapes
  - [ ] 02_draw_text
  - [ ] 03_rect_object
- [ ] 03_linux_command — ターミナル操作・Python ファイル実行
- [ ] 04_draw_images — 画像の読み込みと表示
  - [ ] ex01
  - [ ] ex02
  - [ ] ex03
- [ ] 05_event_process — キーボード・マウスイベント
  - [ ] 01_keyboard
  - [ ] 02_mouse
  - [ ] 03_push_flag
  - [ ] 04_event
- [ ] 06_function — 関数（定義・引数・スコープ）
  - [ ] ex01
  - [ ] ex02
  - [ ] ex03
  - [ ] ex04
- [ ] 07_switch_screen — 画面切り替え・ボタン処理
  - [ ] 01_display_page
  - [ ] 02_btn_to_jump
  - [ ] 03_page_branch
- [ ] 08_pathlib_module — pathlib によるパス管理

### ゲーム制作
- [ ] 09_actiongame — アクションゲーム
  - [ ] ex01
  - [ ] ex02
  - [ ] ex03
  - [ ] ex04
  - [ ] ex05
  - [ ] ex06
  - [ ] ex07
- [ ] 10_exception — 例外処理
- [ ] 11_multidimensional_list — リスト・タプル・辞書・二次元リスト
- [ ] 12_TicTocToe — マルバツゲーム（CLI → pygame）
  - [ ] CLI版
  - [ ] pygame版
- [ ] 13_BreakoutClone — ブロック崩し
  - [ ] ex01
  - [ ] ex02
  - [ ] ex03
- [ ] 14_shooting_game — シューティングゲーム
  - [ ] ex01
  - [ ] ex02
  - [ ] ex03
  - [ ] ex04
  - [ ] ex05

### Python 応用
- [ ] 15_class — オブジェクト指向（基礎）
  - [ ] ex01
  - [ ] ex02
  - [ ] ex03
  - [ ] Q1
  - [ ] Q2
  - [ ] Q3
- [ ] 16_battle_game — バトルゲーム（段階的実装）
  - [ ] ex01
  - [ ] ex02
  - [ ] ex03
- [ ] 17_BreakoutClone_class_ver — クラス化練習（ブロック崩し）
  - [ ] ex01
  - [ ] ex02
  - [ ] ex03
  - [ ] ex04
  - [ ] ex05
- [ ] 18_module — モジュール・パッケージ
  - [ ] Q1
  - [ ] Q2
  - [ ] Q3
  - [ ] Q4
- [ ] 19_shooting_game_class_ver — クラス化練習・ファイル分割（シューティング）
  - [ ] ex01
  - [ ] ex02
  - [ ] ex03
  - [ ] ex04
  - [ ] ex05
  - [ ] ex06（難易度変化）
  - [ ] package（ファイル分割）
- [ ] 20_sprite — Sprite / Group によるオブジェクト管理
  - [ ] ex01
  - [ ] ex02
  - [ ] ex03
  - [ ] ex04

---

## カリキュラム一覧

### 準備

| フォルダ | 概要 | リンク |
| --- | --- | --- |
| 00_setup | Python・pygame の環境構築 | [README](00_setup/README.md) |

### pygame 入門

| フォルダ | テーマ | 概要 | リンク |
| --- | --- | --- | --- |
| 01_window | ウィンドウ | ゲームウィンドウの作成、描画ループ、FPS 管理 | [README](01_window/README.md) |
| 02_draw_shapes | 図形描画 | 線・円・四角形・多角形・テキスト、アニメーション | [README](02_draw_shapes/README.md) |
| 03_linux_command | Linux コマンド | ターミナル操作、パス、Python ファイルの実行 | [README](03_linux_command/README.md) |
| 04_draw_images | 画像描画 | 画像ファイルの読み込みと座標指定表示 | [README](04_draw_images/README.md) |
| 05_event_process | イベント処理 | キーボード・マウス入力の取得と反映 | [README](05_event_process/README.md) |
| 06_function | 関数 | 関数定義・引数（位置・デフォルト・キーワード）・スコープ | [README](06_function/README.md) |
| 07_switch_screen | 画面切り替え | ページ変数とボタン処理による画面遷移 | [README](07_switch_screen/README.md) |
| 08_pathlib_module | pathlib | pathlib を使った画像・サウンドのパス管理 | [README](08_pathlib_module/README.md) |

### ゲーム制作

| フォルダ | テーマ | 概要 | リンク |
| --- | --- | --- | --- |
| 09_actiongame | アクションゲーム | 移動・衝突判定・ゲームオーバー・ゲームクリア | [README](09_actiongame/README.md) |
| 10_exception | 例外処理 | try/except、エラーの種類、random モジュール | [README](10_exception/README.md) |
| 11_multidimensional_list | 多次元リスト | リスト・タプル・辞書・二次元リスト・マトリクス表 | [README](11_multidimensional_list/README.md) |
| 12_TicTocToe | マルバツゲーム | CLI 版からの設計、pygame への移植 | [README](12_TicTocToe/README.md) |
| 13_BreakoutClone | ブロック崩し | バー・ボール・ブロック管理、衝突・スコア | [README](13_BreakoutClone/README.md) |
| 14_shooting_game | シューティング | 自機・弾・UFO・スコア、ゲームオーバー | [README](14_shooting_game/README.md) |

### Python 応用

| フォルダ | テーマ | 概要 | リンク |
| --- | --- | --- | --- |
| 15_class | OOP 基礎 | クラス・インスタンス・メソッド・継承 | [README](15_class/README.md) |
| 16_battle_game | OOP 実践 | 15_class の CLI 版を pygame 化し、パーティー化・反撃・連戦へ拡張する | [README](16_battle_game/README.md) |
| 17_BreakoutClone_class_ver | OOP 練習① | ブロック崩しを関数ベース→クラスへ段階的に書き直す | [README](17_BreakoutClone_class_ver/README.md) |
| 18_module | モジュール | モジュール・パッケージ・標準ライブラリ・相対インポート | [README](18_module/README.md) |
| 19_shooting_game_class_ver | OOP 練習②・ファイル分割 | シューティングゲームを段階的にクラス化し、モジュールの知識でクラスごとにファイル分割する | [README](19_shooting_game_class_ver/README.md) |
| 20_sprite | Sprite / Group | 敵キャラをランダムに動かし、壁や敵同士で跳ね返らせる。キーボードで Group への追加・削除・全削除を操作する | [README](20_sprite/README.md) |

### 補足

| 項目 | 内容 |
| --- | --- |
| [docs/vscode_basics.md](docs/vscode_basics.md) | VSCode の使い方リファレンス |
| [docs/python_grammar/](docs/python_grammar/README.md) | Python 文法リファレンス（基礎・中級・発展） |
| [pygame ドキュメント（日本語訳）](https://westplain.sakura.ne.jp/translate/pygame/) | pygame の関数・引数を調べるときのリファレンス（外部サイト。一部未翻訳） |
| [docs/pixel_art_tool.md](docs/pixel_art_tool.md) | ドット絵エディタ（Pixnote Editor Lite）の紹介。`*_pixels.txt`形式のドット絵を作るときに使う |
| [02_draw_shapes/color_code.md](02_draw_shapes/color_code.md) | カラーコード一覧（色名・RGB・RGBA） |
| [05_event_process/keycode.md](05_event_process/keycode.md) | キーコード一覧（定数・数値） |
| 00_assets | 共通の画像・サウンド素材 |
