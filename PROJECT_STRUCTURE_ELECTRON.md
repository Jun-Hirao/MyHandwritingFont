# ディレクトリ構造
```
this-repository/  
├── .github/  
│   ├── workflows/  
│   │   └── validate-structure.yml  
│   └── ISSUE_TEMPLATE/  
│       └── FEATURE_REQUEST.md  
├── src/  
│   ├── main.js                # Electronのメインプロセスのエントリーポイント  
│   ├── preload.js             # レンダラープロセスとメインプロセス間の安全な通信のためのプリロードスクリプト  
│   └── renderer/              # レンダラープロセス（UI関連）のソースコード  
│       ├── index.html         # アプリのメインHTML  
│       ├── renderer.js        # ブラウザ側のロジック  
│       └── style.css          # UI用のスタイルシート  
├── tests/  
│   ├── unit/                  # 単体テスト用のコード  
│   │   ├── test_main.js       # メインプロセスの単体テスト  
│   │   └── test_renderer.js   # レンダラープロセスの単体テスト  
│   └── integration/           # 統合テスト（またはE2Eテスト）用のコード  
│       ├── test_integration.js  
│       └── helper.js          # テスト補助用の共通関数や設定
├── dist/                      
│   └── app_name/              # Electron-packagerでビルドされた実行可能なパッケージ、packager.jsonで決めた任意のアプリ名
│       └── (生成ファイル)      # 実行可能なexeファイルを含む
├── docs/  
│   ├── source/  
│   │   ├── index.md           # ドキュメントのメインエントリーポイント（Markdown形式など）  
│   │   └── config.yml         # ドキュメント生成ツール（例：MkDocsなど）の設定ファイル  
│   └── build/                 # 生成されたドキュメント（HTML等）の出力先  
│       └── (生成ファイル)  
├── scripts/  
│   ├── validate_structure.js  # CI/CDやローカルでディレクトリ構造を検証するためのスクリプト  
│   └── build.js               # ビルドやパッケージングを補助するスクリプト  
├── vendor/  
│   └── node/                  # ポータブルなNode.js環境（バイナリや必要なファイル。npmなど）  
├── node_modules/              # パッケージが保存されるディレクトリ(ElectronとElectron-packagerもこの中に入る)
├── .gitignore                 # Gitで管理しないファイルやディレクトリの指定  
├── package.json               # プロジェクト全体の依存パッケージ、スクリプト、メタデータの設定ファイル  
├── package-lock.json          # npmによる依存パッケージのバージョン固定ファイル（npm利用時）  
├── README.md                  # プロジェクト概要、セットアップ手順、使用方法などを記載  
├── CODING_GUIDELINES.md       # コーディング規約の詳細  
├── PROJECT_STRUCTURE.md       # 本ファイル：プロジェクトのディレクトリ構造と運用ルール  
├── LICENSE                    # プロジェクトのライセンス情報  
└── electron-packager-config.json  # Electron-packager用の設定ファイル（必要に応じて）
```
# 各ディレクトリとファイルの説明

## this-repository/
プロジェクトのルートディレクトリです。すべての設定ファイル、ソースコード、テスト、ドキュメント等が含まれます。

### .github/
GitHub上でのCI/CDやIssue管理に関する設定ファイルを配置します。

- **workflows/**  
  - `validate-structure.yml`: プッシュやプルリクエスト時に、`scripts/validate_structure.js`などを用いてプロジェクト構造が規約に沿っているか検証するCI/CDワークフローを定義します。  
- **ISSUE_TEMPLATE/**  
  - `FEATURE_REQUEST.md`: 機能要望や改善案のためのIssueテンプレートです。

### src/
Electronアプリの主要ソースコードを配置するディレクトリです。

- **main.js**  
  - Electronのメインプロセスのエントリーポイント。ウィンドウ生成やアプリ全体のライフサイクル管理を担当します。  
- **preload.js**  
  - レンダラープロセスとメインプロセス間で安全に通信するためのプリロードスクリプトです。  
- **renderer/**  
  - ユーザーインターフェース（UI）に関連するファイル（HTML、JavaScript、CSS）を格納します。

### tests/
アプリの単体テストや統合テスト（またはE2Eテスト）を配置するディレクトリです。

- **unit/**  
  - 各モジュール単位のテストコードを配置します。例として、メインプロセスとレンダラープロセスのテストファイルを格納。  
- **integration/**  
  - 複数モジュールが連携する際の統合テストやシステム全体の挙動を検証するテストコードを配置します。  
  - 補助的な関数や設定が必要な場合は、`helper.js`などのファイルを追加してください。

### dist/
Electron-packagerでビルドされた実行可能なパッケージを配置するディレクトリです。

- **app_name/**  
  - Electron-packagerでビルドするとpackager.jsonで決めた任意のアプリ名でここに格納されます。


### docs/
プロジェクトのドキュメントを管理するディレクトリです。

- **source/**  
  - ドキュメントの元となるソースファイル（Markdown、RSTなど）と生成ツールの設定ファイル（例：config.yml）を配置します。  
- **build/**  
  - ドキュメント生成ツール（例：MkDocsやその他）の出力先として使用します。生成されたHTMLなどが格納されます。

### scripts/
開発支援やCI/CD、ビルド・パッケージング等のための補助スクリプトを配置します。

- **validate_structure.js**  
  - リポジトリ内のディレクトリ構造が規約通りになっているか検証するスクリプトです。  
- **build.js**  
  - アプリのビルドやパッケージング（Electron-packagerの呼び出し等）を補助するスクリプトです。

### vendor/
ポータブル環境に対応するため、リポジトリ内に同梱する外部ツールやランタイムを配置します。

- **node/**  
  - プロジェクトで利用するポータブルなNode.js環境（バイナリや関連ファイル）を保持します。npmもこの中に入ります。

### node_modules/
npm install -D するとパッケージがここに保存されます。electronとelectron-packagerがここに入ります。

### 主要ファイル（ルート直下）

- **.gitignore**  
  - Gitで管理対象外とするファイルやディレクトリ（例：ビルド成果物や一時ファイル）を指定します。  
- **package.json**  
  - プロジェクトの依存パッケージ、スクリプト、メタデータを管理するファイルです。Electron関連の設定やパッケージングのスクリプトもここに記載可能です。  
- **package-lock.json**  
  - npmによる依存関係のバージョン固定ファイルです。  
- **README.md**  
  - プロジェクト概要、セットアップ手順、使用方法、依存関係など、開発者および利用者向けの情報を記載します。  
- **CODING_GUIDELINES.md**  
  - チーム内でのコーディング規約やベストプラクティスを記載します。  
- **PROJECT_STRUCTURE.md**  
  - 本ファイル。プロジェクトのディレクトリ構造とその運用ルールを明示します。  
- **LICENSE**  
  - プロジェクトに適用するライセンス文書です。  
- **electron-packager-config.json**  
  - Electron-packager利用時の設定を記述するためのファイルです（必要に応じて）。

# ディレクトリ規約と運用ルール

1. **新規追加時のルール**  
   - 新しいモジュール、テスト、ドキュメント、スクリプト、もしくは外部ツール（例：Node.js、Electron）の追加時は、本規約に沿い適切なディレクトリに配置してください。  
   - ファイル名、ディレクトリ名は一貫性を持って命名し、用途ごとに分かりやすくしてください。

2. **変更時のルール**  
   - ディレクトリ構造やファイル配置に変更が必要な場合は、チーム内で議論し、合意の上で本ファイル（PROJECT_STRUCTURE.md）を更新してください。  
   - 大きな変更はGitHubのIssueやPull Requestを通じてレビューを実施してください。

3. **CI/CDでの検証**  
   - `.github/workflows/validate-structure.yml`を用い、プッシュやプルリクエスト時に`scripts/validate_structure.js`などでディレクトリ構造の自動検証を実施することを推奨します。  
   - ローカル環境でも同様の検証スクリプトを利用し、規約遵守を確認できるようにしてください。
---

# 備考

- **ポータブル環境対応**  
  リポジトリ内にNode.js、Electron、Electron-packagerを保持することで、環境依存を排除し、誰でも同一環境でアプリをビルド・実行できるようにしています。  
  実際のプロジェクト作成時には、各ツールのバージョン管理と更新方法についてもチーム内で合意してください。

- **テストの構造**  
  単体テストと統合テスト（またはE2Eテスト）を明確に分けることで、テスト実行時の設定や依存関係の管理を容易にしています。必要に応じて追加のテストディレクトリを設けてもよいでしょう。

- **CI/CDの運用**  
  GitHub ActionsなどのCIツールを活用し、コード品質チェック、テスト自動実行、ディレクトリ構造の検証を実施して、プロジェクトの品質維持に努めてください。
