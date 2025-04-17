# 🚀 《崩坏：星穹铁道》Windows端注册表帧率修改工具

![Version](https://img.shields.io/badge/版本-1.0-blue)
![Python](https://img.shields.io/badge/Python-3.7+-green?logo=python)
![Platform](https://img.shields.io/badge/平台-Windows_10/11-0078d7?logo=windows)

## 功能
- **自动请求管理员权限**
- **快速修改游戏帧率 (120 FPS)**

## 快速使用
- 确保安装 python 并且有标准库
```python
import winreg
import ctypes
import sys
import argparse
```
- 下载 starrail_fps_tool.py 文件
- cmd 进入文件目录，运行以下代码

```cmd
# 查看帮助
python starrail_fps_tool.py

# 设置为120帧（通常只能设置为120）
python starrail_fps_tool.py 120

# 恢复默认60帧
python starrail_fps_tool.py --revert