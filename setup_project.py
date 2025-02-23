#!/usr/bin/env python3
"""
使い方: $ python setup_project.py

プロジェクトの初期ディレクトリ構造とファイルを作成するスクリプト

【対象】
- 既に作成済み：.github/ とその中のファイル、CODING_GUIDELINES.md、PROJECT_STRUCTURE.md、README.md
- このコードで新規作成：CODING_GUIDELINES.mdの中に書いてあるその他のディレクトリおよびファイル
"""

import os

def create_dir(path):
    """ディレクトリが存在しなければ作成する"""
    if not os.path.exists(path):
        print(f"Creating directory: {path}")
        os.makedirs(path)
    else:
        print(f"Directory exists: {path}")

def create_file(path, content=""):
    """ファイルが存在しなければ作成する。存在する場合はスキップ"""
    if not os.path.exists(path):
        print(f"Creating file: {path}")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    else:
        print(f"File exists: {path}")

def main():
    # プロジェクトルート（このスクリプトを実行したディレクトリ）を基準にする
    base = os.getcwd()

    # 生成済みのファイルはスキップするため、対象外として明記
    skip_files = {
        os.path.join(base, ".github"),
        os.path.join(base, "CODING_GUIDELINES.md"),
        os.path.join(base, "PROJECT_STRUCTURE.md"),
        os.path.join(base, "README.md")
    }

    # デフォルトのパッケージ名（必要に応じて変更してください）
    package_name = "your_package"
    src_dir = os.path.join(base, "src")
    package_dir = os.path.join(src_dir, package_name)
    subpackage_dir = os.path.join(package_dir, "subpackage")

    # 作成するディレクトリ一覧
    dirs_to_create = [
        os.path.join(base, "src"),
        package_dir,
        subpackage_dir,
        os.path.join(base, "tests"),
        os.path.join(base, "tests", "integration"),
        os.path.join(base, "docs"),
        os.path.join(base, "docs", "source"),
        os.path.join(base, "docs", "build"),
        os.path.join(base, "scripts"),
    ]

    for d in dirs_to_create:
        create_dir(d)

    # 生成するファイルとその初期コンテンツ
    files_to_create = {
        # src/[package_name]/ 以下
        os.path.join(package_dir, "__init__.py"): f"# {package_name} package initialization\n",
        os.path.join(package_dir, "module1.py"): (
            "# module1.py\n\n"
            "def sample_function():\n"
            "    \"\"\"サンプル関数\"\"\"\n"
            "    pass\n"
        ),
        os.path.join(subpackage_dir, "__init__.py"): "# subpackage initialization\n",
        os.path.join(subpackage_dir, "module_sub.py"): (
            "# module_sub.py in subpackage\n\n"
            "def sub_function():\n"
            "    \"\"\"サブパッケージ内のサンプル関数\"\"\"\n"
            "    pass\n"
        ),
        # tests/ 以下
        os.path.join(base, "tests", "conftest.py"): "# pytest 共通フィクスチャ設定\n",
        os.path.join(base, "tests", "__init__.py"): "# tests パッケージ初期化\n",
        os.path.join(base, "tests", "test_module1.py"): (
            "def test_sample_function():\n"
            "    # TODO: module1.py のテストを実装\n"
            "    assert True\n"
        ),
        os.path.join(base, "tests", "integration", "__init__.py"): "# integration tests 初期化\n",
        os.path.join(base, "tests", "integration", "test_integration.py"): (
            "def test_integration_sample():\n"
            "    # TODO: 統合テストを実装\n"
            "    assert True\n"
        ),
        # docs/ 以下
        os.path.join(base, "docs", "source", "conf.py"): (
            "# Sphinx configuration file\n\n"
            "project = 'Your Project Name'\n"
            "extensions = []\n"
        ),
        os.path.join(base, "docs", "source", "index.rst"): (
            "Your Project Name\n"
            "=================\n\n"
            "Welcome to the documentation!\n"
        ),
        # scripts/ 以下
        os.path.join(base, "scripts", "validate_structure.py"): (
            "#!/usr/bin/env python3\n"
            "\"\"\"Script to validate the project directory structure\"\"\"\n\n"
            "import os\n"
            "import sys\n\n"
            "def main():\n"
            "    print('Validation script placeholder')\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    main()\n"
        ),
        # ルート直下のファイル
        os.path.join(base, ".gitignore"): (
            "# Byte-compiled / optimized / DLL files\n"
            "__pycache__/\n"
            "*.py[cod]\n"
        ),
        os.path.join(base, "pyproject.toml"): "# pyproject.toml - Build system configuration\n",
        os.path.join(base, "requirements.txt"): "# requirements.txt - List your dependencies here\n",
        os.path.join(base, "LICENSE"): "Your license information here\n",
        os.path.join(base, "setup.cfg"): "# setup.cfg - Package metadata and configuration\n",
    }

    for file_path, content in files_to_create.items():
        # スキップ対象のパスと一致するかどうかは、ディレクトリの場合のみチェック
        skip = False
        for skip_path in skip_files:
            if file_path.startswith(skip_path):
                skip = True
                break
        if not skip:
            create_file(file_path, content)

    print("\n※ 下記のディレクトリ・ファイルは既に存在するため、編集や再作成は行いません:")
    print("   .github/ , CODING_GUIDELINES.md , PROJECT_STRUCTURE.md , README.md")

if __name__ == "__main__":
    main()
