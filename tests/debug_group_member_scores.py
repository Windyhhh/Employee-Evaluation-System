#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
调试脚本：验证业务架构组成员的评分是否正确计入副处长和组长维度
"""
import openpyxl
import os
import sys

# 导入主程序
import main

def verify_group_member_scores():
    """验证业务架构组成员的评分"""
    
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
            print(f"  层级: {member.level}")
            print(f"  score[1]（副处长评价）:")
            print(f"    维度1: {member.score1[1].score}/{member.score1[1].num} = {member.score1[1].get_score():.2f}")
            print(f"    维度2: {member.score2[1].score}/{member.score2[1].num} = {member.score2[1].get_score():.2f}")
            print(f"    维度3: {member.score3[1].score}/{member.score3[1].num} = {member.score3[1].get_score():.2f}")
            print(f"  score[2]（组长评价）:")
            print(f"    维度1: {member.score1[2].score}/{member.score1[2].num} = {member.score1[2].get_score():.2f}")
            print(f"    维度2: {member.score2[2].score}/{member.score2[2].num} = {member.score2[2].get_score():.2f}")
            print(f"    维度3: {member.score3[2].score}/{member.score3[2].num} = {member.score3[2].get_score():.2f}")
    
    print("\n" + "=" * 80)
    print("技术管理组成员的评分数据（王丽丽作为组长）")
    print("=" * 80)
    
    # 查看技术管理组成员的评分
    for name in ['杨磊磊', '王建伟', '刘歆毅', '文静', '汪国辉', '徐艳婷']:
        if name in main.MERITS_MAP:
            member = main.MERITS_MAP[name]
            print(f"\n{name}:")
            print(f"  层级: {member.level}")
            print(f"  score[1]（副处长评价）:")
            print(f"    维度1: {member.score1[1].score}/{member.score1[1].num} = {member.score1[1].get_score():.2f}")
            print(f"  score[2]（组长评价）:")
            print(f"    维度1: {member.score1[2].score}/{member.score1[2].num} = {member.score1[2].get_score():.2f}")

if __name__ == '__main__':
    verify_group_member_scores()

