#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ロギング機能
"""

import logging
import sys
from pathlib import Path
from datetime import datetime

# ログディレクトリの作成
LOG_DIR = Path(__file__).parent.parent.parent / 'logs'
LOG_DIR.mkdir(exist_ok=True)

def setup_logger(name, level=logging.INFO):
    """
    ロガーの設定
    
    Args:
        name: ロガー名
        level: ログレベル
    
    Returns:
        logger: 設定済みのロガーオブジェクト
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # フォーマッタの設定
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # ファイルハンドラ
    log_file = LOG_DIR / f'{name}_{datetime.now().strftime("%Y%m%d")}.log'
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # コンソールハンドラ
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger
