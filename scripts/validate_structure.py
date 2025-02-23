#!/usr/bin/env python3
# 使い方：$ python scripts/validate_structure.py
import os
import sys

def check_path(path, *, is_dir=False, required=True):
    """
    指定パスが存在するかどうかをチェックする。
    :param path: チェック対象のパス
    :param is_dir: ディレクトリであることを期待する場合 True を指定
    :param required: 存在しない場合にエラーとする場合 True
    :return: 存在していれば True、存在しなければ False
    """
    if is_dir:
        exists = os.path.isdir(path)
    else:
        exists = os.path.isfile(path)
    if not exists and required:
        kind = "directory" if is_dir else "file"
        print(f"Error: Expected {kind} '{path}' not found.")
    return exists

def check_structure():
    errors = False
    base = os.getcwd()  # スクリプト実行時のカレントディレクトリをリポジトリルートとする

    print("Starting directory structure validation...\n")

    # 1. .github 配下のチェック
    github_dir = os.path.join(base, ".github")
    if not os.path.isdir(github_dir):
        print("Error: .github directory not found.")
        errors = True
    else:
        # workflows/validate-structure.yml
        workflows_dir = os.path.join(github_dir, "workflows")
        if not check_path(workflows_dir, is_dir=True):
            errors = True
        else:
            workflow_file = os.path.join(workflows_dir, "validate-structure.yml")
            if not check_path(workflow_file):
                errors = True

        # ISSUE_TEMPLATE/BUG_REPORT.md, FEATURE_REQUEST.md
        issue_template_dir = os.path.join(github_dir, "ISSUE_TEMPLATE")
        if not check_path(issue_template_dir, is_dir=True):
            errors = True
        else:
            for template in ["BUG_REPORT.md", "FEATURE_REQUEST.md"]:
                template_path = os.path.join(issue_template_dir, template)
                if not check_path(template_path):
                    errors = True

    # 2. src/ 配下のチェック
    src_dir = os.path.join(base, "src")
    if not check_path(src_dir, is_dir=True):
        errors = True
    else:
        # [package_name] ディレクトリを特定（src内で __init__.py を持つ最初のディレクトリ）
        package_dir = None
        for entry in os.listdir(src_dir):
            entry_path = os.path.join(src_dir, entry)
            if os.path.isdir(entry_path) and check_path(os.path.join(entry_path, "__init__.py"), required=False):
                package_dir = entry_path
                package_name = entry  # パッケージ名として利用
                break
        if not package_dir:
            print("Error: No Python package directory found in src (directory with __init__.py).")
            errors = True
        else:
            # package内の module1.py の存在確認
            module1 = os.path.join(package_dir, "module1.py")
            if not check_path(module1):
                errors = True

            # subpackage のチェック
            subpackage_dir = os.path.join(package_dir, "subpackage")
            if not check_path(subpackage_dir, is_dir=True):
                errors = True
            else:
                # __init__.py のチェック
                sub_init = os.path.join(subpackage_dir, "__init__.py")
                if not check_path(sub_init):
                    errors = True
                # module_sub.py のチェック（仕様に合わせて必須の場合）
                module_sub = os.path.join(subpackage_dir, "module_sub.py")
                if not check_path(module_sub):
                    errors = True

    # 3. tests/ 配下のチェック
    tests_dir = os.path.join(base, "tests")
    if not check_path(tests_dir, is_dir=True):
        errors = True
    else:
        # 共通テスト設定ファイル
        for test_file in ["conftest.py", "test_module1.py"]:
            if not check_path(os.path.join(tests_dir, test_file)):
                errors = True

        # integration テストディレクトリ
        integration_dir = os.path.join(tests_dir, "integration")
        if not check_path(integration_dir, is_dir=True):
            errors = True
        else:
            for int_file in ["__init__.py", "test_integration.py"]:
                if not check_path(os.path.join(integration_dir, int_file)):
                    errors = True

    # 4. docs/ 配下のチェック
    docs_dir = os.path.join(base, "docs")
    if not check_path(docs_dir, is_dir=True):
        errors = True
    else:
        source_dir = os.path.join(docs_dir, "source")
        build_dir  = os.path.join(docs_dir, "build")
        if not check_path(source_dir, is_dir=True):
            errors = True
        else:
            for doc_file in ["conf.py", "index.rst"]:
                if not check_path(os.path.join(source_dir, doc_file)):
                    errors = True
        if not check_path(build_dir, is_dir=True):
            errors = True

    # 5. scripts/ 配下のチェック
    scripts_dir = os.path.join(base, "scripts")
    if not check_path(scripts_dir, is_dir=True):
        errors = True
    else:
        # このスクリプト自身が scripts/ に存在することをチェック
        current_script = os.path.basename(__file__)
        script_path = os.path.join(scripts_dir, current_script)
        if not os.path.isfile(script_path):
            print(f"Error: Expected file '{current_script}' in scripts directory not found.")
            errors = True

    # 6. ルート直下の主要ファイルチェック
    root_files = [
        ".gitignore",
        "pyproject.toml",
        "requirements.txt",
        "README.md",
        "CODING_GUIDELINES.md",
        "PROJECT_STRUCTURE.md",
        "LICENSE",
        "setup.cfg"
    ]
    for rf in root_files:
        if not check_path(os.path.join(base, rf)):
            errors = True

    print()  # 空行で区切り

    if errors:
        print("Directory structure validation FAILED.")
        sys.exit(1)
    else:
        print("Directory structure validation PASSED.")
        sys.exit(0)

if __name__ == "__main__":
    check_structure()
