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
  - [ ] 02_btn_to_jamp
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
- [ ] 20_sprite — Sprite / Group によるオブジェクト管理（21_super_mario の準備）
  - [ ] ex01
  - [ ] ex02
  - [ ] ex03
  - [ ] ex04

### 発展
- [ ] 21_super_mario — スーパーマリオ
- [ ] 22_tap_flight — SPACEで羽ばたいて障害物をすり抜けるタップフライト
  - [ ] ステップ1〜6
- [ ] 23_invader_squad — 弾幕シューティング
  - [ ] ステップ1〜7
- [ ] 24_reversi — リバーシ
  - [ ] ステップ1〜6
- [ ] 25_Tetris — テトリス
- [ ] 26_regex_battle — 一般的なタイピングゲームからレベルアップする呪文詠唱バトル（re モジュール）
  - [ ] ステップ1〜6
- [ ] 27_bou_taoshi — 棒倒し法による迷路生成
  - [ ] ex01
  - [ ] ex02
- [ ] 28_ana_hori — 穴掘り法による迷路生成
  - [ ] ex01
- [ ] 29_search — 探索アルゴリズム（線形探索・二分探索）
  - [ ] ex01
  - [ ] ex02
- [ ] 30_sort — 選択ソートでランキングを作る
  - [ ] ex01
- [ ] 31_delivery_race — ダイクストラ法で最短経路を進むCPUとの配達レース
  - [ ] ステップ1〜6
- [ ] 32_rogue_maze — 霧（視界）と追跡してくる敵から逃げるランダム生成迷路のローグライク
  - [ ] ステップ1〜6
- [ ] 33_dot_chase — ランダム生成迷路のドットを集めながら、4種類の追い方をする敵から逃げる（レベル1〜3）。レベル4は固定のオリジナル迷路によるクラシック版。パワーエサで一時的に敵を食べられる
  - [ ] ステップ1〜6
- [ ] 34_arcade_intro — pygameではなく Python Arcade ライブラリで基礎を触り、クラシックなインベーダーゲームを作る。敵編隊の移動はNumPyでも書き直す（カリキュラム本編とは別のライブラリ比較レッスン）
  - [ ] ex01
  - [ ] ex02
  - [ ] ex03
  - [ ] ステップ1〜6（インベーダーゲーム）
  - [ ] ex01
  - [ ] ex02
  - [ ] ex03

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
| 20_sprite | Sprite / Group | 敵キャラをランダムに動かし、壁や敵同士で跳ね返らせる。キーボードで Group への追加・削除・全削除を操作する（21_super_mario の準備） | [README](20_sprite/README.md) |

### 発展

| フォルダ | テーマ | 概要 | リンク |
| --- | --- | --- | --- |
| 21_super_mario | スーパーマリオ | 横スクロールアクションの実装（Sprite / Group を活用） | [README](21_super_mario/README.md) |
| 22_tap_flight | タップ操作アクション | 重力で落下するキャラクターをSPACEキーで羽ばたかせ、周期的に現れる障害物の隙間をすり抜けてスコアを稼ぐ | [README](22_tap_flight/README.md) |
| 23_invader_squad | 弾幕シューティング | 19の続きのボス戦。Player/Bulletは19から流用し、math.sin/cos/atan2でボスの楕円軌道・直進/螺旋/放射状/蛇行/追跡弾/狙い撃ち弾幕を実装。ダメージに応じて6段階で激しくなる | [README](23_invader_squad/README.md) |
| 24_reversi | 盤面ゲーム | 石で相手を挟んでひっくり返すリバーシ。合法手判定・パス処理・簡単なCPU（ランダム着手）まで実装する | [README](24_reversi/README.md) |
| 25_Tetris | テトリス | ゼロからテトリスを段階的に実装するハンズオン | [README](25_Tetris/README.md) |
| 26_regex_battle | 正規表現 | 一般的なタイピングゲーム（決まった単語）から始まり、スコアに応じて単語が長くなり、HARDレベルでは正規表現の条件に合う候補を選ぶ形式へレベルアップする呪文詠唱バトル | [README](26_regex_battle/README.md) |
| 27_bou_taoshi | 迷路生成 | 棒倒し法のアルゴリズムで迷路ができる様子を1本ずつ確認し、その迷路から制限時間内に脱出するゲームを作る | [README](27_bou_taoshi/README.md) |
| 28_ana_hori | 迷路生成 | 穴掘り法のアルゴリズムで、部屋を1つずつ掘り進めて迷路ができる様子を確認する。棒倒し法（27）とのアルゴリズム比較 | [README](28_ana_hori/README.md) |
| 29_search | 探索アルゴリズム | 線形探索・二分探索を1ステップずつ確認して見比べる。並べ替え済みかどうかで選べるアルゴリズムと必要な比較回数が変わることを体感する | [README](29_search/README.md) |
| 30_sort | ソートアルゴリズム | 選択ソートでスコアを降順に並べ替え、ランキングができる過程を1ステップずつ確認する | [README](30_sort/README.md) |
| 31_delivery_race | グラフ・探索 | マスごとにコストが違うグリッド上で、プレイヤーが手動配達し、ダイクストラ法で最短コスト経路を進むCPUとタイムレースする | [README](31_delivery_race/README.md) |
| 32_rogue_maze | グラフ・探索（ターン制ローグライク） | ランダム生成迷路を霧（視界）付きで探索し、探知範囲に入ると追いかけてくる敵から逃げて出口を目指すターン制ゲーム | [README](32_rogue_maze/README.md) |
| 33_dot_chase | ドット収集＋追跡アクション | ランダム生成迷路のドットを集めながら、レベルごとに増える性格の違う敵から逃げる（レベル1〜3は手続き生成、レベル4は固定のオリジナル迷路によるクラシック版）。パワーエサを取ると一時的に敵を食べられる | [README](33_dot_chase/README.md) |
| 34_arcade_intro | ライブラリ比較（Python Arcade / NumPy） | pygameではなく Arcade ライブラリでウィンドウ表示・図形描画・スプライト移動の基礎を触ったあと、クラシックな隣列行進形式のインベーダーゲームを作る。敵編隊の移動計算をNumPyの配列演算で書き直し、forループとの違いも見る。カリキュラム本編（pygame）とは別のライブラリ入門レッスン | [README](34_arcade_intro/README.md) |

### 補足

| フォルダ | 内容 |
| --- | --- |
| [docs/vscode_basics.md](docs/vscode_basics.md) | VSCode の使い方リファレンス |
| [docs/python_grammar/](docs/python_grammar/README.md) | Python 文法リファレンス（基礎・中級・発展） |
| [docs/pixel_art_tool.md](docs/pixel_art_tool.md) | ドット絵エディタ（Pixnote Editor Lite）の紹介。`*_pixels.txt`形式のドット絵を作るときに使う |
| [computer_science/](computer_science/README.md) | CS基礎リファレンス（アルゴリズム・データ構造・計算量・データ表現） |
| [02_draw_shapes/color_code.md](02_draw_shapes/color_code.md) | カラーコード一覧（色名・RGB・RGBA） |
| [05_event_process/keycode.md](05_event_process/keycode.md) | キーコード一覧（定数・数値） |
| 00_assets | 共通の画像・サウンド素材 |
