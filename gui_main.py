#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ポート開放練習ツール - GUI版メインプログラム

Windowsでのポート開放手順を実践的に学べるツール
EXE形式で動作
"""

import PySimpleGUI as sg
import sys
import os
from pathlib import Path

# パスを追加
sys.path.insert(0, str(Path(__file__).parent))

from src.gui.main_window import MainWindow
from src.utils.logger import setup_logger

# ロガーの設定
logger = setup_logger('GUI')

# PySimpleGUIのテーマ設定
sg.theme('LightBlue2')
sg.set_options(font=('メイリオ', 10), margins=(10, 10))

def main():
    """
    メイン処理
    """
    try:
        logger.info("ポート開放練習ツール GUI版を起動します")
        window = MainWindow()
        window.run()
    except Exception as e:
        logger.error(f"エラーが発生しました: {e}", exc_info=True)
        sg.popup_error(f"エラーが発生しました:\n{str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
