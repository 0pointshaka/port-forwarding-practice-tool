#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXE生成スクリプト

PyInstallerを使用してスタンドアロンのEXEファイルを生成します
"""

import os
import subprocess
import sys
from pathlib import Path

def build_exe():
    """
    EXEファイルを生成
    """
    print("="*60)
    print("ポート開放練習ツール EXE生成")
    print("="*60)
    
    # PyInstallerが対応しているか確認
    try:
        import PyInstaller
    except ImportError:
        print("\n[エラー] PyInstallerがインストールされていません")
        print("インストール: pip install PyInstaller")
        sys.exit(1)
    
    # プロジェクトのルートディレクトリ
    project_root = Path(__file__).parent
    
    # PyInstallerのコマンド
    cmd = [
        'pyinstaller',
        '--name=PortForwardingPracticeTool',
        '--onefile',
        '--windowed',
        '--icon=assets/icon.ico' if Path('assets/icon.ico').exists() else '',
        '--add-data=src:src',
        '--add-data=docs:docs',
        '--distpath=dist',
        '--workpath=build',
        '--specpath=.',
        'gui_main.py'
    ]
    
    # 空文字列を削除
    cmd = [c for c in cmd if c]
    
    print(f"\n[実行] {' '.join(cmd)}\n")
    
    try:
        result = subprocess.run(cmd, cwd=str(project_root))
        
        if result.returncode == 0:
            print("\n" + "="*60)
            print("✓ EXE生成成功！")
            print("="*60)
            print(f"\n出力先: {project_root / 'dist' / 'PortForwardingPracticeTool.exe'}")
            print("\nダブルクリックで起動できます。")
        else:
            print("\n[エラー] EXE生成に失敗しました")
            sys.exit(1)
            
    except Exception as e:
        print(f"\n[エラー] {e}")
        sys.exit(1)

if __name__ == '__main__':
    build_exe()
