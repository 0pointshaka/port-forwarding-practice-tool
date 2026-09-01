#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ポートスキャナーツール
"""

import socket
import threading
from concurrent.futures import ThreadPoolExecutor
from src.utils.logger import setup_logger

logger = setup_logger('PortScanner')

class PortScanner:
    """
    ポートスキャナークラス
    """
    
    def __init__(self, host='127.0.0.1', timeout=2):
        """
        初期化
        
        Args:
            host: スキャン対象ホスト
            timeout: タイムアウト時間（秒）
        """
        self.host = host
        self.timeout = timeout
        self.open_ports = []
    
    def scan_port(self, port):
        """
        単一ポートをスキャン
        
        Args:
            port: ポート番号
        
        Returns:
            bool: ポートが開いている場合True
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.host, port))
            sock.close()
            
            if result == 0:
                self.open_ports.append(port)
                logger.info(f"ポート {port} が開いています")
                return True
            return False
        except Exception as e:
            logger.error(f"ポート {port} スキャンエラー: {e}")
            return False
    
    def scan_range(self, start_port, end_port, max_workers=10):
        """
        ポート範囲をスキャン
        
        Args:
            start_port: 開始ポート
            end_port: 終了ポート
            max_workers: スレッド数
        
        Returns:
            list: 開いているポート番号のリスト
        """
        logger.info(f"{self.host} の {start_port}-{end_port} をスキャン開始")
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            for port in range(start_port, end_port + 1):
                executor.submit(self.scan_port, port)
        
        logger.info(f"スキャン完了: 開いているポート {sorted(self.open_ports)}")
        return sorted(self.open_ports)
    
    def get_open_ports(self):
        """
        開いているポートを取得
        
        Returns:
            list: 開いているポート番号のリスト
        """
        return self.open_ports
