#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
员工评价管理系统 - GUI启动器
"""

import sys
import os

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import tkinter as tk
from src.gui_main import ScoreEvalGUI

def main():
    """主函数"""
    root = tk.Tk()
    app = ScoreEvalGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()