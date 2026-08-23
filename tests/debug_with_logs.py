"""
带日志的调试
"""
import sys
import os
import shutil
import logging
sys.path.insert(0, '.')

# 设置日志级别为DEBUG
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

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
from main import init, init_config, computed, out

print("初始化配置...")
init()
init_config()

print("\n计算评分...")
computed()

print("\n输出结果...")
out()

