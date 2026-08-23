"""
调试row长度问题
"""
import openpyxl

test_file = '测试文档_20251211/2025年度架构与技术管理处员工评价表-王岳珑.xlsx'
wb = openpyxl.load_workbook(test_file)
ws = wb['员工评价表']

print("检查所有行的长度...")
print()

for row_idx, row in enumerate(ws.iter_rows(min_row=4, values_only=True), start=4):
    if not row[1]:  # 考评对象为空，停止
        print(f"Row {row_idx}: 考评对象为空，停止")
        break
    
    evaluated_name = row[1]
    row_len = len(row)
    
    print(f"Row {row_idx}: {evaluated_name:8} - {row_len} columns")
    
    if row_len < 8:
        print(f"  WARNING: row长度不足！")
        for col_idx, val in enumerate(row):
            print(f"    [{col_idx}]: {val}")

