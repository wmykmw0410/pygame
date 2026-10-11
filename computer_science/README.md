# コンピュータサイエンスの基礎

アルゴリズムやデータ構造など、Python の文法だけでは触れきれない「プログラミングを支える考え方」をまとめたリファレンス。[docs/python_grammar/](../docs/python_grammar/README.md) が「Pythonの書き方」を扱うのに対し、こちらは「どう考えてコードを書くか」を扱う。

| ファイル | 内容 |
| --- | --- |
| [01_algorithms.md](01_algorithms.md) | アルゴリズムとは何か・探索（線形探索・二分探索）・ソート・再帰 |
| [02_data_structures.md](02_data_structures.md) | スタック・キュー・木構造・グラフの考え方 |
| [03_computational_complexity.md](03_computational_complexity.md) | 計算量（Big-O 記法）の考え方 |
| [04_data_representation.md](04_data_representation.md) | 2進数・浮動小数点の誤差・メモリとミュータビリティ |

## 対象読者・方針

[CURRICULUM_SCOPE.md](../CURRICULUM_SCOPE.md) と同じく、Python 初学者の中学生・高校生を対象にしている。ネットワーク・OS・データベースのような、プログラミングと直結しない一般的なコンピュータの教養は扱わず、**このリポジトリのゲーム制作コードを読み書きするうえで実際に役立つ考え方**に絞っている。可能な限り、このリポジトリの既存コード（`25_Tetris`・`21_super_mario`・`27_bou_taoshi` など）を具体例として使う。

## 使い方

- レッスンを進める中で「なぜこう書くのか」「もっと良い書き方は無いか」と感じたときに、辞書的に参照する。
- レッスンのように順番にやる必要は無い。[docs/python_grammar/](../docs/python_grammar/README.md) と同様、知りたいときに読む使い方を想定している。
