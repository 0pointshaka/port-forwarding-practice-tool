#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
学習ダイアログ
"""

import PySimpleGUI as sg
from src.utils.logger import setup_logger

logger = setup_logger('LearningDialog')

class LearningDialog:
    """
    学習ダイアログクラス
    """
    
    def show_basics(self):
        """
        基礎知識を表示
        """
        content = """
【ポート開放について】

ポートとは？
  - コンピュータが通信する際の「窓口」です
  - 0～65535の番号が付与されています
  - 複数のアプリケーションが異なるポートを使用します

ファイアウォールとは？
  - コンピュータへの不正なアクセスを防ぐセキュリティ機能です
  - デフォルトではすべてのポートが「閉じた」状態です
  - 必要に応じて特定のポートを「開く」設定をします

ポート開放の必要性：
  - ゲームのマルチプレイ機能
  - リモートデスクトップ接続
  - Webサーバーの公開
  - その他ネットワークアプリケーション

【Windows Defenderファイアウォール】

アクセス許可ポートの確認方法：
  1. コントロールパネルを開く
  2. 「Windows Defender ファイアウォール」をクリック
  3. 「アプリケーションをファイアウォール経由で許可」をクリック

ポートを開く手順：
  1. コマンドプロンプトを管理者として実行
  2. netsh advfirewall firewall add rule コマンドを実行
  3. 設定が反映されるまで数秒待機
  4. ポート確認ツールで検証

【よくある質問】

Q. ポートを開くと危険では？
A. セキュリティリスクがあります。必要最小限のポートのみ開き、
   定期的に設定を確認することをお勧めします。

Q. 複数のアプリケーションで同じポートは使用できる？
A. いいえ。同じポート番号は1つのアプリケーションのみが
   使用できます。
        """
        
        layout = [
            [sg.Text('基礎知識', font=('メイリオ', 14, 'bold'))],
            [sg.Multiline(content, size=(60, 25), disabled=True, 
                         font=('メイリオ', 9))],
            [sg.Button('閉じる', size=(10, 1))]
        ]
        
        window = sg.Window('基礎知識', layout, finalize=True)
        logger.info("基礎知識ウィンドウを表示")
        
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == '閉じる':
                break
        
        window.close()
    
    def show_practice(self):
        """
        実践演習を表示
        """
        content = """
【実践演習】

レベル1：基本的なポート操作
  課題: ポート8080を開く
  手順:
    1. コマンドプロンプトを管理者として実行
    2. 以下のコマンドを実行:
       netsh advfirewall firewall add rule name="Test Port 8080" \
       dir=in action=allow protocol=tcp localport=8080
    3. ポート状態確認ツールでポート8080が開いているか確認
  
  テスト方法: ポートスキャンツールを使用して確認

レベル2：複数ポートの管理
  課題: ポート3306（MySQL）と5432（PostgreSQL）を開く
  手順:
    1. ポート3306を開く:
       netsh advfirewall firewall add rule name="MySQL" \
       dir=in action=allow protocol=tcp localport=3306
    2. ポート5432を開く:
       netsh advfirewall firewall add rule name="PostgreSQL" \
       dir=in action=allow protocol=tcp localport=5432
    3. 両方のポートが開いていることを確認

レベル3：ポートのクローズ
  課題: 開いたポートを閉じる
  手順:
    1. 設定したポートを削除:
       netsh advfirewall firewall delete rule name="Test Port 8080"
    2. ポートが閉じたことを確認

【チェックリスト】

□ 基礎知識を理解できた
□ ポートを開く手順を実行できた
□ 開いたポートを確認できた
□ ポートをクローズできた
□ すべてのポート操作を完了した
        """
        
        layout = [
            [sg.Text('実践演習', font=('メイリオ', 14, 'bold'))],
            [sg.Multiline(content, size=(60, 25), disabled=True, 
                         font=('メイリオ', 9))],
            [sg.Button('閉じる', size=(10, 1))]
        ]
        
        window = sg.Window('実践演習', layout, finalize=True)
        logger.info("実践演習ウィンドウを表示")
        
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == '閉じる':
                break
        
        window.close()
