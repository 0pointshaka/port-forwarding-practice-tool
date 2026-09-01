#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ファイアウォールチェッカー
"""

import subprocess
from src.utils.logger import setup_logger

logger = setup_logger('FirewallChecker')

class FirewallChecker:
    """
    ファイアウォール設定チェッカークラス
    """
    
    @staticmethod
    def get_firewall_status():
        """
        ファイアウォールステータスを取得
        
        Returns:
            dict: ファイアウォール状態
        """
        try:
            result = subprocess.run(
                'netsh advfirewall show allprofiles',
                capture_output=True,
                text=True,
                shell=True
            )
            
            logger.info("ファイアウォールステータスを取得")
            return {
                'status': 'success',
                'output': result.stdout
            }
        except Exception as e:
            logger.error(f"ファイアウォール状態取得エラー: {e}")
            return {
                'status': 'error',
                'message': str(e)
            }
    
    @staticmethod
    def get_firewall_rules():
        """
        ファイアウォールルール一覧を取得
        
        Returns:
            dict: ファイアウォールルール
        """
        try:
            result = subprocess.run(
                'netsh advfirewall firewall show rule name=all',
                capture_output=True,
                text=True,
                shell=True
            )
            
            logger.info("ファイアウォールルール一覧を取得")
            return {
                'status': 'success',
                'rules': result.stdout
            }
        except Exception as e:
            logger.error(f"ファイアウォールルール取得エラー: {e}")
            return {
                'status': 'error',
                'message': str(e)
            }
    
    @staticmethod
    def add_rule(rule_name, port, protocol='tcp', direction='in'):
        """
        ファイアウォールルールを追加
        
        Args:
            rule_name: ルール名
            port: ポート番号
            protocol: プロトコル（tcp/udp）
            direction: 方向（in/out）
        
        Returns:
            dict: 実行結果
        """
        try:
            cmd = f'netsh advfirewall firewall add rule name="{rule_name}" dir={direction} action=allow protocol={protocol} localport={port}'
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                shell=True
            )
            
            if result.returncode == 0:
                logger.info(f"ルール '{rule_name}' を追加しました")
                return {
                    'status': 'success',
                    'message': f"ルール '{rule_name}' が追加されました"
                }
            else:
                logger.error(f"ルール追加エラー: {result.stderr}")
                return {
                    'status': 'error',
                    'message': result.stderr
                }
        except Exception as e:
            logger.error(f"ルール追加例外: {e}")
            return {
                'status': 'error',
                'message': str(e)
            }
    
    @staticmethod
    def delete_rule(rule_name):
        """
        ファイアウォールルールを削除
        
        Args:
            rule_name: ルール名
        
        Returns:
            dict: 実行結果
        """
        try:
            cmd = f'netsh advfirewall firewall delete rule name="{rule_name}"'
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                shell=True
            )
            
            if result.returncode == 0:
                logger.info(f"ルール '{rule_name}' を削除しました")
                return {
                    'status': 'success',
                    'message': f"ルール '{rule_name}' が削除されました"
                }
            else:
                logger.error(f"ルール削除エラー: {result.stderr}")
                return {
                    'status': 'error',
                    'message': result.stderr
                }
        except Exception as e:
            logger.error(f"ルール削除例外: {e}")
            return {
                'status': 'error',
                'message': str(e)
            }
