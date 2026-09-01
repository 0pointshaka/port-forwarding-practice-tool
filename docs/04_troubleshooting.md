# トラブルシューティング

## よくの問題と解決方法

## 1. ツール起動に関する問題

### EXEが起動しない

#### 症状
- ダブルクリックしても何も起こらない
- または、すぐに閉じてしまう

#### 原因と対策

**原因1: Windows Defender がブロックしている**
```
1. EXEファイルを右クリック
2. 「プロパティ」をクリック
3. "ブロックを解除"チェックボックスをチェック
4. 「適用」をクリック
5. 再度実行
```

**原因2: 依存ファイルが見つからない**
```
EXEが生成されたフォルダに以下が必要です：
- src/ ディレクトリ
- docs/ ディレクトリ
- assets/ ディレクトリ
```

**原因3: Python関連の問題**
```bash
# 再度EXEをビルド
python build_exe.py
```

### GUI版が起動しない

#### コマンドプロンプトでのエラーメッセージを確認

```bash
# 管理者として実行
cd port-forwarding-practice-tool
venv\Scripts\activate
python gui_main.py
```

#### 一般的なエラーと対策

**エラー: ModuleNotFoundError: No module named 'PySimpleGUI'**
```bash
# PySimpleGUIを再インストール
pip install PySimpleGUI --upgrade
```

**エラー: ModuleNotFoundError: No module named 'src'**
```bash
# プロジェクトディレクトリにいることを確認
cd port-forwarding-practice-tool
python gui_main.py
```

## 2. ポート開放に関する問題

### ポート開放コマンドが実行できない

#### 症状
- "アクセスが拒否されました"エラー
- または"このコマンドは見つかりません"と表示される

#### 解決方法

**管理者権限で実行していない**
```
1. コマンドプロンプトを終了
2. コマンドプロンプトを右クリック
3. "管理者として実行"をクリック
4. 再度コマンドを実行
```

**コマンド構文が間違っている**
```bash
# 正しい構文
netsh advfirewall firewall add rule name="ルール名" \
dir=in action=allow protocol=tcp localport=ポート番号

# 例（ポート8080）
netsh advfirewall firewall add rule name="Test8080" \
dir=in action=allow protocol=tcp localport=8080
```

### ポート開放設定が反映されない

#### 症状
- ファイアウォール設定は完了したが、アクセスできない
- ツールのポート確認で「閉鎖」と表示される

#### 原因と対策

**設定反映の遅延**
- コマンド実行後、30秒～1分待つ
- その間、アプリケーションが起動しているか確認

**アプリケーションが起動していない**
```bash
# Webサーバーを起動（例）
python -m http.server 8080
```

**ファイアウォール自体が無効になっている**
```
1. コントロールパネルを開く
2. "Windows Defender ファイアウォール"をクリック
3. "Windows Defender ファイアウォールの有効化/無効化"をクリック
4. 両方のプロファイルを有効化
```

**PCの再起動が必要な場合**
```
設定が反映されない場合、PCを再起動してみてください
```

### ファイアウォール設定確認コマンドが動作しない

#### 症状
- ツールのファイアウォール確認ボタンを押してもエラーが表示される

#### 解決方法

**管理者権限で実行**
```bash
# 管理者として実行したコマンドプロンプトから
netsh advfirewall show allprofiles
```

## 3. ネットワーク関連の問題

### ポートスキャンが動作しない

#### 症状
- ツールのポートスキャン機能が使用できない
- またはスキャン結果が表示されない

#### 原因と対策

**機能がまだ実装されていない**
- 現バージョンではポートスキャン機能は開発中です
- 代替方法として、別のツール（例：nmap）の使用を検討してください

### テスト接続が失敗する

#### 症状
- ポートを開放しても、テスト接続で失敗する
- または、外部から接続できない

#### チェックリスト

1. **ポート番号が正しいか確認**
   ```bash
   # 開放されているポートを確認
   netsh advfirewall firewall show rule name=all
   ```

2. **アプリケーションが起動しているか確認**
   ```bash
   # ポートをリッスンしているプロセスを確認
   netstat -ano | findstr :8080
   ```

3. **ファイアウォール設定が正しいか確認**
   - ポート番号が正確
   - プロトコル（TCP/UDP）が正確
   - 受信（in）/送信（out）が正確

4. **ルーターのポート開放設定**
   - ルーター機能を使用している場合、ルーターレベルでもポート開放が必要な場合があります

## 4. その他の問題

### ツールの使用方法がわからない

#### メニューの説明

| ボタン | 説明 |
|-------|------|
| 基礎知識を学ぶ | ポート開放の基本を学習 |
| 実践演習 | ステップバイステップのガイド付き練習 |
| ポート状態確認 | 特定のポートが開いているか確認 |
| ファイアウォール設定確認 | 現在のファイアウォール設定を表示 |
| ポートスキャン | （開発中）ポートをスキャン |
| テスト接続 | （開発中）接続テスト |

### ログファイルを確認したい

#### ログファイルの場所
```
port-forwarding-practice-tool/logs/
```

#### ログの閲覧
```bash
# 最新のログを表示
type logs\GUI_20260827.log
```

### セキュリティの警告が表示される

#### 対策

1. **Windows Defender がEXEをブロック**
   - EXEのプロパティで「ブロックを解除」をチェック

2. **"このアプリは危険な可能性があります"メッセージ**
   - 「詳細情報」をクリック
   - "実行"をクリック

## 5. サポート方法

### バグを報告する

以下の情報を含めて Issue を作成してください：

```
【環境】
- Windows バージョン
- Python バージョン
- ツールバージョン

【症状】
- 何が起こったか
- どうなるはずだったか

【手順】
- 問題を再現する手順
- 実行したコマンド

【エラーメッセージ】
- 表示されたエラーメッセージ
```

### 質問をする

Discussions で質問できます。
以下の情報を含めてください：

- 何を達成したいのか
- これまで試したこと
- エラーメッセージまたはスクリーンショット

## リソース

- [Microsoft ドキュメント：Windows ファイアウォール](https://docs.microsoft.com/ja-jp/windows/security/threat-protection/windows-firewall/windows-firewall-with-advanced-security)
- [netsh コマンド リファレンス](https://docs.microsoft.com/ja-jp/windows-server/networking/technologies/netsh/netsh-contexts)
- [ポート番号の一覧](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)
