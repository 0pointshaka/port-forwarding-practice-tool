#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
メインウィンドウ
"""

import PySimpleGUI as sg
from pathlib import Path
from src.utils.logger import setup_logger
from src.gui.learning_dialog import LearningDialog
from src.gui.tools_dialog import ToolsDialog

logger = setup_logger('MainWindow')

class MainWindow:
    """
    メインウィンドウクラス
    """
    
    def __init__(self):
        """
        初期化
        """
        self.window = None
        self.learning_dialog = LearningDialog()
        self.tools_dialog = ToolsDialog()
    
    def create_layout(self):
        """
        レイアウトの作成
        
        Returns:
            list: レイアウト
        """
        layout = [
            [sg.Text('ポート開放練習ツール', font=('メイリオ', 16, 'bold'), text_color='#2E86AB')],
            [sg.Text('Windowsでのポート開放手順を実践的に学習', font=('メイリオ', 10))],
            [sg.Separator()],
            
            [sg.Frame('学習と練習', [
                [sg.Button('📚 基礎知識を学ぶ', size=(25, 2), key='-LEARN-')],
                [sg.Button('🎯 実践演習', size=(25, 2), key='-PRACTICE-')],
            ])],
            
            [sg.Frame('診断・検証ツール', [
                [sg.Button('🔍 ポート状態確認', size=(25, 2), key='-PORT_CHECK-')],
                [sg.Button('🔧 ファイアウォール設定確認', size=(25, 2), key='-FW_CHECK-')],
                [sg.Button('📡 ポートスキャン', size=(25, 2), key='-SCAN-')],
                [sg.Button('🔗 テスト接続', size=(25, 2), key='-TEST_CONNECTION-')],
            ])],
            
            [sg.Separator()],
            [sg.Button('終了', size=(25, 1), key='-EXIT-')],
        ]
        
        return layout
    
    def run(self):
        """
        ウィンドウを実行
        """
        layout = self.create_layout()
        
        self.window = sg.Window(
            'ポート開放練習ツール',
            layout,
            finalize=True,
            size=(400, 600)
        )
        
        logger.info("メインウィンドウを表示")
        
        while True:
            event, values = self.window.read()
            
            if event == sg.WINDOW_CLOSED or event == '-EXIT-':
                logger.info("アプリケーションを終了")
                break
            
            elif event == '-LEARN-':
                self.learning_dialog.show_basics()
            
            elif event == '-PRACTICE-':
                self.learning_dialog.show_practice()
            
            elif event == '-PORT_CHECK-':
                self.tools_dialog.check_ports()
            
            elif event == '-FW_CHECK-':
                self.tools_dialog.check_firewall()
            
            elif event == '-SCAN-':
                self.tools_dialog.port_scan()
            
            elif event == '-TEST_CONNECTION-':
                self.tools_dialog.test_connection()
        
        self.window.close()
