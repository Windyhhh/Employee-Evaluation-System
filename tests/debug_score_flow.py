#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
调试脚本：追踪王岳珑、王丽丽的评分流程
"""
import openpyxl
import os
import sys
import logging

# 设置日志级别为DEBUG
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s]: %(message)s'
)

# 导入主程序
import main

def trace_scores_for_dual_role():
    """追踪王岳珑、王丽丽的评分"""
    
    # 初始化
    main.init(auto_scan=False)
    main.CONFIG_FILE_PATH = os.path.abspath('人员配置表2025.xlsx')
    main.MERITS_FILE_PATH_LIST.clear()
    
    # 添加全员互评文件
    merits_dir = '全员互评'
    for f in os.listdir(merits_dir):
        if f.endswith('.xlsx'):
            main.MERITS_FILE_PATH_LIST.append(os.path.abspath(os.path.join(merits_dir, f)))
    
    # 初始化配置
    main.init_config()
    
    print("\n" + "=" * 80)
    print("开始追踪评分流程")
    print("=" * 80 + "\n")
    
    # 读取评分数据
    main.check_file()
    main.computed()
    
    print("\n" + "=" * 80)
    print("业务架构组成员的评分数据（王岳珑作为组长）")
    print("=" * 80)
    
    # 查看业务架构组成员的评分
    for name in ['彭亮', '高琦', '马芳琳', '李晓婧']:
        if name in main.MERITS_MAP:
            member = main.MERITS_MAP[name]
            print(f"\n{name}:")
            print(f"  score[1]（副处长评价）: {member.score1[1].score}/{member.score1[1].num} = {member.score1[1].get_score():.2f}")
            print(f"  score[2]（组长评价）: {member.score1[2].score}/{member.score1[2].num} = {member.score1[2].get_score():.2f}")

if __name__ == '__main__':
    trace_scores_for_dual_role()

