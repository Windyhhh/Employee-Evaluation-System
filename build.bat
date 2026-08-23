@echo off
REM 员工评价管理系统 - Windows部署脚本

echo ========================================
echo 员工评价管理系统 - 构建和部署脚本
echo ========================================

REM 检查Python环境
echo 正在检查Python环境...
python --version
if errorlevel 1 (
    echo 错误: 未找到Python环境，请先安装Python 3.8+
    pause
    exit /b 1
)

REM 检查pip
echo 正在检查pip...
pip --version
if errorlevel 1 (
    echo 错误: 未找到pip
    pause
    exit /b 1
)

REM 安装依赖
echo 正在安装依赖...
pip install -r requirements.txt
if errorlevel 1 (
    echo 警告: 依赖安装失败，尝试继续...
)

REM 运行测试（如果有）
if exist tests (
    echo 正在运行测试...
    python -m pytest tests/ -v
    if errorlevel 1 (
        echo 警告: 测试失败，但继续构建...
    )
)

REM 构建可执行文件
echo 正在构建可执行文件...
pyinstaller --clean --onefile --windowed --name "员工评价管理系统" --icon=icon.ico run_gui.py 2>nul
if errorlevel 1 (
    echo 正在使用无图标构建...
    pyinstaller --clean --onefile --windowed --name "员工评价管理系统" run_gui.py
)

if exist dist (
    echo 构建完成! 可执行文件位置: dist\员工评价管理系统.exe
) else (
    echo 构建失败!
)

echo ========================================
echo 部署完成!
echo ========================================
pause