"""
详细调试王岳珑和王丽丽的评分
"""
import sys
import os
import shutil
sys.path.insert(0, '.')

# 清理旧的输出文件
output_file = '2025年度架构与技术管理处人员评价汇总表.xlsx'
if os.path.exists(output_file):
    os.remove(output_file)

# 只使用王岳珑的评分文件
test_dir = '测试文档_20251211'
file = '2025年度架构与技术管理处员工评价表-王岳珑.xlsx'

src = os.path.join(test_dir, file)
shutil.copy(src, file)
print(f"复制: {file}")

# 导入并运行主程序
from main import init, init_config, computed, out, MERITS_MAP, GROUP_LEADERS, STAFF_LEADERS

print("\n初始化配置...")
init()
init_config()

print(f"\nGROUP_LEADERS: {GROUP_LEADERS}")
print(f"STAFF_LEADERS: {STAFF_LEADERS}")

# 检查王岳珑的信息
wang_yuanlong = MERITS_MAP.get('王岳珑')
print(f"\n王岳珑的信息:")
print(f"  name: {wang_yuanlong.name}")
print(f"  group: {wang_yuanlong.group}")
print(f"  level: {wang_yuanlong.level}")
print(f"  是否在STAFF_LEADERS中: {wang_yuanlong.name in STAFF_LEADERS}")

# 检查业务架构组的组长
print(f"\n业务架构组的组长: {GROUP_LEADERS.get('业务架构组')}")

# 检查高琦的信息
gaoqi = MERITS_MAP.get('高琦')
print(f"\n高琦的信息:")
print(f"  name: {gaoqi.name}")
print(f"  group: {gaoqi.group}")
print(f"  level: {gaoqi.level}")
print(f"  是否在STAFF_LEADERS中: {gaoqi.name in STAFF_LEADERS}")

print("\n计算评分...")
computed()

print("\n输出结果...")
out()

# 检查王岳珑的评分
print("\n=== 王岳珑的评分详情 ===")
wang_yuanlong = MERITS_MAP.get('王岳珑')
print(f"副处长评价(score1[1]): {wang_yuanlong.score1[1].get_score()}")
print(f"  score1[1].score: {wang_yuanlong.score1[1].score}")
print(f"  score1[1].num: {wang_yuanlong.score1[1].num}")
print(f"组长评价(score1[2]): {wang_yuanlong.score1[2].get_score()}")
print(f"  score1[2].score: {wang_yuanlong.score1[2].score}")
print(f"  score1[2].num: {wang_yuanlong.score1[2].num}")

# 检查高琦的评分
print("\n=== 高琦的评分详情 ===")
gaoqi = MERITS_MAP.get('高琦')
print(f"副处长评价(score1[1]): {gaoqi.score1[1].get_score()}")
print(f"  score1[1].score: {gaoqi.score1[1].score}")
print(f"  score1[1].num: {gaoqi.score1[1].num}")
print(f"组长评价(score1[2]): {gaoqi.score1[2].get_score()}")
print(f"  score1[2].score: {gaoqi.score1[2].score}")
print(f"  score1[2].num: {gaoqi.score1[2].num}")

