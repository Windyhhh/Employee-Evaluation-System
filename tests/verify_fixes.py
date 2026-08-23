#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
验证脚本：验证所有修复是否正确
"""
import main
import os
import openpyxl

def verify_all_fixes():
    """验证所有修复"""
    
    # 初始化
    main.init(auto_scan=False)
    main.CONFIG_FILE_PATH = os.path.abspath('人员配置表2025.xlsx')
    main.MERITS_FILE_PATH_LIST.clear()
    
    # 添加测试文档_20251211文件夹中的所有评分文件
    test_folder = '测试文档_20251211'
    if os.path.exists(test_folder):
        for f in os.listdir(test_folder):
            if f.endswith('.xlsx'):
                main.MERITS_FILE_PATH_LIST.append(os.path.abspath(os.path.join(test_folder, f)))
    
    # 初始化配置
    main.init_config()
    
    print("=" * 80)
    print("验证修复1：王岳珑和王丽丽的角色配置")
    print("=" * 80)
    
    # 验证王岳珑和王丽丽的配置
    for name in ['王岳珑', '王丽丽']:
        if name in main.MERITS_MAP:
            member = main.MERITS_MAP[name]
            print(f"\n{name}:")
            print(f"  层级: {member.level}")
            assert member.level == '副处长', f"错误：{name}的层级应该是副处长，但是{member.level}"
            print(f"  ✓ 层级正确")
    
    # 读取评分数据
    main.check_file()
    main.computed()
    
    print("\n" + "=" * 80)
    print("验证修复2：小队长能被组长评价")
    print("=" * 80)
    
    # 验证彭亮（小队长）有组长评价
    if '彭亮' in main.MERITS_MAP:
        member = main.MERITS_MAP['彭亮']
        group_leader_score = member.score1[2].get_score()
        print(f"\n彭亮（小队长）的组长评价: {group_leader_score:.2f}")
        assert group_leader_score > 0, "错误：彭亮应该有组长评价"
        print(f"  ✓ 小队长能被组长评价")
    
    print("\n" + "=" * 80)
    print("验证修复3：王岳珑和王丽丽的评分同时计入副处长和组长维度")
    print("=" * 80)
    
    # 验证业务架构组成员的副处长评价和组长评价
    for name in ['高琦', '马芳琳', '李晓婧']:
        if name in main.MERITS_MAP:
            member = main.MERITS_MAP[name]
            vice_director = member.score1[1].get_score()
            group_leader = member.score1[2].get_score()
            print(f"\n{name}:")
            print(f"  副处长评价: {vice_director:.2f}")
            print(f"  组长评价: {group_leader:.2f}")
            assert vice_director > 0, f"错误：{name}应该有副处长评价"
            assert group_leader > 0, f"错误：{name}应该有组长评价"
            print(f"  ✓ 评分同时计入副处长和组长维度")
    
    print("\n" + "=" * 80)
    print("验证修复4：王岳珑和王丽丽不在输出结果中")
    print("=" * 80)
    
    # 输出结果
    main.out()
    
    # 检查输出文件
    file_path = main.RESULT_FILE_PATH
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active
    
    found_wang = False
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row[2] in ['王岳珑', '王丽丽']:
            found_wang = True
            break
    
    assert not found_wang, "错误：王岳珑和王丽丽不应该在输出结果中"
    print("\n✓ 王岳珑和王丽丽已正确排除")
    
    print("\n" + "=" * 80)
    print("所有修复验证完成！✓")
    print("=" * 80)

if __name__ == '__main__':
    verify_all_fixes()

