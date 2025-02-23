## アプリ名: MyHandwritingFont

## アプリの仕様
**概要**
自分の手書き文字をフォントに変換するアプリです。ペンタブやマウスで文字を書いて、それをデジタルフォント（.ttf形式）に変換することで、手書き風の履歴書などに利用できます。対応OSはWindowsです。

### インストール
1. [Ghostscript](https://ghostscript.com/index.html)をインストールしてください。
2. リポジトリをクローン: `git clone https://github.com/Jun-Hirao/MyHandwritingFont.git`
3. 依存関係をインストール: `pip install -r requirements.txt`
4. 実行: `python src/myhandwritingfont/main.py`

### 使い方
1. アプリ起動したら、キャンバスに1文字手書き。
2. 保存ボタンでPNGに保存。
3. フォント生成ボタンで.ttfファイルが`output/`に出力されます。
4. 生成されたttfをPCにインストールする等でご利用できます。

## 開発環境
- Windows11(23H2)
- pyenv-win
- Python 3.11.9
- venv
- Ghostscript 10.04.0


## コーディング規約
コーディング規約はリポジトリ直下の [CODING_GUIDELINES.md](CODING_GUIDELINES.md) で定義されています。
変更する場合はレビューが必要です。

## ディレクトリ構造
ディレクトリ構造はリポジトリ直下の [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) で定義されています。
変更する場合はレビューが必要です。

## ライセンス
MIT ライセンスです。詳細は [LICENSE](LICENSE) を参照してください。

