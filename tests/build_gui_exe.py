#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
打包脚本：将GUI程序打包为exe可执行文件
"""

import os
import shutil
import subprocess
import sys

def build_gui_exe():
    """构建GUI exe文件"""
    
    print("="*80)
    print("2025年度架构与技术管理处员工评价系统 - GUI EXE打包")
    print("="*80)
    
    # 清理旧的dist和build目录
    print("\n【步骤1】清理旧文件...")
    if os.path.exists('dist'):
        shutil.rmtree('dist')
        print("✓ 删除旧dist目录")
    if os.path.exists('build'):
        shutil.rmtree('build')
        print("✓ 删除旧build目录")
    if os.path.exists('员工评价管理系统GUI.spec'):
        os.remove('员工评价管理系统GUI.spec')
        print("✓ 删除旧spec文件")
    
    # 使用PyInstaller打包
    print("\n【步骤2】使用PyInstaller打包...")
    cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--onefile',  # 打包为单个exe文件
        '--windowed',  # 不显示控制台窗口（GUI应用）
        '--name', '员工评价管理系统',  # exe名称
        '--icon=NONE',  # 不使用图标
        '--hidden-import=openpyxl',  # 隐式导入
        '--hidden-import=tkinter',  # 隐式导入tkinter
        'gui_main.py'  # 主程序
    ]
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✓ PyInstaller打包成功")
    except subprocess.CalledProcessError as e:
        print("✗ PyInstaller打包失败")
        print(e.stderr)
        return False
    
    # 复制必要的文件到dist目录
    print("\n【步骤3】复制必要文件到dist目录...")
    dist_dir = 'dist'
    
    files_to_copy = [
        '人员配置表2025.xlsx',
        '2025年度架构与技术管理处员工评价表.xlsx',
    ]
    
    for file in files_to_copy:
        if os.path.exists(file):
            shutil.copy(file, os.path.join(dist_dir, file))
            print(f"✓ 复制 {file}")
    
    # 生成使用说明
    print("\n【步骤4】生成使用说明...")
    readme_content = """================================================================================
2025年度架构与技术管理处员工评价系统 - GUI版本使用说明
================================================================================

【系统说明】

这是一个员工评价系统的GUI版本。无需安装Python即可运行。

【快速开始】

1. 双击运行 "员工评价管理系统.exe"
2. 在GUI界面中选择配置文件和评分文件
3. 点击"开始评分计算"按钮
4. 程序会自动生成评分汇总表

【文件说明】

本目录中的文件：
  - 员工评价管理系统.exe - 主程序（GUI版本）
  - 人员配置表2025.xlsx - 人员和权重配置（必需）
  - 2025年度架构与技术管理处员工评价表.xlsx - 评分模板（参考用）

输出文件：
  - 2025年度架构与技术管理处人员评价汇总表.xlsx - 评分汇总结果

【重要说明】

⚠️ 本目录中的 "2025年度架构与技术管理处员工评价表.xlsx" 是空白模板，
   不包含实际的评分数据。

✓ 实际的评分数据应该来自原始目录中的 "测试文档" 文件夹。

【使用步骤】

1. 准备评分数据
   - 从原始目录的 "测试文档" 文件夹中获取所有评分表文件
   - 这些文件包含各评分人对各员工的评分数据

2. 运行程序
   - 双击 "员工评价管理系统.exe"
   - 在GUI界面中：
     a) 点击"选择配置文件"，选择本目录中的 "人员配置表2025.xlsx"
     b) 点击"添加评价文件"，选择 "测试文档" 文件夹中的所有评分表文件
     c) 点击"开始评分计算"

3. 查看结果
   - 程序会自动生成结果文件
   - 打开 "2025年度架构与技术管理处人员评价汇总表.xlsx" 查看详细评分

【权重规则】

普通员工：
  最终得分 = 处长评价×20% + 副处长评价×30% + 组长评价×30% + 其他人员互评×20%

组长/小队长：
  最终得分 = 处长评价×40% + 副处长评价×30% + 其他人员互评×30%

【常见问题】

Q: 为什么输出的评分都是0？
A: 检查是否选择了正确的评分文件。应该选择 "测试文档" 文件夹中的文件，
   而不是本目录中的模板文件。

Q: 找不到配置文件？
A: 确保 "人员配置表2025.xlsx" 在程序同一目录中

Q: 如何修改配置？
A: 编辑 "人员配置表2025.xlsx" 中的相关Sheet

【技术信息】

- 基于Python 3.9+
- 使用openpyxl库处理Excel文件
- 使用tkinter库实现GUI
- 使用PyInstaller打包为exe

================================================================================
"""
    
    with open(os.path.join(dist_dir, 'README.txt'), 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print("✓ 生成README.txt")
    
    # 完成
    print("\n" + "="*80)
    print("✓ GUI EXE打包完成！")
    print("="*80)
    print(f"\n生成的文件位置：{os.path.abspath(dist_dir)}")
    print(f"主程序：{os.path.join(dist_dir, '员工评价管理系统.exe')}")
    print("\n可以直接运行exe文件，无需安装Python！")
    print("="*80)
    
    return True

if __name__ == '__main__':
    success = build_gui_exe()
    sys.exit(0 if success else 1)

