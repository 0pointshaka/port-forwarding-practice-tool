#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
診断・検証ツールダイアログ
"""

import PySimpleGUI as sg
import socket
import subprocess
import os
from src.utils.logger import setup_logger

logger = setup_logger('ToolsDialog')

class ToolsDialog:
    """
    診断・検証ツールダイアログクラス
    """
    
    def check_ports(self):
        """
        ポート状態を確認
        """
        try:
            layout = [
                [sg.Text('ポート状態確認', font=('メイリオ', 14, 'bold'))],
                [sg.Text('確認するポート番号を入力してください:')],
                [sg.InputText(key='-PORT-', size=(10, 1)), 
                 sg.Button('確認', size=(10, 1))],
                [sg.Multiline(size=(50, 15), key='-OUTPUT-', disabled=True)],
                [sg.Button('閉じる', size=(10, 1))]
            ]
            
            window = sg.Window('ポート状態確認', layout, finalize=True)
            logger.info("ポート状態確認ウィンドウを表示")
            
            while True:
                event, values = window.read()
                
                if event == sg.WINDOW_CLOSED or event == '閉じる':
                    break
                
                if event == '確認':
                    try:
                        port = int(values['-PORT-'])
                        result = self._check_port(port)
                        window['-OUTPUT-'].update(result)
                    except ValueError:
                        sg.popup_error('ポート番号は数字で入力してください')
                    except Exception as e:
                        window['-OUTPUT-'].update(f'エラー: {str(e)}')
            
            window.close()
        except Exception as e:
            logger.error(f"ポート状態確認エラー: {e}")
            sg.popup_error(f'エラーが発生しました: {str(e)}')
    
    def _check_port(self, port):
        """
        ポートが開いているか確認
        
        Args:
            port: ポート番号
        
        Returns:
            str: 確認結果
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex(('127.0.0.1', port))
            sock.close()
            
            if result == 0:
                return f"ポート {port}: 開放状態 ✓"
            else:
                return f"ポート {port}: 閉鎖状態 ✗"
        except Exception as e:
            return f"エラー: {str(e)}"
    
    def check_firewall(self):
        """
        ファイアウォール設定を確認
        """
        try:
            result = subprocess.run(
                'netsh advfirewall show allprofiles',
                capture_output=True,
                text=True,
                shell=True
            )
            
            layout = [
                [sg.Text('ファイアウォール設定確認', font=('メイリオ', 14, 'bold'))],
                [sg.Multiline(result.stdout, size=(60, 20), disabled=True,
                             font=('メイリオ', 9))],
                [sg.Button('閉じる', size=(10, 1))]
            ]
            
            window = sg.Window('ファイアウォール設定確認', layout, finalize=True)
            logger.info("ファイアウォール設定確認ウィンドウを表示")
            
            while True:
                event, values = window.read()
                if event == sg.WINDOW_CLOSED or event == '閉じる':
                    break
            
            window.close()
        except Exception as e:
            logger.error(f"ファイアウォール確認エラー: {e}")
            sg.popup_error(f'エラーが発生しました: {str(e)}')
    
    def port_scan(self):
        """
        ポートスキャンを実行
        """
        sg.popup_info('ポートスキャン機能は開発中です')
        logger.info("ポートスキャン機能へのアクセス")
    
    def test_connection(self):
        """
        テスト接続を実行
        """
        sg.popup_info('テスト接続機能は開発中です')
        logger.info("テスト接続機能へのアクセス")
