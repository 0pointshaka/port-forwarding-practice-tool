#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
接続テスター
"""

import socket
import subprocess
from src.utils.logger import setup_logger

logger = setup_logger('ConnectionTester')

class ConnectionTester:
    """
    接続テスタークラス
    """
    
    @staticmethod
    def test_tcp_connection(host, port, timeout=5):
        """
        TCP接続をテスト
        
        Args:
            host: テスト対象ホスト
            port: テスト対象ポート
            timeout: タイムアウト時間（秒）
        
        Returns:
            dict: テスト結果
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            sock.close()
            
            if result == 0:
                logger.info(f"{host}:{port} への接続成功")
                return {
                    'status': 'success',
                    'message': f"{host}:{port} への接続に成功しました"
                }
            else:
                logger.warning(f"{host}:{port} への接続失敗")
                return {
                    'status': 'failed',
                    'message': f"{host}:{port} への接続に失敗しました（接続タイムアウト）"
                }
        except socket.gaierror as e:
            logger.error(f"ホスト名解決エラー: {e}")
            return {
                'status': 'error',
                'message': f"ホスト '{host}' が見つかりません"
            }
        except Exception as e:
            logger.error(f"接続テストエラー: {e}")
            return {
                'status': 'error',
                'message': str(e)
            }
    
    @staticmethod
    def test_ping(host, timeout=5):
        """
        PING接続をテスト
        
        Args:
            host: テスト対象ホスト
            timeout: タイムアウト時間（秒）
        
        Returns:
            dict: テスト結果
        """
        try:
            # Windows の ping コマンド
            result = subprocess.run(
                f'ping -n 1 -w {timeout*1000} {host}',
                capture_output=True,
                text=True,
                shell=True
            )
            
            if result.returncode == 0:
                logger.info(f"{host} へのPING成功")
                return {
                    'status': 'success',
                    'message': f"{host} は応答しています",
                    'details': result.stdout
                }
            else:
                logger.warning(f"{host} へのPING失敗")
                return {
                    'status': 'failed',
                    'message': f"{host} は応答していません"
                }
        except Exception as e:
            logger.error(f"PING実行エラー: {e}")
            return {
                'status': 'error',
                'message': str(e)
            }
