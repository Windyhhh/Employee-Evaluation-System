"""
调试王岳珑和王丽丽的评分问题
"""
import sys
import os
import shutil
sys.path.insert(0, '.')

# 清理旧的输出文件
output_file = '2025年度架构与技术管理处人员评价汇总表.xlsx'
if os.path.exists(output_file):
    os.remove(output_file)

# 使用测试文档_20251211中的王岳珑和王丽丽的评分
test_dir = '测试文档_20251211'
files = [
    '2025年度架构与技术管理处员工评价表-王岳珑.xlsx',
    '2025年度架构与技术管理处员工评价表-王丽丽.xlsx'
]

print("复制王岳珑和王丽丽的评分文件...")
for file in files:
    src = os.path.join(test_dir, file)
    if os.path.exists(src):
        shutil.copy(src, file)
        print(f"  OK: {file}")

# 导入并运行主程序
from main import init, init_config, computed, out, MERITS_MAP

print("\n初始化配置...")
init()
init_config()

print("\n计算评分...")
computed()

print("\n输出结果...")
out()

# 检查王岳珑和王丽丽的评分
print("\n=== 王岳珑的评分 ===")
wang_yuanlong = MERITS_MAP.get('王岳珑')
if wang_yuanlong:
    print(f"姓名: {wang_yuanlong.name}")
    print(f"职能组: {wang_yuanlong.group}")
    print(f"层级: {wang_yuanlong.level}")
    print(f"副处长评价(score1[1]): {wang_yuanlong.score1[1].get_score()}")
    print(f"组长评价(score1[2]): {wang_yuanlong.score1[2].get_score()}")
    print(f"其他人员互评(score1[4]): {wang_yuanlong.score1[4].get_score()}")

print("\n=== 王丽丽的评分 ===")
wang_lili = MERITS_MAP.get('王丽丽')
if wang_lili:
    print(f"姓名: {wang_lili.name}")
    print(f"职能组: {wang_lili.group}")
    print(f"层级: {wang_lili.level}")
    print(f"副处长评价(score1[1]): {wang_lili.score1[1].get_score()}")
    print(f"组长评价(score1[2]): {wang_lili.score1[2].get_score()}")
    print(f"其他人员互评(score1[4]): {wang_lili.score1[4].get_score()}")

# 检查业务架构组的成员
print("\n=== 业务架构组成员的评分 ===")
for name, member in MERITS_MAP.items():
    if member.group == '业务架构组' and member.level == '普通员工':
        print(f"\n{name}:")
        print(f"  副处长评价(score1[1]): {member.score1[1].get_score()}")
        print(f"  组长评价(score1[2]): {member.score1[2].get_score()}")
        print(f"  其他人员互评(score1[4]): {member.score1[4].get_score()}")
        break

