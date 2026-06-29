# Pygame 学習カリキュラム

```
次回:

メモ:
```

---

## 進捗

### 準備
- [ ] 00_setup — 環境構築
- [ ] 00_sample_game — サンプルゲーム体験

### pygame 入門
- [ ] 001_window — ウィンドウ作成・ゲームループ
  - [ ] ex01
- [ ] 002_draw_shapes — 図形・テキスト描画・アニメーション
  - [ ] 01_draw_shapes
  - [ ] 02_draw_text
  - [ ] 03_rect_object
- [ ] 003_linux_command — ターミナル操作・Python ファイル実行
- [ ] 004_draw_images — 画像の読み込みと表示
  - [ ] ex01
  - [ ] ex02
  - [ ] ex03
- [ ] 005_event_process — キーボード・マウスイベント
  - [ ] 01_keyboard
  - [ ] 02_mouse
  - [ ] 03_push_flag
  - [ ] 04_event
- [ ] 006_function — 関数（定義・引数・スコープ）
  - [ ] ex01
  - [ ] ex02
  - [ ] ex03
  - [ ] ex04
  - [ ] ex05
- [ ] 007_switch_screen — 画面切り替え・ボタン処理
  - [ ] 01_display_page
  - [ ] 02_btn_to_jamp
  - [ ] 03_page_branch
- [ ] 008_pathlib_module — pathlib によるパス管理

### ゲーム制作
- [ ] 009_actiongame — アクションゲーム
  - [ ] ex01
  - [ ] ex02
  - [ ] ex03
  - [ ] ex04
  - [ ] ex05
  - [ ] ex06
  - [ ] ex07
- [ ] 010_exception — 例外処理
- [ ] 011_multidimensional_list — リスト・タプル・辞書・二次元リスト
- [ ] 012_TicTocToe — マルバツゲーム（CLI → pygame）
  - [ ] CLI版
  - [ ] pygame版
- [ ] 013_BreakoutClone — ブロック崩し
  - [ ] ex01
  - [ ] ex02
  - [ ] ex03
- [ ] 014_shooting_game — シューティングゲーム
  - [ ] ex01
  - [ ] ex02
  - [ ] ex03
  - [ ] ex04
  - [ ] ex05

### Python 応用
- [ ] 015_class — オブジェクト指向（基礎）
  - [ ] ex01
  - [ ] ex02
  - [ ] ex03
  - [ ] ex04
  - [ ] ex05
  - [ ] ex06
  - [ ] ex07
- [ ] 016_battle_game — バトルゲーム（段階的実装）
  - [ ] Q1
- [ ] 017_BreakoutClone_class_ver — クラス化練習（ブロック崩し）
  - [ ] ex01
  - [ ] ex02
  - [ ] ex03
  - [ ] ex04
  - [ ] ex05
- [ ] 018_shooting_game_class_ver — クラス化練習（シューティング）
  - [ ] ex01
  - [ ] ex02
  - [ ] ex03
  - [ ] ex04
  - [ ] ex05
- [ ] 019_module — モジュール・パッケージ
  - [ ] Q1
  - [ ] Q2
  - [ ] Q3
  - [ ] Q4
- [ ] 020_frog_blaster — オブジェクト指向（ゲーム設計）
  - [ ] Q1
  - [ ] Q2

### 発展
- [ ] 021_Tetris — テトリス

---

## カリキュラム一覧

### 準備

| フォルダ | 概要 | リンク |
| --- | --- | --- |
| 00_setup | Python・pygame の環境構築 | [README](00_setup/README.md) |
| 00_sample_game | 完成ゲームを動かして全体像をつかむ | — |

### pygame 入門

| フォルダ | テーマ | 概要 | リンク |
| --- | --- | --- | --- |
| 001_window | ウィンドウ | ゲームウィンドウの作成、描画ループ、FPS 管理 | [README](001_window/README.md) |
| 002_draw_shapes | 図形描画 | 線・円・四角形・多角形・テキスト、アニメーション | [README](002_draw_shapes/README.md) |
| 003_linux_command | Linux コマンド | ターミナル操作、パス、Python ファイルの実行 | [README](003_linux_command/README.md) |
| 004_draw_images | 画像描画 | 画像ファイルの読み込みと座標指定表示 | [README](004_draw_images/README.md) |
| 005_event_process | イベント処理 | キーボード・マウス入力の取得と反映 | [README](005_event_process/README.md) |
| 006_function | 関数 | 関数定義・引数（位置・デフォルト・キーワード）・スコープ | [README](006_function/README.md) |
| 007_switch_screen | 画面切り替え | ページ変数とボタン処理による画面遷移 | [README](007_switch_screen/README.md) |
| 008_pathlib_module | pathlib | pathlib を使った画像・サウンドのパス管理 | [README](008_pathlib_module/README.md) |

### ゲーム制作

| フォルダ | テーマ | 概要 | リンク |
| --- | --- | --- | --- |
| 009_actiongame | アクションゲーム | 移動・衝突判定・ゲームオーバー・ゲームクリア | [README](009_actiongame/README.md) |
| 010_exception | 例外処理 | try/except、エラーの種類、random モジュール | [README](010_exception/README.md) |
| 011_multidimensional_list | 多次元リスト | リスト・タプル・辞書・二次元リスト・マトリクス表 | [README](011_multidimensional_list/README.md) |
| 012_TicTocToe | マルバツゲーム | CLI 版からの設計、pygame への移植 | [README](012_TicTocToe/README.md) |
| 013_BreakoutClone | ブロック崩し | バー・ボール・ブロック管理、衝突・スコア | [README](013_BreakoutClone/README.md) |
| 014_shooting_game | シューティング | 自機・弾・UFO・スコア、ゲームオーバー | [README](014_shooting_game/README.md) |

### Python 応用

| フォルダ | テーマ | 概要 | リンク |
| --- | --- | --- | --- |
| 015_class | OOP 基礎 | クラス・インスタンス・メソッド・継承 | [README](015_class/README.md) |
| 016_battle_game | OOP 実践 | バトルゲームを関数版→クラス版へ段階的に実装する | [README](016_battle_game/README.md) |
| 017_BreakoutClone_class_ver | OOP 練習① | ブロック崩しを関数ベース→クラスへ段階的に書き直す | [README](017_BreakoutClone_class_ver/README.md) |
| 018_shooting_game_class_ver | OOP 練習② | シューティングゲームを段階的にクラス化する | [README](018_shooting_game_class_ver/README.md) |
| 019_module | モジュール | モジュール・パッケージ・標準ライブラリ・相対インポート | [README](019_module/README.md) |
| 020_frog_blaster | OOP ゲーム | クラスを活用したゲーム設計・実装 | [README](020_frog_blaster/README.md) |

### 発展

| フォルダ | テーマ | 概要 | リンク |
| --- | --- | --- | --- |
| 021_Tetris | テトリス | ゼロからテトリスを段階的に実装するハンズオン | [README](021_Tetris/README.md) |

### 補足

| フォルダ | 内容 |
| --- | --- |
| [002_draw_shapes/color_code.md](002_draw_shapes/color_code.md) | カラーコード一覧（色名・RGB・RGBA） |
| 00_assets | 共通の画像・サウンド素材 |
