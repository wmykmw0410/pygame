# ドット絵エディタ（Pixnote Editor Lite）

→ [https://pixnote.net/apps/editor2/pixedit2.html](https://pixnote.net/apps/editor2/pixedit2.html)

ブラウザだけで使えるドット絵エディタ。インストール不要で、アクセスするとすぐに編集を始められる。

## このリポジトリでの使いどころ

このリポジトリでは、ブロック・土管・旗のようなシンプルなドット絵を、画像ファイルを直接置くのではなく「1文字 = 1ピクセル」のテキストグリッド（`*_pixels.txt`）で定義し、`_generate_assets.py` で画像に変換するレッスンがある（例: [21_super_mario](../21_super_mario/)の`block_pixels.txt`・`pipe_pixels.txt`・`flag_pixels.txt`）。

```
xxx##xxx
xx#..#xx
x#....#x
```
（`x` = 透明、それ以外の文字 = 色を割り当てたピクセル）

ドット絵エディタでマス目を見ながらデザインを考え、できあがった絵を1マスずつ文字に書き起こして`*_pixels.txt`を作る、という流れで使うと、テキストエディタだけで直接グリッドを書くよりもデザインしやすい。

## IPへの配慮

新しくドット絵を描くときは、`CLAUDE.md`の「IP・著作権への配慮」に従い、実在するゲームのドット絵をそのまま模写しない。ジャンルのお約束（例: 「土管らしい緑の円柱」）を踏まえて、独自に描き起こす。
