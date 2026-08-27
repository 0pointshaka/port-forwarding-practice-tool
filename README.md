# ポート開放練習ツール (Windows EXE版)

Windowsでのポート開放手順を実践的に学べるガイド付き練習ツールです。EXE形式で簡単に起動でき、初心者から中級者向けに段階的にポート開放の概念と実装方法を習得できます。

## 機能

### 📚 学習モード
- **基礎知識講座**: ポートとは、ファイアウォール、ポート開放の必要性など
- **ステップバイステップガイド**: Windows Defender ファイアウォール設定方法
- **実践演習**: 段階別の練習課題

### 🔍 診断・検証ツール
- ポートの開放状態を確認
- ファイアウォール設定の確認
- ポートスキャン（ローカル/リモート）
- テスト接続の実施

### 💻 シミュレーション機能
- ファイアウォール設定のシミュレーション
- ポート開放手順のステップバイステップデモ
- 設定前後での動作比較

## システム要件

- **OS**: Windows 10 / Windows 11
- **Python**: 3.8以上（開発環境のみ）
- **権限**: 管理者権限が必要な操作あり

## インストール

### 方法1: EXE版を使用（推奨）
1. [Releases](https://github.com/0pointshaka/port-forwarding-practice-tool/releases)からEXEをダウンロード
2. ダブルクリックで起動
3. GUIメニューで操作

### 方法2: Pythonから実行
```bash
# リポジトリをクローン
git clone https://github.com/0pointshaka/port-forwarding-practice-tool.git
cd port-forwarding-practice-tool

# 依存ライブラリをインストール
pip install -r requirements.txt

# GUI版を起動
python main.py --gui
```

## 使用方法

### EXE版を起動
`PortForwardingPracticeTool.exe` をダブルクリック

### GUIメニュー
メイン画面から以下のボタンをクリック：
1. **基礎知識を学ぶ** - ポート開放の基礎講座
2. **実践演習** - 段階別の練習課題
3. **ポート状態確認** - 開放状態を確認
4. **ファイアウォール設定確認** - 現在の設定を表示
5. **ポートスキャン** - ポートをスキャン
6. **テスト接続** - 接続テスト

## ディレクトリ構成

```
port-forwarding-practice-tool/
├── main.py                      # メインプログラム
├── gui_main.py                  # GUI版メインプログラム
├── build_exe.py                 # EXE生成スクリプト
├── requirements.txt             # 依存ライブラリ
├── requirements-gui.txt         # GUI用ライブラリ
├── README.md
├── src/
│   ├── __init__.py
│   ├── gui/                     # GUI関連
│   │   ├── __init__.py
│   │   ├── main_window.py      # メインウィンドウ
│   │   ├── learning_dialog.py  # 学習画面
│   │   ├── tools_dialog.py     # ツール画面
│   │   └── styles.py           # UI スタイル
│   ├── learning/               # 学習モジュール
│   │   ├── __init__.py
│   │   ├── basics.py          # 基礎知識
│   │   └── tutorials.py       # チュートリアル
│   ├── tools/                  # ツール群
│   │   ├── __init__.py
│   │   ├── port_scanner.py    # ポートスキャン
│   │   ├── firewall_checker.py # ファイアウォール確認
│   │   └── connection_tester.py # テスト接続
│   ├── simulation/             # シミュレーション
│   │   ├── __init__.py
│   │   ├── firewall_sim.py    # FW設定シミュレーション
│   │   └── steps.py           # 手順シミュレーション
│   └── utils/                  # ユーティリティ
│       ├── __init__.py
│       ├── system_info.py     # システム情報取得
│       └── logger.py          # ログ機能
├── docs/
│   ├── 01_basics.md           # ポートの基礎
│   ├── 02_firewall.md         # ファイアウォール解説
│   ├── 03_setup_guide.md      # セットアップガイド
│   └── 04_troubleshooting.md  # トラブルシューティング
├── dist/
│   └── PortForwardingPracticeTool.exe  # 生成されたEXE
└── tests/
    ├── test_scanner.py
    ├── test_firewall.py
    └── test_tools.py
```

## 学習フロー

```
1. 基礎知識の学習（GUIで読み進める）
   ↓
2. Windowsファイアウォールの理解
   ↓
3. シミュレーションで手順を実践
   ↓
4. 実際の設定に挑戦
   ↓
5. 診断ツールで検証
```

## EXEの生成方法（開発者向け）

```bash
# PyInstallerをインストール
pip install pyinstaller

# EXEを生成
python build_exe.py
```

生成されたEXEは `dist/PortForwardingPracticeTool.exe` に出力されます。

## トラブルシューティング

### よくある質問
- **EXEが起動しない**: Windows Defender がブロックしている可能性があります。「詳細情報」をクリックして「実行」を選択してください
- **管理者権限が必要な場合**: EXEを右クリック → 「管理者として実行」を選択
- **ファイアウォール設定が反映されない**: PCの再起動が必要な場合があります
- **ポートがまだ開いていない**: 設定反映に数秒かかることがあります

詳細は[トラブルシューティング](docs/04_troubleshooting.md)を参照してください。

## ライセンス

MIT License

## 貢献

改善提案やバグ報告は Issues をお願いします。

## サポート

質問や不明な点がある場合は、Discussions をご利用ください。
