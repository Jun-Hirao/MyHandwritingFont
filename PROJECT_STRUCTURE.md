# ディレクトリ構造
```
this-repository/  
├── .github/  
│   ├── workflows/  
│   │   └── validate-structure.yml  
│   └── ISSUE_TEMPLATE/  
│       └── FEATURE_REQUEST.md  
├── src/  
│   └── [package_name]/  
│       ├── __init__.py  
│       ├── main.py  
│       ├── drawing.py  
│       └── fontgen.py  
├── output/  
├── assets/  
├── tests/  
│   ├── conftest.py  
│   ├── __init__.py 
│   ├── test_module1.py  
│   └── integration/  
│       ├── __init__.py
│       └── test_integration.py  
├── scripts/  
│   ├── validate_structure.py  
│   └── other_tools.py 
├── .gitignore  
├── pyproject.toml  
├── requirements.txt
├── README.md
├── CODING_GUIDELINES.md
├── PROJECT_STRUCTURE.md
└── LICENSE

```
# 各ディレクトリとファイルの説明

## this-repository/
プロジェクトのルートディレクトリ。すべての設定ファイルと主要ディレクトリを含みます。

### .github/
GitHub関連の設定ファイルを格納します。

#### workflows/
- **validate-structure.yml**: CI/CDパイプラインの設定ファイル。プッシュ/プルリクエスト時に構造検証スクリプトを実行
- その他のワークフロー（テスト、デプロイなど）を追加可能

#### ISSUE_TEMPLATE/
- **機能要望.md**: 機能要望用のテンプレート
- その他のテンプレート（質問用、ドキュメント改善用など）を追加可能

### src/
メインのPythonパッケージコードを格納します。
#### **[package_name]/**
**プロジェクトのメインパッケージディレクトリです。通常、パッケージ名はプロジェクト名と同じにします。  **
  - `__init__.py`: パッケージの初期化ファイル
  - `module1.py`: 機能ごとに分割したモジュール例。モジュールは機能別に分割して配置します。  
  - サブパッケージは別ディレクトリに分割
  - **subpackage/**: より細かい機能やドメインごとに分割するためのサブパッケージ。  
    - `__init__.py`: サブパッケージの初期化ファイル。  
    - `module_sub.py`: サブパッケージ内のモジュール例。

### output/
手書きした文字のPNGや生成した.ttfを出力するフォルダです。

### assets/
アプリのアイコンなどの静的ファイルを保存するフォルダです。

### tests/
単体テスト、統合テスト、エンドツーエンドテストなど、テストコード全般を配置します。

- `conftest.py`: pytestのフィクスチャなど、共通のテスト設定を記述します。  
- `__init__.py`: テストコードをパッケージとして扱う場合に配置します（必須ではありません）。  
- `test_module1.py`: 対象モジュールに対する単体テスト。  
#### integration/
統合テストやシステム全体のテストを配置するディレクトリ。  

- `__init__.py`: 統合テストのパッケージ化用（必要に応じて）。  
- `test_integration.py`: 統合テストの例。


### scripts/
開発支援用のスクリプト類を格納します。
- **validate_structure.py**: CI/CDやローカルでプロジェクトのディレクトリ構造を検証するためのスクリプト。
- **other_tools.py**: その他、開発やデプロイ、データ生成などで使用するツール類を配置してください。

### 主要ファイル(ルート直下) 
- **.gitignore**: Gitで管理しないファイルやディレクトリを指定します。
- **LICENSE**: プロジェクトに適用するライセンス文書ファイル。
- **README.md**: プロジェクト概要説明、プロジェクトの仕様、セットアップ手順、使用方法、依存関係などを記載します。
- **CODING_GUIDELINES.md**: コーディング規約を記載します。
- **PROJECT_STRUCTURE.md**: 本ファイル。プロジェクトのディレクトリ構造とその説明を記載します。 

### 主要ファイル(Python)
- **requirements.txt**: Pythonの依存パッケージの一覧を記述します。
- **pyproject.toml**: PEP 518準拠のビルドシステム設定ファイルです。

# ディレクトリ規約と運用ルール

1. **新規追加時のルール**  
   - 新しいモジュール、テスト、ドキュメント、スクリプトを追加する場合は、本規約に則り適切なディレクトリに配置してください。  
   - ディレクトリ階層やファイル名は、一貫性をもって命名してください（例：テストファイルは`test_*.py`とするなど）。

2. **変更時のルール**  
   - ディレクトリ構造やファイル配置に変更が必要な場合は、チーム内で議論し、合意の上で本ファイル（PROJECT_STRUCTURE.md）を更新してください。  
   - 大きな変更の場合は、GitHubのIssueやPull Requestを通じてレビューを実施してください。

3. **CI/CDでの検証**  
   - `.github/workflows/validate-structure.yml`などを用いて、プッシュ時やプルリクエスト時にプロジェクト構造が規約に従っているか自動検証を実施することを推奨します。  
   - ローカルでも`scripts/validate_structure.py`を実行して、規約遵守を確認できるようにしてください。


---

# 備考

- **パッケージ名のプレースホルダ `[package_name]`**  
  実際のプロジェクト作成時には、プロジェクト名に合わせたディレクトリ名に置き換えてください。

- **テストの構造**  
  単体テストと統合テストを明確に分けることで、テスト実行時の設定や依存関係管理を容易にしています。必要に応じてE2Eテスト等のディレクトリを追加してください。

- **CI/CDの運用**  
  GitHub Actionsやその他のCIツールを活用して、コードの品質チェックやテスト自動実行、ディレクトリ構造の検証を行い、品質維持に努めてください。
