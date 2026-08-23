'''
Author: yl_li
Date: 2023-12-11
LastEditors: yl_li
LastEditTime: 2024-12-21
description: GUI版本的员工评价管理系统
'''
import os
import sys
import logging
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import src.main as main

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s',
    handlers=[logging.StreamHandler()]
)

class ScoreEvalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("员工评价管理系统")
        self.root.geometry("700x600")
        self.root.resizable(False, False)

        self.config_file = None
        self.merits_files = []
        self.execute_btn = None

        self.setup_ui()
    
    def setup_ui(self):
        """设置用户界面"""
        # 标题
        title_label = tk.Label(self.root, text="员工评价管理系统", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # 配置文件选择
        config_frame = tk.LabelFrame(self.root, text="第一步：选择配置文件", padx=10, pady=10)
        config_frame.pack(padx=10, pady=5, fill="x")

        self.config_label = tk.Label(config_frame, text="未选择", fg="gray", font=("Arial", 10))
        self.config_label.pack(side="left", fill="x", expand=True)

        config_btn = tk.Button(config_frame, text="选择配置文件", command=self.select_config_file,
                              bg="#4CAF50", fg="white", padx=10)
        config_btn.pack(side="right", padx=5)

        # 评价文件选择
        merits_frame = tk.LabelFrame(self.root, text="第二步：添加评价文件", padx=10, pady=10)
        merits_frame.pack(padx=10, pady=5, fill="both", expand=True)

        # 文件列表
        self.merits_listbox = tk.Listbox(merits_frame, height=8)
        self.merits_listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(merits_frame, command=self.merits_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.merits_listbox.config(yscrollcommand=scrollbar.set)

        # 按钮框
        button_frame = tk.Frame(self.root)
        button_frame.pack(padx=10, pady=5, fill="x")

        add_btn = tk.Button(button_frame, text="添加评价文件", command=self.add_merits_file,
                           bg="#2196F3", fg="white")
        add_btn.pack(side="left", padx=5)

        remove_btn = tk.Button(button_frame, text="移除选中", command=self.remove_merits_file,
                              bg="#FF9800", fg="white")
        remove_btn.pack(side="left", padx=5)

        clear_btn = tk.Button(button_frame, text="清空列表", command=self.clear_merits_files,
                             bg="#f44336", fg="white")
        clear_btn.pack(side="left", padx=5)

        # 进度条
        self.progress = ttk.Progressbar(self.root, mode='indeterminate')
        self.progress.pack(padx=10, pady=5, fill="x")

        # 状态标签
        self.status_label = tk.Label(self.root, text="就绪", fg="green", font=("Arial", 10))
        self.status_label.pack(pady=5)

        # 执行按钮
        self.execute_btn = tk.Button(self.root, text="第三步：开始评分计算", command=self.execute,
                                    bg="#4CAF50", fg="white", font=("Arial", 12, "bold"),
                                    padx=20, pady=10)
        self.execute_btn.pack(padx=10, pady=10, fill="x")
    
    def select_config_file(self):
        """选择配置文件"""
        file = filedialog.askopenfilename(
            title="选择配置文件",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
        )
        if file:
            self.config_file = file
            self.config_label.config(text=os.path.basename(file), fg="black")
    
    def add_merits_file(self):
        """添加评价文件"""
        files = filedialog.askopenfilenames(
            title="选择评价文件",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
        )
        for file in files:
            if file not in self.merits_files:
                self.merits_files.append(file)
                self.merits_listbox.insert(tk.END, os.path.basename(file))
    
    def remove_merits_file(self):
        """移除选中的评价文件"""
        selection = self.merits_listbox.curselection()
        if selection:
            index = selection[0]
            self.merits_listbox.delete(index)
            del self.merits_files[index]
    
    def clear_merits_files(self):
        """清空评价文件列表"""
        self.merits_listbox.delete(0, tk.END)
        self.merits_files = []
    
    def execute(self):
        """执行评分计算"""
        # 验证配置文件
        if not self.config_file:
            messagebox.showerror("错误", "❌ 请先选择配置文件！")
            return

        if not os.path.exists(self.config_file):
            messagebox.showerror("错误", f"❌ 配置文件不存在：\n{self.config_file}")
            self.config_file = None
            self.config_label.config(text="未选择", fg="gray")
            return

        # 验证评价文件
        if not self.merits_files:
            messagebox.showerror("错误", "❌ 请先添加评价文件！")
            return

        # 检查所有评价文件是否存在
        missing_files = [f for f in self.merits_files if not os.path.exists(f)]
        if missing_files:
            messagebox.showerror("错误", f"❌ 以下文件不存在：\n" + "\n".join(missing_files))
            return

        # 禁用执行按钮，防止重复点击
        self.execute_btn.config(state="disabled")

        # 在新线程中执行，避免阻塞 GUI
        thread = threading.Thread(target=self.run_calculation)
        thread.daemon = True
        thread.start()
    
    def run_calculation(self):
        """运行计算逻辑"""
        try:
            self.progress.start()
            self.status_label.config(text="正在处理...", fg="blue")
            self.root.update()

            # 设置全局变量
            main.CONFIG_FILE_PATH = self.config_file
            main.MERITS_FILE_PATH_LIST.clear()
            main.MERITS_FILE_PATH_LIST.extend(self.merits_files)
            main.MERITS_MAP.clear()

            # 执行计算
            logging.info(f"开始处理，配置文件：{os.path.basename(self.config_file)}")
            logging.info(f"评价文件数量：{len(self.merits_files)}")

            # 初始化（设置工作目录和输出文件路径）
            main.init(auto_scan=False)
            main.init_config()
            main.check_file()
            main.computed()
            main.out()

            self.progress.stop()
            self.status_label.config(text="✓ 完成！", fg="green")

            # 显示成功信息
            result_file = main.RESULT_FILE_PATH
            result_name = os.path.basename(result_file) if result_file else "输出文件"
            messagebox.showinfo("✓ 成功", f"评分计算完成！\n\n输出文件：\n{result_name}")

            logging.info(f"处理完成，输出文件：{result_file}")

        except Exception as e:
            self.progress.stop()
            self.status_label.config(text="✗ 错误", fg="red")
            error_msg = str(e)
            messagebox.showerror("✗ 错误", f"处理过程中出错：\n{error_msg}")
            logging.error(f"Error: {error_msg}", exc_info=True)

        finally:
            # 重新启用执行按钮
            self.execute_btn.config(state="normal")

def run_gui():
    root = tk.Tk()
    app = ScoreEvalGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()

