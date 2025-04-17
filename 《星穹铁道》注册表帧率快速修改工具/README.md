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
- 管理员运行 cmd 进入文件目录，运行以下代码

```cmd
# 查看帮助
python starrail_fps_tool.py

# 设置为120帧（通常只能设置为120）
python starrail_fps_tool.py 120

# 恢复默认60帧
python starrail_fps_tool.py --revert
```

## ⚠️ 重要警告
- 操作前必须完全关闭游戏进程
- 修改前建议导出注册表备份：
  reg export HKCU\Software\miHoYo "%USERPROFILE%\Desktop\mihoyo_backup.reg"
- 超频可能导致设备过热
+ 成功提示示例：
  [√] 已成功设置 120 FPS！请重启游戏生效

## 免责声明
- **本工具为开源学习项目，非官方软件**
- **仅个人与好友使用**
- **使用即表示知晓可能出现游戏文件损坏等意外情况**
- **使用即表示知晓可能导致的封号风险**
- **不得用于商业用途及非法修改**
