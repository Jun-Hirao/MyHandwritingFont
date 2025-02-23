#!/usr/bin/env node
/**
 * validate_structure.js
 *
 * このスクリプトは、プロジェクトのディレクトリ構造が定義どおりになっているかを検証します。
 * 検証対象のディレクトリ・ファイルは、下記の "expectedStructure" オブジェクトに定義されています。
 *
 * 使用方法:
 *   node scripts/validate_structure.js
 */

const fs = require('fs');
const path = require('path');

/**
 * expectedStructure:
 * プロジェクトのルートディレクトリからの相対パスで必要なディレクトリやファイルを定義します。
 *
 * - サブオブジェクトの場合はディレクトリとして扱い、その中のファイル/ディレクトリを検証します。
 * - 値が "file" の場合はファイルとして、"dir" の場合は空のディレクトリとして存在を確認します。
 */
const expectedStructure = {
  ".github": {
    "workflows": {
      "validate-structure.yml": "file"
    },
    "ISSUE_TEMPLATE": {
      "FEATURE_REQUEST.md": "file"
    }
  },
  "src": {
    "main.js": "file",
    "preload.js": "file",
    "renderer": {
      "index.html": "file",
      "renderer.js": "file",
      "style.css": "file"
    }
  },
  "tests": {
    "unit": {
      "test_main.js": "file",
      "test_renderer.js": "file"
    },
    "integration": {
      "test_integration.js": "file",
      "helper.js": "file"
    }
  },
  "dist": "dir",
  "docs": {
    "source": {
      "index.md": "file",
      "config.yml": "file"
    },
    "build": "dir"  // ドキュメント生成物が配置されるディレクトリ（空の場合も許容）
  },
  "scripts": {
    "validate_structure.js": "file",
    "build.js": "file"
  },
  "vendor": {
    "node": "dir"
  },
  "node_modules": "dir",
  ".gitignore": "file",
  "package.json": "file",
  "package-lock.json": "file",
  "README.md": "file",
  "CODING_GUIDELINES.md": "file",
  "PROJECT_STRUCTURE.md": "file",
  "LICENSE": "file",
  "electron-packager-config.json": "file"
};

/**
 * validateStructure
 *
 * @param {string} baseDir - 現在検証中のディレクトリの絶対パス
 * @param {object|string} structureObj - 検証する構造定義。オブジェクトの場合はディレクトリ、文字列の場合は "file" または "dir"
 * @returns {boolean} - 全ての検証が成功した場合 true、失敗があれば false
 */
function validateStructure(baseDir, structureObj) {
  let isValid = true;

  if (typeof structureObj === 'string') {
    // structureObjが単一の "file" または "dir" 指定の場合は、baseDir自体の検証を行う
    if (structureObj === "file") {
      if (!fs.existsSync(baseDir) || !fs.lstatSync(baseDir).isFile()) {
        console.error(`Missing file: ${baseDir}`);
        return false;
      }
    } else if (structureObj === "dir") {
      if (!fs.existsSync(baseDir) || !fs.lstatSync(baseDir).isDirectory()) {
        console.error(`Missing directory: ${baseDir}`);
        return false;
      }
    }
    return true;
  }

  // 構造がオブジェクトの場合、キーを順次検証
  for (const key in structureObj) {
    const expected = structureObj[key];
    const fullPath = path.join(baseDir, key);

    if (typeof expected === "string") {
      // 単一のファイルまたはディレクトリの存在確認
      if (expected === "file") {
        if (!fs.existsSync(fullPath) || !fs.lstatSync(fullPath).isFile()) {
          console.error(`Missing file: ${fullPath}`);
          isValid = false;
        }
      } else if (expected === "dir") {
        if (!fs.existsSync(fullPath) || !fs.lstatSync(fullPath).isDirectory()) {
          console.error(`Missing directory: ${fullPath}`);
          isValid = false;
        }
      }
    } else if (typeof expected === "object") {
      // オブジェクトの場合はディレクトリとして存在するか確認
      if (!fs.existsSync(fullPath) || !fs.lstatSync(fullPath).isDirectory()) {
        console.error(`Missing directory: ${fullPath}`);
        isValid = false;
      } else {
        // 再帰的に内部の構造を検証
        const subValid = validateStructure(fullPath, expected);
        if (!subValid) {
          isValid = false;
        }
      }
    }
  }
  return isValid;
}

/**
 * main
 *
 * リポジトリのルートディレクトリから検証を実施します。
 */
function main() {
  // スクリプトが配置されているディレクトリから見たリポジトリのルート（例: scripts/から1階層上）
  const repoRoot = path.resolve(__dirname, '..');
  const structureValid = validateStructure(repoRoot, expectedStructure);

  if (!structureValid) {
    console.error("Project structure validation failed.");
    process.exit(1);
  } else {
    console.log("Project structure validated successfully.");
    process.exit(0);
  }
}

main();
