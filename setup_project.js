#!/usr/bin/env node
/**
 * setup_project.js
 *
 * プロジェクト開発開始時に必要なディレクトリとファイルを自動生成するスクリプトです。
 * ファイル作成時には、最低限のサンプル内容を書き込むようにしています（サンプルであることが明確になるよう記述）。
 *
 * ※ 以下のファイル・ディレクトリは既に存在している前提のため、変更や作成は行いません。
 *   - .github/ とその中のファイル
 *   - CODING_GUIDELINES.md
 *   - PROJECT_STRUCTURE.md
 *   - README.md
 *
 * 使用方法:
 * Node.jsが使えるようにあらかじめ用意しておく
 *   node setup_project.js
 */

const fs = require('fs');
const path = require('path');

// プロジェクトの必須構造（既存のものは除外）
const projectStructure = {
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
    "build": "dir" // 空のディレクトリとして作成（ビルド成果物用）
  },
  "scripts": {
    "validate_structure.js": "file",
    "build.js": "file"
  },
  "vendor": {
    "node": "dir" // Node.js実行環境を格納する想定
  },
  "node_modules": "dir",
  ".gitignore": "file",
  "package.json": "file",
  "LICENSE": "file",
  "electron-packager-config.json": "file"
};

// 既存として扱うファイル・ディレクトリ（プロジェクトルート直下）
const skipList = [
  '.github',
  'CODING_GUIDELINES.md',
  'PROJECT_STRUCTURE.md',
  'README.md'
];

// サンプル内容の定義（プロジェクトルートからの相対パスをキーにする）
const sampleContents = {
  "src/main.js": `// Sample main.js for Electron
const { app, BrowserWindow } = require('electron');
function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: { preload: __dirname + '/preload.js' }
  });
  win.loadFile('src/renderer/index.html');
}
app.whenReady().then(createWindow);
app.on('window-all-closed', () => { if (process.platform !== 'darwin') app.quit(); });
`,
  "src/preload.js": `// Sample preload.js
window.addEventListener('DOMContentLoaded', () => {
  console.log('Preload script loaded.');
});
`,
  "src/renderer/index.html": `<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Sample Electron App</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Hello, Electron!</h1>
  <script src="renderer.js"></script>
</body>
</html>
`,
  "src/renderer/renderer.js": `// Sample renderer.js
console.log('Renderer process loaded.');
`,
  "src/renderer/style.css": `/* Sample style.css */
body { 
  font-family: Arial, sans-serif; 
  background-color: #f0f0f0; 
}
`,
  "tests/unit/test_main.js": `// Sample test_main.js
const assert = require('assert');
describe('Main Process', () => {
  it('should run sample test', () => {
    assert.strictEqual(1, 1);
  });
});
`,
  "tests/unit/test_renderer.js": `// Sample test_renderer.js
const assert = require('assert');
describe('Renderer Process', () => {
  it('should run sample test', () => {
    assert.strictEqual(1, 1);
  });
});
`,
  "tests/integration/test_integration.js": `// Sample test_integration.js
const assert = require('assert');
describe('Integration Test', () => {
  it('should run sample integration test', () => {
    assert.strictEqual(1, 1);
  });
});
`,
  "tests/integration/helper.js": `// Sample helper.js for tests
module.exports = {};
`,
  "docs/source/index.md": `# Sample Documentation
This is a sample documentation file for the Electron project.
`,
  "docs/source/config.yml": `# Sample configuration for documentation generator (e.g., MkDocs)
site_name: "Sample Electron App Documentation"
`,
  "scripts/validate_structure.js": `#!/usr/bin/env node
// Sample validate_structure.js
console.log('Validation script placeholder.');
`,
  "scripts/build.js": `#!/usr/bin/env node
// Sample build.js
console.log('Build script placeholder.');
`,
  ".gitignore": `# Sample .gitignore
node_modules/
dist/
vendor/
docs/build/
`,
  "package.json": `{
  "name": "sample-electron-app",
  "productName": "サンプルアプリ",
  "version": "0.1.0",
  "main": "src/main.js",
  "scripts": {
    "start": "electron .",
    "build": "electron-packager . --overwrite --out=dist"
  },
  "devDependencies": {
    "@electron/packager": "^18.3.6",
    "electron": "^34.1.0",
    "moment": "^2.30.1"
}
`,
  "LICENSE": `MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted...（ライセンス本文は必要に応じて追加）`,
  "electron-packager-config.json": `{
  "name": "sample-electron-app",
  "platform": "all",
  "arch": "all"
}
`
};

/**
 * createStructure
 *
 * 再帰的にディレクトリ・ファイル構造を作成する関数
 */
function createStructure(baseDir, structure, relativeBase = '') {
  for (const key in structure) {
    // プロジェクトルート直下の場合、skipListに含まれるものは処理しない
    const currentRelativePath = relativeBase ? 
      path.posix.join(relativeBase, key) : 
      key;

    if (!relativeBase && skipList.includes(key)) {
      console.log(`Skipped (pre-existing): ${currentRelativePath}`);
      continue;
    }

    const expected = structure[key];
    const fullPath = path.join(baseDir, key);

    if (typeof expected === "string") {
      if (expected === "file") {
        if (!fs.existsSync(fullPath)) {
          const content = sampleContents[currentRelativePath] || '';
          fs.writeFileSync(fullPath, content, 'utf8');
          console.log(`Created file: ${currentRelativePath}`);
        } else {
          console.log(`File exists: ${currentRelativePath}`);
        }
      } else if (expected === "dir") {
        if (!fs.existsSync(fullPath)) {
          fs.mkdirSync(fullPath, { recursive: true });
          console.log(`Created directory: ${currentRelativePath}`);
        } else {
          console.log(`Directory exists: ${currentRelativePath}`);
        }
      }
    } else if (typeof expected === "object") {
      if (!fs.existsSync(fullPath)) {
        fs.mkdirSync(fullPath, { recursive: true });
        console.log(`Created directory: ${currentRelativePath}`);
      } else {
        console.log(`Directory exists: ${currentRelativePath}`);
      }
      createStructure(fullPath, expected, currentRelativePath);
    }
  }
}

function main() {
  const projectRoot = process.cwd();
  console.log(`Setting up project structure in: ${projectRoot}`);
  createStructure(projectRoot, projectStructure);
  console.log("Project setup complete.");
}

main();
