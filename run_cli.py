#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
员工评价管理系统 - 命令行启动器
"""

import sys
import os

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def main():
    """主函数"""
    # 导入main模块
    import src.main as main_module
    
    # 执行main.py中的main逻辑
    main_module.init()
    main_module.init_config()
    main_module.check_file()
    main_module.computed()
    main_module.out()

if __name__ == "__main__":
    main()