#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
システム情報取得ユーティリティ
"""

import socket
import subprocess
import re
from src.utils.logger import setup_logger

logger = setup_logger('SystemInfo')

def get_local_ip():
    """
    ローカルIPアドレスを取得
    
    Returns:
        str: ローカルIPアドレス
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        logger.error(f"ローカルIP取得エラー: {e}")
        return "127.0.0.1"

def get_listening_ports():
    """
    リッスンしているポート一覧を取得
    
    Returns:
        list: リッスンしているポート番号のリスト
    """
    try:
        result = subprocess.run(
            'netstat -ano | findstr LISTENING',
            capture_output=True,
            text=True,
            shell=True
        )
        
        ports = []
        for line in result.stdout.split('\n'):
            if line.strip():
                # ポート番号を抽出
                match = re.search(r':(\d+)\s+', line)
                if match:
                    port = int(match.group(1))
                    if port not in ports:
                        ports.append(port)
        
        return sorted(ports)
    except Exception as e:
        logger.error(f"リッスンポート取得エラー: {e}")
        return []

def get_firewall_rules():
    """
    ファイアウォールルール一覧を取得
    
    Returns:
        list: ファイアウォールルールのリスト
    """
    try:
        result = subprocess.run(
            'netsh advfirewall firewall show rule name=all',
            capture_output=True,
            text=True,
            shell=True
        )
        
        return result.stdout
    except Exception as e:
        logger.error(f"ファイアウォール設定取得エラー: {e}")
        return "ファイアウォール設定を取得できませんでした"

def check_firewall_enabled():
    """
    ファイアウォールが有効か確認
    
    Returns:
        bool: ファイアウォールが有効な場合True
    """
    try:
        result = subprocess.run(
            'netsh advfirewall show allprofiles',
            capture_output=True,
            text=True,
            shell=True
        )
        
        # "State ON" を検索
        return 'State ON' in result.stdout or 'State                                ON' in result.stdout
    except Exception as e:
        logger.error(f"ファイアウォール有効確認エラー: {e}")
        return False
