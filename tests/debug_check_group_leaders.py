"""
检查GROUP_LEADERS
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

# 导入并运行主程序
from main import init, init_config, computed, MERITS_MAP, GROUP_LEADERS

init()
init_config()

# 检查王岳珑的信息
wang_yuanlong = MERITS_MAP.get('王岳珑')
print(f'王岳珑的group: {wang_yuanlong.group}')
print(f'王岳珑的level: {wang_yuanlong.level}')

# 检查GROUP_LEADERS
print(f'\nGROUP_LEADERS ({len(GROUP_LEADERS)} items):')
for group, leader in sorted(GROUP_LEADERS.items()):
    print(f'  {group}: {leader}')

# 检查是否王岳珑是业务架构组的组长
group_name = '业务架构组'
leader_name = GROUP_LEADERS.get(group_name)
print(f'\n业务架构组的组长: {leader_name}')
print(f'王岳珑是否是业务架构组的组长: {wang_yuanlong.name == leader_name}')

computed()

