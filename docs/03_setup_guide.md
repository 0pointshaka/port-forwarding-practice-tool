# セットアップガイド

## 開発環境のセットアップ

### 前提条件
- Windows 10/11
- Python 3.8以上がインストール済み
- 管理者権限がある

### ステップ1: リポジトリをクローン

```bash
git clone https://github.com/0pointshaka/port-forwarding-practice-tool.git
cd port-forwarding-practice-tool
```

### ステップ2: 仮想環境を作成（推奨）

```bash
# 仮想環境を作成
python -m venv venv

# 仮想環境を有効化
venv\Scripts\activate
```

### ステップ3: 依存ライブラリをインストール

```bash
pip install -r requirements.txt
```

### ステップ4: GUI版を実行

```bash
python gui_main.py
```

## EXE版のビルド

### 前提条件
- 開発環境がセットアップ済み
- PyInstallerがインストール済み

### ビルド手順

#### ステップ1: PyInstallerをインストール

```bash
pip install PyInstaller
```

#### ステップ2: EXEを生成

```bash
python build_exe.py
```

#### ステップ3: EXEの確認

```
dist/PortForwardingPracticeTool.exe が生成されます
```

### EXEの配布

EXEファイルをスタンドアロンで配布できます：

```
PortForwardingPracticeTool.exe
├─ assets/
├─ docs/
└─ src/
```

## トラブルシューティング

### Pythonがインストールされていない

1. [Python公式サイト](https://www.python.org/)にアクセス
2. 最新バージョンをダウンロード
3. インストーラーを実行
4. "Add Python to PATH"にチェック
5. "Install Now"をクリック

### gitコマンドが認識されない

1. [Git公式サイト](https://git-scm.com/)にアクセス
2. Windowsバージョンをダウンロード
3. インストーラーを実行
4. デフォルト設定でインストール

### 依存ライブラリのインストール失敗

```bash
# キャッシュをクリア
pip cache purge

# 再度インストール
pip install -r requirements.txt --no-cache-dir
```

### EXEビルドが失敗する

```bash
# PyInstallerを再インストール
pip uninstall PyInstaller
pip install PyInstaller --upgrade

# 再度ビルド
python build_exe.py
```

### GUI が起動しない

1. コマンドプロンプトを管理者として実行
2. 仮想環境を有効化
3. `python gui_main.py` を実行
4. エラーメッセージを確認

## ポート開放の実践

### 基本的な流れ

#### 1. アプリケーションを起動

ポートを使用するアプリケーション（Webサーバー等）を起動します。

```bash
# 例：Pythonで簡易Webサーバーを起動
python -m http.server 8080
```

#### 2. ファイアウォール設定

アプリケーションが使用するポートをファイアウォールで許可します。

```bash
# コマンドプロンプトを管理者として実行
netsh advfirewall firewall add rule name="Python HTTP" \
dir=in action=allow protocol=tcp localport=8080
```

#### 3. ポート状態を確認

ツールのポート状態確認機能を使用して、ポートが開いていることを確認します。

#### 4. 外部からアクセステスト（オプション）

別のPC（またはスマートフォン）から、あなたのPCのIPアドレスとポート番号でアクセスします。

```
http://[あなたのPCのIPアドレス]:8080
```

## よくある質問

### Q: ファイアウォール設定後、すぐにアクセスできない
**A:** 設定反映に数秒かかります。30秒程度待ってから再度試してください。

### Q: ポート開放が本当に成功したか確認したい
**A:** ツールのポート状態確認機能を使用してください。ポート開放確認ツールも利用できます。

### Q: 複数のポートを一度に開きたい
**A:** コマンドプロンプトで複数の `netsh` コマンドを実行してください。

```bash
netsh advfirewall firewall add rule name="Rule1" dir=in action=allow protocol=tcp localport=8080
netsh advfirewall firewall add rule name="Rule2" dir=in action=allow protocol=tcp localport=3306
netsh advfirewall firewall add rule name="Rule3" dir=in action=allow protocol=tcp localport=5432
```

### Q: ポートを閉じるにはどうしたら良い？
**A:** ルールを削除します。

```bash
netsh advfirewall firewall delete rule name="ルール名"
```
