# クイックスタートガイド

## 最も簡単な実行方法（Windows）

### 方法1：run.bat をダブルクリック（推奨）

```
1. run.bat をダブルクリック
2. 自動でEXE を生成・実行します
3. アプリケーションが立ち上がります

初回は EXE 生成に 1-2 分かかります
```

### 方法2：EXE を直接実行

```
dist/PortForwardingPracticeTool.exe をダブルクリック
```

## セットアップ（一度だけ必要）

### Windows

```bash
# 1. Python 3.8以上がインストール済みか確認
python --version

# 2. 依存ライブラリをインストール
pip install -r requirements.txt
pip install -r requirements-build.txt

# 3. EXEを生成（オプション）
python build_exe.py

# 完了！これ以降は run.bat をダブルクリックで実行
```

### Linux/Mac

```bash
# 1. Python 3.8以上がインストール済みか確認
python3 --version

# 2. 仮想環境を作成
python3 -m venv venv
source venv/bin/activate  # Mac/Linux

# 3. 依存ライブラリをインストール
pip install -r requirements.txt

# 4. GUI版を実行
python3 gui_main.py
```

## ファイル説明

| ファイル | 説明 |
|---------|------|
| `run.bat` | Windows用ワンクリック実行スクリプト |
| `run.py` | Python用実行スクリプト |
| `build_exe.py` | EXE生成スクリプト |
| `gui_main.py` | GUI版メインプログラム |
| `dist/PortForwardingPracticeTool.exe` | 生成されたEXEファイル |

## トラブルシューティング

### EXE が起動しない

```
1. run.bat をもう一度実行
2. それでもダメな場合：
   - コマンドプロンプトを「管理者として実行」
   - python run.py を実行
```

### Python が見つからない

```
1. Python 3.8以上をインストール
   https://www.python.org/

2. インストール時に「Add Python to PATH」にチェック

3. コマンドプロンプトを再度開いて実行
```

### PySimpleGUI エラー

```bash
pip install PySimpleGUI --upgrade
```

### 詳細なトラブルシューティング

詳細は `docs/04_troubleshooting.md` を参照してください。

## よくある質問

### Q: EXE ファイルはどこにある？
**A:** `dist/PortForwardingPracticeTool.exe` にあります

### Q: USB メモリで別の PC で使える？
**A:** はい、EXE をコピーして直接実行できます

### Q: ポート開放の実装は？
**A:** 学習画面に手順が記載されています。実際のコマンド実行は管理者権限が必要です

### Q: オンラインで実行できる？
**A:** いいえ、Windows PC に PyInstaller でビルドしたEXEが必要です

## 次のステップ

1. **アプリを起動**
   - `run.bat` をダブルクリック

2. **基礎知識を学ぶ**
   - メニューから「基礎知識を学ぶ」を選択

3. **実践演習に挑戦**
   - 段階別のガイドに従う

4. **ポート開放を実装**
   - コマンドプロンプト（管理者）でコマンド実行

5. **検証ツールで確認**
   - ツールでポートの開放状態を確認

## サポート

質問やバグ報告は GitHub Issues でお願いします：
https://github.com/0pointshaka/port-forwarding-practice-tool/issues
