#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
调试脚本：分析王岳珑、王丽丽双重角色的评分处理问题
"""
import openpyxl
import os
import sys

# 导入主程序
import main

def analyze_dual_role_scores():
    """分析王岳珑、王丽丽的评分处理"""
    
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
    
    print("=" * 80)
    print("人员配置信息")
    print("=" * 80)
    print(f"处长: {main.DIRECTOR}")
    print(f"职能组组长: {main.GROUP_LEADERS}")
    print(f"员工组长/小队长: {list(main.STAFF_LEADERS.keys())}")
    print()
    
    # 检查王岳珑和王丽丽的配置
    print("=" * 80)
    print("王岳珑和王丽丽的配置")
    print("=" * 80)
    for name in ['王岳珑', '王丽丽']:
        if name in main.MERITS_MAP:
            member = main.MERITS_MAP[name]
            print(f"{name}:")
            print(f"  职能组: {member.group}")
            print(f"  组长: {member.group_leader}")
            print(f"  层级: {member.level}")
            print(f"  是否为组长/小队长: {name in main.STAFF_LEADERS}")
        print()
    
    # 读取评分数据
    main.check_file()
    main.computed()
    
    print("=" * 80)
    print("王岳珑的评分数据")
    print("=" * 80)
    if '王岳珑' in main.MERITS_MAP:
        member = main.MERITS_MAP['王岳珑']
        print(f"维度1（敏捷自驱）:")
        for i, score in enumerate(member.score1):
            print(f"  score[{i}]: {score.score}/{score.num} = {score.get_score():.2f}")
        print(f"维度2（追求卓越）:")
        for i, score in enumerate(member.score2):
            print(f"  score[{i}]: {score.score}/{score.num} = {score.get_score():.2f}")
        print(f"维度3（超越自我）:")
        for i, score in enumerate(member.score3):
            print(f"  score[{i}]: {score.score}/{score.num} = {score.get_score():.2f}")
    print()
    
    print("=" * 80)
    print("王丽丽的评分数据")
    print("=" * 80)
    if '王丽丽' in main.MERITS_MAP:
        member = main.MERITS_MAP['王丽丽']
        print(f"维度1（敏捷自驱）:")
        for i, score in enumerate(member.score1):
            print(f"  score[{i}]: {score.score}/{score.num} = {score.get_score():.2f}")
        print(f"维度2（追求卓越）:")
        for i, score in enumerate(member.score2):
            print(f"  score[{i}]: {score.score}/{score.num} = {score.get_score():.2f}")
        print(f"维度3（超越自我）:")
        for i, score in enumerate(member.score3):
            print(f"  score[{i}]: {score.score}/{score.num} = {score.get_score():.2f}")
    print()

if __name__ == '__main__':
    analyze_dual_role_scores()

