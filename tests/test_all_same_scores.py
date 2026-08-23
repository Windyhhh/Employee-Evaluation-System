"""
测试全员互评 - 所有人打分都一样，但输出结果不同
"""
import sys
import os
import shutil
sys.path.insert(0, '.')

# 清理旧的输出文件
output_file = '2025年度架构与技术管理处人员评价汇总表.xlsx'
if os.path.exists(output_file):
    os.remove(output_file)
    print(f"已删除旧文件: {output_file}")

# 复制全员互评文件到主目录
test_dir = '全员互评'
files = sorted([f for f in os.listdir(test_dir) if f.endswith('.xlsx')])

print(f"\n复制 {len(files)} 个全员互评文件到主目录...")
for file in files:
    src = os.path.join(test_dir, file)
    dst = file
    shutil.copy(src, dst)
    print(f"  OK: {file}")

# 导入并运行主程序
from main import init, computed, out

print("\n初始化配置...")
init()

print("计算评分...")
computed()

print("输出结果...")
out()

print(f"\n✅ 完成！输出文件: {output_file}")

# 检查输出结果
import openpyxl
wb = openpyxl.load_workbook(output_file)
ws = wb['评分汇总']

print("\n=== 输出结果前10行 ===")
print()

for row_idx, row in enumerate(ws.iter_rows(min_row=1, max_row=11, values_only=True), start=1):
    if row_idx == 1:
        print(f"{'排名':<4} {'姓名':<8} {'层级':<8} {'处长':<6} {'副处长':<6} {'组长':<6} {'互评':<6} {'总分':<6}")
        print("-" * 60)
    else:
        rank, group, name, level, director, vice_dir, group_leader, other, total = row
        print(f"{rank:<4} {name:<8} {level:<8} {director:<6} {vice_dir:<6} {group_leader:<6} {other:<6} {total:<6}")

print()
print("问题：所有人打分都一样（非常满足），但输出结果不同")

